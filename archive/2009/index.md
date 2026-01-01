---
layout: single
title: "2009 Archive"
permalink: /archive/2009/
---

# 2009 Blog Archive

This archive contains 295 posts from 2009.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2009'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
