#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ITS'
SITENAME = u'SimonsRockPelican'
SITEURL = ''
FAVICON = '/home/ubuntu/favicon.ico'
THEME = 'pelican-bootstrap3'
PLUGIN_PATHS = ['./plugins']
PLUGINS = []
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

LOAD_CONTENT_CACHE = False
DISPLAY_PAGES_ON_MENU = False
