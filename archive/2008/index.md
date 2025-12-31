---
layout: page
title: "2008 Archive"
permalink: /archive/2008/
---

# 2008 Blog Archive

This archive contains 355 posts from 2008.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2008'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
