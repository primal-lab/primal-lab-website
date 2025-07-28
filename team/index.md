---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %} Team

Below, you will find detailed information about our team members at the PRIMAL Lab. Please do not hesitate to contact us regarding our work.

## Principal Investigator

{% include list.html data="members" component="portrait" filters="role == 'principal-investigator'" %}

## Students
{% include list.html data="members" component="portrait" filters="role == 'phd'" %}
{% include list.html data="members" component="portrait" filters="role == 'masters'" %}
{% include list.html data="members" component="portrait" filters="role == 'undergrad'" %}

## Alumni
{% include list.html data="members" component="portrait" filters="role=='alumni'" %}

{% include section.html background="images/background.jpg" dark=true %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

{% include section.html %}

{% capture content %}

{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}
