Title: Auto-posting static site updates from GitHub to Twitter with Zapier
Date: 2013-04-20 21:00
Tags: API, Github, Zapier, automation
Slug: auto-post-static-site-updates-from-github-to-twitter-with-zapier
Summary: Just created a new zap for auto-posting to Twitter when i commit website updates to GitHub <https://Zapier.com> ![select services](/static/images/2013/04/20/zapier-github-to-twitter-000.png)

Quickly created a new zap for auto-posting to Twitter when i commit website updates to GitHub <https://Zapier.com>.

![select services](/static/images/2013/04/20/zapier-github-to-twitter-000.png)

### Rundown

Selected this website's repo and branch (<https://github.com/zemanel/zemanel.eu/tree/master/>)

![twitter zap screenshot 001](/static/images/2013/04/20/zapier-github-to-twitter-001.png)

and chose a simple and short tweet message. Too bad Twitter is url shortening my site's <http://zemanel.eu> URL, it's already short!

![twitter zap screenshot 002](/static/images/2013/04/20/zapier-github-to-twitter-002.png)

Loaded some sample data and tested it out

![twitter zap screenshot 003](/static/images/2013/04/20/zapier-github-to-twitter-003.png)

and it's [alive and kicking](http://www.youtube.com/watch?v=ljIQo1OHkTI) !

### And this is it, basically

> Yo! Just updated my site http://t.co/73vWqUZjKw
> 
> "update general anchor CSS"
> 
> (via @zapier)

For it to be perfect, just have to improve the commit messages, since **release 0.5.14** is not that meaningful on Twitter :-)

The generated content is actually being served from the *gh-pages* branch, as i'm using the `ghp-import` tool which allows a commit message to be specific.

Currently just using the defaults, so an improvement point is to specify that commit message manually, for example:

    :::console
    $ ghp-import -m "New blog post about chunky bacon!" ./_output/

and use the 'gh-pages' branch as source.

That is all.
