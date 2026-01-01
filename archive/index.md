---
layout: single
title: Blog Archive
permalink: /archive/
---

Welcome to the archive of everything I've written (and managed not to lose) since 2003. The blog actually existed since at least 2001 - one day I'll go on a trawling expedition through old ZIP disks (yes, I kept my old ZIP drive) to see if I can find any of it.

Click on a year:

{% for year in (2003..2025) reversed %}
- [{{ year }}](/categories/{{ year }}/)
{% endfor %}

---

*Current posts can be found on the [home page](/).*
