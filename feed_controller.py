# coding: utf-8

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
stream = Template(stream_template)

for s in sets_of_feeds:

    parsed_datums = feed_sifter.feedcache_foo(s.get_urls())
    entry_info_objects = feed_sifter.get_info(parsed_datums)
    items_html = ""
    for e in entry_info_objects:
        items_html += item.render( e.get_dict() )
    output_html = page.render({'main_content':items_html, 'title':s.title, 'nav':nav, 'javascript':''})

    f = open(s.get_filename(), 'w')
    f.write(output_html.encode('utf-8'))
    f.close()

    print "%s written." % s.get_filename()


j = "<script type='text/javascript' src='/home/katie/prog/foofurple_feeds/media/js/spaceOcto.js'></script>"

foo = """
    <div id="newFeedFoo" style="position:fixed;top:10px;left:-1000px;z-index:2;background-color: white;padding:10px;padding-top:5px;border:3px solid grey;border-radius: 5px;">
        <h3>Add a new feed:</h3>
        <p>
            Feed name:
            <input type='text' id="elephant" />
            Feed url:
            <input type='text' id="walrus" />
            <button onclick="reallyAddFeed()">Submit</button>
        </p>
    </div>


    <div id="saveAllChanges" style="width:200px;position:fixed;top:10px;left:-1000px;z-index:2;background-color: white;padding:10px;padding-top:5px;border:3px solid grey;border-radius: 5px;">
    <h3>Save all changes</h3>
    <p>To save your changes, please right-click the file below and save it as /home/katie/prog/foofurple_feeds/streams.json. 

    <p><a id="saveAllChangesLink" href="">Save all changes</a></p>

    <p>Confused? Read <a href="">why do I have to save a text file?</a></p>

    </div>

"""

for s in sets_of_feeds:
    foo += stream.render({'stream_title':s.title, 'stream_url':s.get_filename(), 'stream_feeds':s.feeds_list})

foo += "<button onclick='saveAllChanges()'>SAVE ALL CHANGES</button>"

index_html = page.render({'main_content':foo, 'title':'Streams and feeds', 'nav':nav, 'javascript':j})
f = open('/home/katie/prog/foofurple_feeds/output/index.html', 'w')
f.write(index_html)
f.close()



