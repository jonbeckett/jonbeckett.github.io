---
layout: page
title: "2024 Archive"
permalink: /archive/2024/
---

# 2024 Blog Archive

This archive contains 144 posts from 2024.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2024'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
