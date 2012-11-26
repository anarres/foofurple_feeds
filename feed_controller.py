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

    settings_main_content = settings_main_content_foo
    settings_js = "<script type='text/javascript' src='%sjs/settings.js'></script>" % MEDIA_DIR
    index_main_content = ""

    # The main bit: the actualy feeds on each stream/page
    for s in sets_of_feeds:

        # Construct the nav
        nav_items = ""
        for sfoo in sets_of_feeds:
            if s.get_filename() == sfoo.get_filename():
                nav_items += """
                <li class='current'><a href='%s'>%s</a></li>""" % (sfoo.get_filename(), sfoo.title)
            else:
                nav_items += """
                <li><a href='%s'>%s</a></li>""" % (sfoo.get_filename(), sfoo.title)    
        nav = nav_template.render({'nav_items': nav_items})



        items_html = ""
        parsed_datums = feed_sifter.feedcache_foo(s.get_urls())
        entry_info_objects = feed_sifter.get_info(parsed_datums)
        for e in entry_info_objects:
            items_html += item_template.render( e.get_dict() )
        output_html = page_template.render({'main_content':items_html, 'title':s.title, 'nav':nav, 'settings_nav':settings_nav, 'javascript':''})

        f = open(s.get_filename(), 'w')
        f.write(output_html.encode('utf-8'))
        f.close()
        print "%s written." % s.get_filename()

        settings_main_content += stream_template.render({'stream_title':s.title, 'stream_url':s.get_filename(), 'stream_feeds':s.feeds_list})
        index_main_content += index_template.render({'stream_title':s.title, 'stream_url':s.get_filename(), 'stream_feeds':s.feeds_list})

    settings_main_content += "</div> <!--#streamGoHere-->"
    settings_main_content += "<button onclick='addStream()'>Create a new stream</button>"
    settings_main_content += "<button class='bigButton' onclick='saveAllChanges()'>SAVE ALL CHANGES</button>"
    settings_html = page_template.render({'main_content':settings_main_content, 'title':'Home', 'nav':nav, 'settings_nav':settings_nav,  'javascript':settings_js})

    index_html = page_template.render({'main_content':index_main_content, 'title':'Home', 'nav':'', 'settings_nav':settings_nav, 'javascript':''})
    appearance_js = "<script type='text/javascript' src='%sjs/appearanceSettings.js'></script>" % MEDIA_DIR
    appearance_html = page_template.render({'main_content':appearance_main_content, 'title':'Appearance', 'nav':nav, 'settings_nav':settings_nav,  'javascript':appearance_js})


    f = open('%sindex.html' % OUTPUT_DIR, 'w')
    f.write(index_html)
    f.close()

    f = open('%ssettings.html' % OUTPUT_DIR, 'w')
    f.write(settings_html)
    f.close()

    f = open('%sappearance.html' % OUTPUT_DIR, 'w')
    f.write(appearance_html)
    f.close()

