#!/usr/bin/env python

OUTPUT_DIR = "/home/katie/prog/foofurple_feeds/output/"
MEDIA_DIR = "/home/katie/prog/foofurple_feeds/media/"
TEMPLATES_DIR = "/home/katie/prog/foofurple_feeds/templates/"

item_template = open('%sitem' % TEMPLATES_DIR,'r').read()
page_template = open('%spage' % TEMPLATES_DIR,'r').read()
list_template = open('%slist' % TEMPLATES_DIR,'r').read()
stream_template = open('%sstream' % TEMPLATES_DIR,'r').read()

