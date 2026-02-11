---
title: Team
nav:
  order: 3
  tooltip: About our team
---
{% include figure.html image="images/site_style/group-picture.png" width="90%" %}
Meet our awesome team at the PRIMAL Lab. Below, you will find detailed information about our team members, their roles, and the research interest. Please do not hesitate to contact us regarding our work.

# {% include icon.html icon="fa-solid fa-microscope" %} Principal Investigator
{% include list.html data="members" component="portrait" filters="role == 'principal-investigator'" %}

# {% include icon.html icon="fa-solid fa-users" %} Current Members
{% include list.html data="members" component="portrait" filters="role == 'phd'" %}
{% include list.html data="members" component="portrait" filters="role == 'masters'" %}
{% include list.html data="members" component="portrait" filters="role == 'undergrad'" %}

# {% include icon.html icon="fa-solid fa-users" %} Alumni
{% include list.html data="members" component="portrait" filters="role=='alumni'" style="small" %}

{% include section.html background="images/background.jpg" dark=false %}

**Prospective students:** If you are a current student at UT Arlington then please fill out this form. Otherwise, please apply directly to the PhD program and mention my name in your application. 

{% include section.html %}

## Gallery

{% capture content %}

{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
