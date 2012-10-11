#!/usr/bin/env python

from jinja2 import Template
import json
import feed_sifter
from settings import *
from feed_utils import _slugify

class SetOfFeeds(object):
    """ A 'stream' or set of feeds grouped together """

    def __init__(self, title, feeds_list):
        self.title = title
        self.feeds_list = feeds_list

    def __str__(self):
        return "SetOfFeeds object with title: %s" % self.title

    def get_urls(self):
        urls = []
        for f in self.feeds_list:
            urls.append(f['url'])
        return urls

    def get_filename(self):
        return "%s%s.html" % (OUTPUT_DIR, _slugify(self.title))


streams = json.loads(open('streams.json','r').read())
sets_of_feeds = []
for s in streams:
    sets_of_feeds.append( SetOfFeeds(s['stream_name'], s['feeds']) )


nav_template = """<ul><li><a href='/home/katie/prog/foofurple_feeds/output/index.html'>Home</a></li>%s</ul>"""
html = ""
for s in sets_of_feeds:
    html += """<li><a href='%s'>%s</a></li>""" % (s.get_filename(), s.title)

nav = nav_template % html

item = Template(item_template)
page = Template(page_template)
#t3 = Template(list_template)
stream = Template(stream_template)

for s in sets_of_feeds:

    parsed_datums = feed_sifter.feedcache_foo(s.get_urls())
    entry_info_objects = feed_sifter.get_info(parsed_datums)
    items_html = ""
    for e in entry_info_objects:
        items_html += item.render( e.get_dict() )
    output_html = page.render({'main_content':items_html, 'title':s.title, 'nav':nav})

    f = open(s.get_filename(), 'w')
    f.write(output_html)
    f.close()

    print "%s written." % s.get_filename()


# Create index page
foo = "<p>Feeds can be grouped together in streams</p>"
for s in sets_of_feeds:

    foo += stream.render({'stream_title':s.title, 'stream_url':s.get_filename(), 'stream_feeds':s.feeds_list})

index_html = page.render({'main_content':foo, 'title':'Setup: streams and feeds', 'nav':nav})
f = open('/home/katie/prog/foofurple_feeds/output/index.html', 'w')
f.write(index_html)
f.close()



