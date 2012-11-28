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
settings_main_content_foo = open('%ssettings_main_content' % TEMPLATES_DIR,'r').read()
appearance_main_content = open('%sappearance_main_content' % TEMPLATES_DIR,'r').read()

MAX_THREADS=5
STORAGE_DIR='/home/katie/prog/foofurple_feeds/tmp/feedcache_example'
image1 = "%simages/message1.gif" % MEDIA_DIR
image2 = "%simages/message2.gif" % MEDIA_DIR
image3 = "%simages/message3.gif" % MEDIA_DIR

settings_nav = """
<ul>

    <li><a href='index.html'>Home</a></li>
    <li><a href='settings.html'>Set-up</a></li>
    <li><a href='appearance.html'>Appearance</a></li>

</ul>
"""

settings_nav_index = """
<ul>

    <li class='current'><a href='index.html'>Home</a></li>
    <li><a href='settings.html'>Set-up</a></li>
    <li><a href='appearance.html'>Appearance</a></li>

</ul>
"""

settings_nav_settings = """
<ul>

    <li><a href='index.html'>Home</a></li>
    <li class='current'><a href='settings.html'>Set-up</a></li>
    <li><a href='appearance.html'>Appearance</a></li>

</ul>
"""

settings_nav_appearance = """
<ul>

    <li><a href='index.html'>Home</a></li>
    <li><a href='settings.html'>Set-up</a></li>
    <li class='current'><a href='appearance.html'>Appearance</a></li>

</ul>
"""


