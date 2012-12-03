#!/usr/bin/env python
# coding: utf-8

from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment
import feed_sifter
import logging

from settings import *
from feed_utils import _slugify

env = Environment()
env.loader = FileSystemLoader('%stemplates/' % BASE_DIR)


def make_all_the_webpages(streams):

    # Write the about page
    tmpl = env.get_template('about.html')
    f = open('%sabout.html' % OUTPUT_DIR, 'w')
    f.write(tmpl.render({'title':'About','streams':streams,'GLOBS':GLOBS}))
    f.close()

    # Write the appearance page
    tmpl = env.get_template('appearance.html')
    f = open('%sappearance.html' % OUTPUT_DIR, 'w')
    f.write(tmpl.render({'title':'Appearance','streams':streams,'GLOBS':GLOBS}))
    f.close()

    # Write the index page
    tmpl = env.get_template('index.html')
    f = open('%sindex.html' % OUTPUT_DIR, 'w')
    f.write(tmpl.render({'title':'About','streams':streams,'GLOBS':GLOBS}))
    f.close()

    # Write the settings page
    tmpl = env.get_template('settings.html')
    f = open('%ssettings.html' % OUTPUT_DIR, 'w')
    f.write(tmpl.render({'title':'Settings','streams':streams,'GLOBS':GLOBS}))
    f.close()

    # Write the stream pages 
    for s in streams:

        tmpl = env.get_template('stream.html')
        f = open(s.filepath, 'w')
        foo = tmpl.render({'stream':s,'streams':streams,'GLOBS':GLOBS})
        bar = foo.encode("utf-8")
        f.write(bar)
        f.close()


