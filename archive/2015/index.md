---
layout: page
title: "2015 Archive"
permalink: /archive/2015/
---

# 2015 Blog Archive

This archive contains 342 posts from 2015.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2015'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
