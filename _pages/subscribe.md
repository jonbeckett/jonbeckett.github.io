---
layout: single
title: Subscribe
permalink: /subscribe/
---

I use **follow.it** to send email updates to subscribers, because it provides more than just a standard newsletter. While ensuring you never miss a post, it gives you total control over your inbox.

When you subscribe, you’ll be able to:

* **Choose your frequency** - get an email the moment a post goes live, or bundle them into a single daily digest.
* **Filter your feed** -  if you’re only interested in specific categories, you can set filters so you only receive what matters to you.
* **Pick your platform** - while you're signing up for email now, **follow.it** also allows you to move your subscription to RSS, Telegram, or other news readers later if you prefer.

<style>
.email-subscribe-form {
  max-width: 400px;
  margin: 2em auto;
  padding: 1.5em;
  background: var(--background-color, #fff);
  border: 1px solid var(--border-color, #f2f3f3);
  border-radius: 4px;
}

.email-subscribe-form h3 {
  margin-top: 0;
  margin-bottom: 1em;
  text-align: center;
  font-size: 1.1em;
}

.email-subscribe-form input[type="email"] {
  width: 100%;
  padding: 0.75em;
  margin-bottom: 1em;
  border: 1px solid var(--border-color, #f2f3f3);
  border-radius: 4px;
  font-size: 1em;
  box-sizing: border-box;
}

.email-subscribe-form input[type="email"]:focus {
  outline: none;
  border-color: var(--link-color, #52adc8);
}

.email-subscribe-form button {
  width: 100%;
  padding: 0.75em;
  background: var(--link-color, #52adc8);
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1em;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

.email-subscribe-form button:hover {
  background: var(--link-color-hover, #216c7a);
}

.powered-by {
  text-align: center;
  margin-top: 1em;
  font-size: 0.8em;
  color: var(--muted-text-color, #999);
}

.powered-by a {
  color: inherit;
  text-decoration: none;
}

.powered-by img {
  vertical-align: middle;
  margin-left: 0.5em;
  height: 1em;
}
</style>

<div class="email-subscribe-form">

  <form action="https://api.follow.it/subscription-form/MlpoeTdDYmxiZ1VwelNhL3ZLbU1iZ1F0cjZteHNWSk00NmJNMGVxOU1LMWJkSkZackdna2R5WFFoRXZ6QkhNMzhkOHFUbFlXdVdhMmNRbjdxeVlGYlplSTNmWGNHYWxXenZTL2l4SHdVUTJ2TWgwSE5WczZJdFNDSWRqak1TbWF8bEtiS1VWODZzSDVmM1g2NXNEOW5kbVNWNmlmb0VBb0Rqa2VCUEg2QTJmcz0=/8" method="post">
    <h3>Subscribe for email updates</h3>
    <input type="email" name="email" placeholder="Enter your email address" required>
    <button type="submit">Subscribe</button>
  </form>
  
  <div class="powered-by">
    <a href="https://follow.it">Powered by <img src="https://follow.it/images/colored-logo.svg" alt="follow.it"></a>
  </div>
</div>