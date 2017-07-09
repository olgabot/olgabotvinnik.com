---
title: "Migrate To Hugo"
date: 2017-07-09T17:25:59-04:00
draft: false
---

My landing page website was originally hosted on flavors.me but that got shut
down and all my web presence was broken for a few weeks (!!).

I got tired of dealing with Github Pages and building via Travis-CI. Today I
migrated to
[Hugo](https://gohugo.io) and deploy the website using
[Netlify](https://www.netlify.com).

I chose Hugo because it has nice minimal themes and was reasonably easy to set
up and deploy. I had some issues with using custom themes and ended up just
copying the folder to my directory rather than dealing with submodules which
were a major headache.


I've found myself avoiding blogging because I didn't like my blog layout, how
much overhead there was for creating a new pelican page (now I do `hugo new
blog/migrate-to-hugo.md` and that creates the new post with the correct date,
and default `draft: true`) and website so I'm hoping that an easier deploy
process will encourage me to blog more.