#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ITS'
SITENAME = u'SimonsRockPelican'
SITEURL = ''
FAVICON = '/home/ubuntu/favicon.ico'
THEME = 'pelican-bootstrap3'
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['testgen']
PATH = 'content'
READERS = {'html': None}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Database vars

DATABASESERVER = 'srcdb1.camvfsq3weo1.us-west-2.rds.amazonaws.com'
DATABASEUSER = 'its'
DATABASEPASS = 'newYear!'
DATABASENAME = 'Pelican'


LOAD_CONTENT_CACHE = False
DISPLAY_PAGES_ON_MENU = False
