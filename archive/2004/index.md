---
layout: single
title: "2004 Archive"
permalink: /archive/2004/
---

# 2004 Blog Archive

This archive contains 106 posts from 2004.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2004'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
