---
layout: page
title: "2019 Archive"
permalink: /archive/2019/
---

# 2019 Blog Archive

This archive contains 282 posts from 2019.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2019'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
