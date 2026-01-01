---
layout: single
title: "2012 Archive"
permalink: /archive/2012/
---

# 2012 Blog Archive

This archive contains 242 posts from 2012.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2012'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
