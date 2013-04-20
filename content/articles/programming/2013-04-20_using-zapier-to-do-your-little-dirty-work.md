Title: Using Zapier.com to do your dirty little work on the Web
Date: 2013-04-20 02:00
Tags: API, RSS, Twitter, Zapier, automation
Slug: using-zapier-to-do-your-little-dirty-work
Summary: A simple example of how <https://Zapier.com> can make my life better ![select services](/static/images/2013/04/20/zapier-create-new-zap-rss-summary.png)

### Zapier and me

Having read some web buzz about regarding Zapier in the past, only payed attention to it until just recently, when i was contacted by <https://www.paymill.com/en-gb/> to help them add their [REST API](https://www.paymill.com/en-gb/documentation-3/reference/api-reference/) as a [Zapier Service](https://zapier.com/developer/reference/#appsummary), since i am a freelancer, **still on a quest to get more work ;-)**

By the way that Service, only for new [*Transaction Successes*](https://www.paymill.com/en-gb/documentation-3/reference/api-reference/#transaction-object) Web Hook [**event**](https://www.paymill.com/en-gb/documentation-3/reference/api-reference/#events) at the moment, is well underway and currently going through the Zapier approval process, which will probably be the topic of another post when it's publicly available.

What brings us here to this post, is exactly this blog, since i am still trying to replace Posterous.com's auto-post feature. For now, i've created a Zap to auto-post to my Twitter account when new posts are available on my [RSS feed](/feeds/all.atom.xml), because that's how Zapier rolls, data sources can either be REST API's or regular Atom/RSS feeds.

Within a Service, **Triggers** poll data from a data source using [*Poling*](https://zapier.com/developer/reference/#polling), either on interval or Web Hooks. **Actions** react to new data items and can perform things related to what the containing Service means to fulfill. For example on the Twitter [Zapier] service, for sure there is an action that receives a body and posts that as a tweet to an account. Connecting my RSS feed to my Twitter account was super easy.

### Let's roll

On my account's Dashboard <https://zapier.com/app/dashboard> i created a new Zap:

![create new zap](/static/images/2013/04/20/zapier-create-new-zap.png)

On **step #1** of the form, selected which *Service*s i would like to connect and their correspondent actions, in this case the RSS Service and Twitter.

![select services](/static/images/2013/04/20/zapier-create-new-zap-select-services.png)

On **step #2**, there is no [user authentication] account setup required, since i am merely going to use the static RSS URL 

![select rss account](/static/images/2013/04/20/zapier-create-new-zap-rss-account.png)

so i move on to **step #3** and connect my Twitter account.

Since i don't have my account already associated on my Zapier account yet, as it keeps track of associated user accounts allowing me to re-use the credentials between zaps, i connect a new one. After going through the Twitter OAuth work-flow, it is good to go:

![associate Twitter account](/static/images/2013/04/20/zapier-create-new-zap-twitter-account.png)

Configuration of the source RSS URL goes on **step #4**

![configure RSS URL](/static/images/2013/04/20/zapier-create-new-zap-rss-configure.png)


and on **step #5** i set the template for the tweet based on **sample values from the RSS entry**! Notice how i can preview the result, due to Zapier using sample entries from the feed itself:

![fill tweet template](/static/images/2013/04/20/zapier-create-new-zap-tweet-tpl.png)

**Step #6** is [The Test](http://www.youtube.com/watch?v=yhS9LnDoo_w). Since i've already posted those entries, let's skip it but you get the point. Clicking **Send!** executes the corresponding Twitter's action and tweets it.

![test the zap](/static/images/2013/04/20/zapier-create-new-zap-rss-test.png)

By the way, did you notice that **The Test** was a link for one amazing Chemical Brother video ? You should check it out.

Wrapping it up, on **step #7**, we can name out zap

![make zap live](/static/images/2013/04/20/zapier-create-new-zap-make-live.png)

and click "Make Zap Live". What happens then is that, from that point, the zap becomes active. From the <https://zapier.com/app/dashboard>:

![live zap on the dashboard](/static/images/2013/04/20/zapier-create-new-zap-live.png)

Zapier polls for new items every X minutes and when new entries are detected on the RSS, entry data is passed to the Twitter Service Action, which then tweets it after applying the template text we chose. We also have access to the zap's activity history

![zap activity history](/static/images/2013/04/20/zapier-create-new-zap-rss-history.png)

### To what it all comes down to

Is this

![end result](/static/images/2013/04/20/zapier-create-new-zap-rss-end-result.png)

every time i post something new and my RSS feed is updated, after a few minutes Zapier jumps into action and posts it for me.

Although i've only scratched the surface, since this was a pretty simple example, and posting to Facebook and Google Plus isn't yet possible (it's possible to post to Facebook Pages but not user wall's it seems), i think they have something good going here and i'm not short of ideas on how to use this, even creating new services ([OpenShift](https://www.openshift.com) i'm looking at you).

### That is [almost] all

If you got excited and want to try out Zapier, feel free to sign up through my <https://zapier.com/r/iAEC/> referral link and get some bonuses together, shall we ? We can get **+100** tasks per referral, up to **+500** ;-)

