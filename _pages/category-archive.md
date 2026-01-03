---
title: "Category Archives"
layout: single
permalink: /category/
---

{% assign category = page.category | default: site.categories.first[0] %}

{% if site.categories[category] %}
<h1>Posts in "{{ category }}"</h1>

<ul>
{% for post in site.categories[category] %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <span class="post-meta"> - {{ post.date | date: "%B %d, %Y" }}</span>
  </li>
{% endfor %}
</ul>

{% else %}

<h1>All Categories</h1>

{% assign categories = site.categories | sort %}
{% for category in categories %}
  {% assign category_name = category[0] %}
  {% assign posts = category[1] %}
  
<h2>{{ category_name }} ({{ posts.size }} posts)</h2>
<ul>
{% for post in posts %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
    <span class="post-meta"> - {{ post.date | date: "%B %d, %Y" }}</span>
  </li>
{% endfor %}
</ul>

{% endfor %}

{% endif %}

<style>
.post-meta {
  color: #666;
  font-size: 0.9em;
}
</style>