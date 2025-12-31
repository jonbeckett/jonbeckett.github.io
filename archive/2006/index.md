---
layout: page
title: "2006 Archive"
permalink: /archive/2006/
---

# 2006 Blog Archive

This archive contains 299 posts from 2006.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2006'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
