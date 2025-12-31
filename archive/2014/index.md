---
layout: page
title: "2014 Archive"
permalink: /archive/2014/
---

# 2014 Blog Archive

This archive contains 254 posts from 2014.

{% assign year_posts = site.pages | where: "categories", "archive" | where_exp: "post", "post.date contains '2014'" | sort: "date" | reverse %}

{% for post in year_posts %}
- {{ post.date | date: "%b %-d" }} - [{{ post.title }}]({{ post.url }})
{% endfor %}

---

[← Back to Archive](/archive/)
