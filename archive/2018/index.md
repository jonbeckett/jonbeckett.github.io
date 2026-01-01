---
layout: single
title: "2018 Archive"
permalink: /archive/2018/
---

# 2018 Blog Archive

This archive contains 312 posts from 2018.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2018'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
