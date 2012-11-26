#!/usr/bin/env python

from jinja2 import Template

BASE_DIR = "/home/katie/prog/foofurple_feeds/"
OUTPUT_DIR = "/home/katie/prog/foofurple_feeds/output/"
MEDIA_DIR = "/home/katie/prog/foofurple_feeds/media/"
TEMPLATES_DIR = "/home/katie/prog/foofurple_feeds/templates/"

nav_template = Template( open('%snav' % TEMPLATES_DIR,'r').read() )
item_template = Template( open('%sitem' % TEMPLATES_DIR,'r').read() )
page_template = Template( open('%spage' % TEMPLATES_DIR,'r').read() )
list_template = Template( open('%slist' % TEMPLATES_DIR,'r').read() )
stream_template = Template( open('%sstream' % TEMPLATES_DIR,'r').read() )
index_template = Template( open('%sindex' % TEMPLATES_DIR,'r').read() )
settings_main_content_template = Template( open('%ssettings_main_content' % TEMPLATES_DIR,'r').read() )

appearance_main_content = open('%sappearance_main_content' % TEMPLATES_DIR,'r').read()

