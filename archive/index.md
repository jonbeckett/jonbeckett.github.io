---
layout: single
title: Blog Archive
permalink: /archive/
---

This archive contains blog posts spanning from 2003 to 2025.

## Browse by Year

{% for year in (2003..2025) reversed %}
- [{{ year }}](/categories/{{ year }}/)
{% endfor %}

---

*Current posts can be found on the [home page](/).*
