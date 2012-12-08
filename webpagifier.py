#!/usr/bin/env python
# coding: utf-8

from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment
import logging
import datetime

from settings import BASE_DIR, OUTPUT_DIR, GLOBS
import feed_sifter
from utils import nice_now

env = Environment()
env.loader = FileSystemLoader('%stemplates/' % BASE_DIR)

def date_msg():
    now = nice_now()
    msg = "Feeds last updated on %s." % now
    return msg

def make_wait_page():
    tmpl = env.get_template('wait.html')
    f = open('%swait.html' % OUTPUT_DIR, 'w')
    f.write(tmpl.render({'GLOBS':GLOBS}))
    f.close()


def make_all_the_webpages(streams):

    # Write the style.css
    tmpl = env.get_template('style.css')
    f = open('%sstyle.css' % OUTPUT_DIR, 'w')
    f.write(tmpl.render({'GLOBS':GLOBS}))
    f.close()

    footer = date_msg()

    # Write the index page
    tmpl = env.get_template('index.html')
    f = open('%sindex.html' % OUTPUT_DIR, 'w')
    f.write(tmpl.render({'title':'About','streams':streams,'GLOBS':GLOBS,'footer':footer}))
    f.close()

    # Write the settings page
    tmpl = env.get_template('settings.html')
    f = open('%ssettings.html' % OUTPUT_DIR, 'w')
    f.write(tmpl.render({'title':'Settings','streams':streams,'GLOBS':GLOBS,'footer':footer}))
    f.close()

    # Write the stream pages 
    for s in streams:
        tmpl = env.get_template('stream.html')
        f = open(s.filepath, 'w')
        foo = tmpl.render({'stream':s,'streams':streams,'GLOBS':GLOBS,'footer':footer})
        bar = foo.encode("utf-8")
        f.write(bar)
        f.close()


