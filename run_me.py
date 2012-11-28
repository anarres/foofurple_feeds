#!/usr/bin/env python

# Import system modules
import Queue
import sys
import shelve
import threading
import json
from Tkinter import *
from PIL import ImageTk, Image
import webbrowser

# Import local modules
import cache
from settings import *
from feed_sifter import SetOfFeeds

#
streams = json.loads(open('streams.json','r').read())
sets_of_feeds = []
for s in streams:
    sets_of_feeds.append( SetOfFeeds(s['stream_name'], s['feeds']) )
urls = []
for s in sets_of_feeds:
    urls += s.get_urls()

def get_parsed_data(urls=[]):

    webbrowser.open('file:///home/katie/prog/foofurple_feeds/wait.html')
    parsed_datums = []

    print 'Saving feed data to ./.feedcache'
    storage = shelve.open('.feedcache')
    try:
        fc = cache.Cache(storage)
        for url in urls:
            parsed_data = fc.fetch(url)
            for entry in parsed_data.entries:
                parsed_datums.append({'url':url,'feed':parsed_data.feed,'entry':entry})
    finally:
        storage.close()
    return parsed_datums

get_parsed_data(urls)

