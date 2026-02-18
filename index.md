---
layout: default
title: Home
---


{% include section.html %}

# Welcome to the PRIMAL Lab

{% capture text %}
[mission statement] Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
{% endcapture %}

{{ text }}

<!-- Sideways scrolling photos (structure only; style later) -->
<div class="photo-scroll">
  <div class="photo-scroll__track">
    <img src="images/photo.jpg" alt="PRIMAL Lab photo 1" />
    <img src="images/photo.jpg" alt="PRIMAL Lab photo 2" />
    <img src="images/photo.jpg" alt="PRIMAL Lab photo 3" />
    <img src="images/photo.jpg" alt="PRIMAL Lab photo 4" />
    <img src="images/photo.jpg" alt="PRIMAL Lab photo 5" />
    <img src="images/photo.jpg" alt="PRIMAL Lab photo 6" />
    <img src="images/photo.jpg" alt="PRIMAL Lab photo 7" />
    <img src="images/photo.jpg" alt="PRIMAL Lab photo 8" />
  </div>
</div>

---

{% include section.html %}

{% capture text %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

{%
  include button.html
  link="projects"
  text="Explore our projects"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="projects"
  title="Current Projects"
  text=text
%}

---

{% include section.html %}

{% capture text %}
Our lab is built on collaboration, curiosity, and mentorship. We are a diverse group of researchers and students working together to advance applied AI and autonomous learning systems, fostering an environment where rigorous research meets creative exploration.

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="team"
  title="Meet Our Team"
  flip=true
  style="bare"
  text=text
%}

---

{% include section.html %}

## News

<!-- Structure-first: replace with a loop later if your site has posts -->
- News item placeholder 1
- News item placeholder 2 

{%
  include button.html
  link="blog"
  text="View all news"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

---

{% include section.html %}

## Sponsors

Our work is made possible by funding from several organizations.

<!-- Placeholder sponsor row -->
<div class="sponsors">
  <img src="images/photo.jpg" alt="Sponsor logo 1" />
  <img src="images/photo.jpg" alt="Sponsor logo 2" />
  <img src="images/photo.jpg" alt="Sponsor logo 3" />
</div>
