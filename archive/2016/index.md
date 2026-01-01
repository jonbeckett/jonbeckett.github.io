---
layout: single
title: "2016 Archive"
permalink: /archive/2016/
---

# 2016 Blog Archive

This archive contains 403 posts from 2016.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2016'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
