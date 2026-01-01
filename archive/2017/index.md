---
layout: single
title: "2017 Archive"
permalink: /archive/2017/
---

# 2017 Blog Archive

This archive contains 369 posts from 2017.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2017'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
