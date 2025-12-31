---
layout: page
title: Blog Archive
permalink: /archive/
---

# Blog Archive

This archive contains {{ site.pages | where: "categories", "archive" | size }} blog posts spanning from 2003 to 2024.

## Browse by Year

{% for year in (2003..2024) reversed %}
  {% capture year_string %}{{ year }}{% endcapture %}
  {% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains year_string" %}
  {% if year_posts.size > 0 %}
- [{{ year }}]({{ year_string }}/) - {{ year_posts.size }} posts
  {% endif %}
{% endfor %}

---

*Current posts can be found on the [home page](/).*