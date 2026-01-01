---
layout: single
title: "2023 Archive"
permalink: /archive/2023/
---

# 2023 Blog Archive

This archive contains 180 posts from 2023.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2023'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
