# -*- coding: utf-8 -*- #
import os

SITEDIR = os.path.realpath(os.path.dirname(__file__))

# General Settings

AUTHOR = u'Jos\xe9 Moreira'
SITENAME = u'There And Back'
SITEURL = 'http://www.zemanel.eu'
RELATIVE_URLS = True

SITEDSN = 'www.zemanel.eu' # custom setting

FEED_DOMAIN = SITEURL
TIMEZONE = 'Europe/Lisbon'
GOOGLE_ANALYTICS = ''
DEFAULT_LANG = u'en'

# Plugins
PLUGIN_PATH = SITEDIR.join('vendor/pelican_plugins')
PLUGINS = [
    'pelican.plugins.sitemap',
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

## Appearence
THEME = os.path.join(SITEDIR, 'theme/zen')

## content
#DELETE_OUTPUT_DIRECTORY = False
OUTPUT_PATH = '_output'
ARTICLE_DIR = 'articles'
PAGE_DIR = 'pages'
FILES_TO_COPY = [
    (os.path.join(SITEDIR, 'vendor/bootstrap/img/glyphicons-halflings.png'), 'img/glyphicons-halflings.png'),
    (os.path.join(SITEDIR, 'vendor/bootstrap/img/glyphicons-halflings-white.png'), 'img/glyphicons-halflings-white.png'),
]

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
