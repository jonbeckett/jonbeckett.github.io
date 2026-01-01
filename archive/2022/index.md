---
layout: single
title: "2022 Archive"
permalink: /archive/2022/
---

# 2022 Blog Archive

This archive contains 189 posts from 2022.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2022'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
