import bibtexparser

def main(entry):

    # list of sources to return
    sources = []

    # Read from a .bib file
    import pdb
    pdb.set_trace()
    with open("bibtex.bib", "r") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Access entries
    for bib_entry in bib_database.entries:

        source = {
            "id": get_safe(work, "citation_id", ""),
            # api does not provide Manubot-citeable id, so keep citation details
            "title": get_safe(work, "title", ""),
            "authors": list(map(str.strip, get_safe(work, "authors", "").split(","))),
            "publisher": get_safe(work, "publication", ""),
            "date": (year + "-01-01") if year else "",
            "link": get_safe(work, "link", ""),
        }

        # copy fields from entry to source
        source.update(entry)

        # add source to list
        sources.append(source)

        print(entry['ID'], entry['title'])

    return sources