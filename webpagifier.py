# coding: utf-8

from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment
import logging
import datetime
import os

from settings import BASE_DIR, OUTPUT_DIR, TEMPLATES_DIR, GLOBS
import feed_sifter
from utils import nice_now

env = Environment()
env.loader = FileSystemLoader(TEMPLATES_DIR)

def date_msg():
    now = nice_now()
    msg = "Feeds last updated on %s." % now
    return msg

def make_wait_page():
    tmpl = env.get_template('wait.html')
    path = os.path.join(OUTPUT_DIR, "wait.html")
    f = open(path, 'w')
    f.write(tmpl.render({'GLOBS':GLOBS}))
    f.close()


def make_all_the_webpages(streams):

    # Write the style.css
    tmpl = env.get_template('style.css')
    path = os.path.join(OUTPUT_DIR, "style.css")
    f = open(path, 'w')
    f.write(tmpl.render({'GLOBS':GLOBS}))
    f.close()

    footer = date_msg()

    # Write the index page
    tmpl = env.get_template('index.html')
    path = os.path.join(OUTPUT_DIR, "index.html")
    f = open(path, 'w')
    f.write(tmpl.render({'title':'About','streams':streams,'GLOBS':GLOBS,'footer':footer}))
    f.close()

    # Write the settings page
    tmpl = env.get_template('settings.html')
    path = os.path.join(OUTPUT_DIR, "settings.html")
    f = open(path, 'w')
    f.write(tmpl.render({'title':'Settings','GLOBS':GLOBS,'footer':footer}))
    f.close()

    # Write the about page
    tmpl = env.get_template('about.html')
    path = os.path.join(OUTPUT_DIR, "about.html")
    f = open(path, 'w')
    f.write(tmpl.render({'title':'About','GLOBS':GLOBS,'footer':footer}))
    f.close()

    # Write the stream pages 
    for s in streams:
        tmpl = env.get_template('stream.html')
        f = open(s.filepath, 'w')
        foo = tmpl.render({'stream':s,'streams':streams,'GLOBS':GLOBS,'footer':footer})
        bar = foo.encode("utf-8")
        f.write(bar)
        f.close()


