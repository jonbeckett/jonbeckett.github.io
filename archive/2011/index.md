---
layout: single
title: "2011 Archive"
permalink: /archive/2011/
---

# 2011 Blog Archive

This archive contains 535 posts from 2011.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2011'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
