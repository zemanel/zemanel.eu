# -*- coding: utf-8 -*- #
import os

SITEDIR = os.path.abspath(os.path.dirname(__file__))

# General Settings

AUTHOR = u'Jos\xe9 Moreira'
SITENAME = u'There And Back'
SITEURL = 'http://www.zemanel.eu'
RELATIVE_URLS = True

SITEDSN = 'www.zemanel.eu'  # custom setting

FEED_DOMAIN = SITEURL
TIMEZONE = 'Europe/Lisbon'
GOOGLE_ANALYTICS = ''
DEFAULT_LANG = u'en'

# Plugins
PLUGIN_PATH = os.path.join(SITEDIR, 'vendor/pelican_plugins')

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

## content
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = os.path.join(SITEDIR, '_output')
ARTICLE_DIR = 'articles'
PAGE_DIR = 'pages'

# Social
TWITTER_USERNAME = 'zemanel'
SOCIAL = (
    ('Twitter', 'http://twitter.com/zemanel'),
    ('Github', 'http://github.com/zemanel'),
    ('Linkedin', 'http://pt.linkedin.com/in/josemoreira'),
    ('Stackoverflow', 'http://stackoverflow.com/users/2278823/zemanel'),
    ('Careers 2.0', 'http://careers.stackoverflow.com/zemanel'),

)

DEFAULT_PAGINATION = 10
