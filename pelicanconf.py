# -*- coding: utf-8 -*- #
import os

SITEDIR = os.path.abspath(os.path.dirname(__file__))
# General Settings

AUTHOR = u'Jos\xe9 Moreira'
SITENAME = u'There And Back'
SITEURL = 'http://zemanel.eu'

RELATIVE_URLS = False
GOOGLE_ANALYTICS = 'UA-26838427-1'
FEED_DOMAIN = SITEURL
TIMEZONE = 'Europe/Lisbon'
DEFAULT_LANG = u'en'

# Plugins
PLUGIN_PATHS = (
    os.path.join(SITEDIR, 'vendor/pelican_plugins'),
)

PLUGINS = [
    'sitemap',
    #'w3c_validate',
    'assets',
]

# Sitemap plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

#assets plugin
_LESSC = '%s/node_modules/.bin/lessc' % SITEDIR
ASSET_CONFIG = (
    ('less_bin', _LESSC)
)

## Appearence
THEME = os.path.join(SITEDIR, 'theme/zen')
THEME = './theme/zen'

## content
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = os.path.join(SITEDIR, '_output')
ARTICLE_PATHS = (
    'articles',
)
PAGE_PATHS = (
    'pages',
)
DIRECT_TEMPLATES = (
    ('index', 'tags', 'categories', 'archives', '404')
)
STATIC_PATHS = [
    'static',
    'CNAME',
    'favicon.ico',
]

# Social
TWITTER_USERNAME = 'zemanel'
DISQUS_SITENAME = 'zemaneleu'
SOCIAL = (
    ('Twitter', 'http://twitter.com/zemanel'),
    ('Github', 'http://github.com/zemanel'),
    ('Bitbucket', 'http://bitbucket.org/zemanel'),
    ('Careers 2.0', 'http://careers.stackoverflow.com/zemanel'),
    ('Linkedin', 'http://pt.linkedin.com/in/josemoreira'),
    ('StackOverflow', 'http://stackoverflow.com/users/2278823/zemanel'),
    ('Last.fm', 'http://www.last.fm/user/jose.moreira'),
    ('Facebook', 'http://facebook.com/OVerdadeiroJoseMoreira'),
)
BLOG_ROLL = (
    ('GetPelican', 'http://blog.getpelican.com'),
)
DEFAULT_PAGINATION = 20
