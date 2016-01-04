#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Charles'
AUTHORS = u'Charles'
SITENAME = u'foxbat'
SITEURL = 'blog.hunterkiller.info'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

DISQUS_SITENAME = 'bloghunterkillerinfo'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/profile/view?id=175630680'),
          ('Stackoverflow', 'http://stackoverflow.com/users/647129/mig-foxbat'),
          ('Facebook','https://www.facebook.com/waffenss1945'),
          ('Google+','https://plus.google.com/+Charlesvinodh'))

DEFAULT_PAGINATION = 10

THEME = "pelican-themes/fresh"

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


