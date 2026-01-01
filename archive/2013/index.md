---
layout: single
title: "2013 Archive"
permalink: /archive/2013/
---

# 2013 Blog Archive

This archive contains 210 posts from 2013.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2013'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
