#!/usr/bin/env python

from jinja2 import Template

BASE_DIR = "/home/katie/prog/foofurple_feeds/"
OUTPUT_DIR = "/home/katie/prog/foofurple_feeds/output/"
MEDIA_DIR = "/home/katie/prog/foofurple_feeds/media/"
TEMPLATES_DIR = "/home/katie/prog/foofurple_feeds/templates/"
STORAGE_DIR='/home/katie/prog/foofurple_feeds/tmp/feedcache_example'

GLOBS = {'BASE_DIR':BASE_DIR,'OUTPUT_DIR':OUTPUT_DIR,'MEDIA_DIR':MEDIA_DIR,
    'TEMPLATES_DIR':TEMPLATES_DIR,'STORAGE_DIR':STORAGE_DIR}


item_template = Template( open('%sitem' % TEMPLATES_DIR,'r').read() )
page_template = Template( open('%spage' % TEMPLATES_DIR,'r').read() )
list_template = Template( open('%slist' % TEMPLATES_DIR,'r').read() )
stream_template = Template( open('%sstream' % TEMPLATES_DIR,'r').read() )
index_template = Template( open('%sindex' % TEMPLATES_DIR,'r').read() )
appearance_main_content = open('%sappearance_main_content' % TEMPLATES_DIR,'r').read()




