---
layout: single
title: "2010 Archive"
permalink: /archive/2010/
---

# 2010 Blog Archive

This archive contains 416 posts from 2010.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2010'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
