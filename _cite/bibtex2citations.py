import bibtexparser
from bibtexparser.bwriter import BibTexWriter
import yaml

def parse_authors(authors_text):

    author_list = map(str.strip, authors_text.split("and"))
    author_list = [[str.strip(el) for el in aut.split(",")[::-1]] for aut in author_list]
    author_list = [" ".join(aut) for aut in author_list]

    #author_list = list(map(lambda x: " ".join(x.split(",")[::-1]), author_list))

    return author_list

def read_bibtex(filename):

    # Convert back to BibTeX string using writer
    writer = BibTexWriter()

    # list of sources to return
    publications = []

    # Read from a .bib file
    with open(filename, "r") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Access entries
    for bib_entry in bib_database.entries:

        print(bib_entry["ID"])

        assert "doi" in bib_entry and bib_entry['doi'] != "" and bib_entry['doi'] is not None
        doi = bib_entry['doi']
        title = bib_entry['title']
        author_list = parse_authors(bib_entry["author"])

        #publisher = bib_entry['journal'] if bib_entry['ENTRYTYPE'] == "article" else bib_entry['conference']

        publisher = ""

        if bib_entry["ENTRYTYPE"] == "inproceedings":
            publisher = bib_entry["booktitle"]
            pub_type = "conference"
        if bib_entry["ENTRYTYPE"] == "article":
            publisher = bib_entry["journal"]
            pub_type = "journal"
        else:
            pass

        for publisher_type in ["booktitle", "journal", "publisher"]:
            if publisher_type in bib_entry and bib_entry[publisher_type] != "":
                publisher = bib_entry[publisher_type]
                break

        #publisher = bib_entry['publisher']
        #date = bib_entry["date"]
        #link = bib_entry['url']
        assert "year" in bib_entry and bib_entry['year'] != ""
        year = bib_entry['year']
        if "opt_preview" in bib_entry and bib_entry['opt_preview'] != "":
            image_link = f"images/pub_thumbnails/{bib_entry['opt_preview']}"
        else:
            image_link = ""

        if "opt_html" in bib_entry and bib_entry['opt_html'] != "":
            entry_link = bib_entry['opt_html']
        else:
            entry_link = ""

        buttons = []
        buttons.append({"type": "bibtex", "link": f"doi:{doi}", "text": "Cite"}, )

        if "opt_code" in bib_entry and bib_entry['opt_code'] != "":
            buttons.append({"type": "source", "link": bib_entry["opt_code"], "text": "Code"},)
        #if "opt_html" in bib_entry and bib_entry['opt_html'] != "":
        #    buttons.append({"type": "website", "link": bib_entry['opt_html']})
        #if "opt_pdf" in bib_entry and bib_entry['opt_pdf'] != "":
        #    buttons.append({"type": "pdf", "link": bib_entry['opt_pdf']})

        tags = []
        #tags.append("preprint")

        # Do this at the end to remove the optional fields
        fields_to_remove = [k for k in bib_entry.keys() if k.startswith("opt_")]
        for field in fields_to_remove:
            bib_entry.pop(field, None)

        source = {
            "id": f"doi:{doi}",
            # api does not provide Manubot-citeable id, so keep citation details
            "title": title,
            #"type": pub_type,
            "authors": author_list,
            "publisher": publisher,
            "date": f"{year}-01-01",
            "link": entry_link,
            "image": image_link,
            "buttons": buttons,
            "tags": tags,
            "bibtex": writer._entry_to_bibtex(bib_entry).replace("\n", "<br/>"),
        }

        publications.append(source)

    return publications

publications = read_bibtex("/Users/diegopatino/Library/CloudStorage/GoogleDrive-dipaco@gmail.com/My Drive/Work/UTA/Lab admin/website/_data/bibtex.bib")

outfile = "/Users/diegopatino/Library/CloudStorage/GoogleDrive-dipaco@gmail.com/My Drive/Work/UTA/Lab admin/website/_data/citations.yaml"

with open(outfile, 'w', encoding='utf-8') as file:
    yaml.dump(publications, file, allow_unicode=True)