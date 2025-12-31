---
layout: page
title: "2020 Archive"
permalink: /archive/2020/
---

# 2020 Blog Archive

This archive contains 261 posts from 2020.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2020'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
