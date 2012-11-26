# coding: utf-8

from jinja2 import Template
import json
import feed_sifter
from settings import *
from feed_utils import _slugify
import Tkinter
import logging
import threading
import time

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


def fetch_feeds():
    """ Put together webpages out of the feed data """

    streams = json.loads(open('streams.json','r').read())
    sets_of_feeds = []
    for s in streams:
        sets_of_feeds.append( SetOfFeeds(s['stream_name'], s['feeds']) )

    # Nav
    nav_items = ""
    for s in sets_of_feeds:
        nav_items += """

    <li><a href='%s'>%s</a></li>""" % (s.get_filename(), s.title)
    nav = nav_template.render({'nav_items': nav_items})

    # The main bit: the actualy feeds on each stream/page
    items_html = ""
    for s in sets_of_feeds:
        parsed_datums = feed_sifter.feedcache_foo(s.get_urls())
        entry_info_objects = feed_sifter.get_info(parsed_datums)
        for e in entry_info_objects:
            items_html += item_template.render( e.get_dict() )
        output_html = page_template.render({'main_content':items_html, 'title':s.title, 'nav':nav, 'javascript':''})

        f = open(s.get_filename(), 'w')
        f.write(output_html.encode('utf-8'))
        f.close()
        print "%s written." % s.get_filename()


    settings_js = "<script type='text/javascript' src='%sjs/settings.js'></script>" % MEDIA_DIR
    settings_main_content = ""
    index_main_content = ""




    for s in sets_of_feeds:
        settings_main_content += stream_template.render({'stream_title':s.title, 'stream_url':s.get_filename(), 'stream_feeds':s.feeds_list})
        index_main_content += index_template.render({'stream_title':s.title, 'stream_url':s.get_filename(), 'stream_feeds':s.feeds_list})

    settings_main_content += "</div> <!--#streamGoHere-->"

    settings_main_content += "<button onclick='addStream()'>Create a new stream</button>"
    settings_main_content += "<button class='bigButton' onclick='saveAllChanges()'>SAVE ALL CHANGES</button>"

    settings_html = page_template.render({'main_content':settings_main_content, 'title':'Home', 'nav':nav, 'javascript':settings_js})


    appearance_js = "<script type='text/javascript' src='%sjs/appearanceSettings.js'></script>" % MEDIA_DIR

    index_html = page_template.render({'main_content':index_main_content, 'title':'Home', 'nav':nav, 'javascript':''})
    appearance_html = page_template.render({'main_content':appearance_main_content, 'title':'Appearance', 'nav':nav, 'javascript':appearance_js})


    f = open('%sindex.html' % OUTPUT_DIR, 'w')
    f.write(index_html)
    f.close()


    f = open('%ssettings.html' % OUTPUT_DIR, 'w')
    f.write(settings_html)
    f.close()

    f = open('%sappearance.html' % OUTPUT_DIR, 'w')
    f.write(appearance_html)
    f.close()

