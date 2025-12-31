---
layout: page
title: "2005 Archive"
permalink: /archive/2005/
---

# 2005 Blog Archive

This archive contains 161 posts from 2005.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2005'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
