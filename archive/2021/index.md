---
layout: single
title: "2021 Archive"
permalink: /archive/2021/
---

# 2021 Blog Archive

This archive contains 206 posts from 2021.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2021'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
