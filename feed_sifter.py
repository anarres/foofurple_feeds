#!/usr/bin/env python
# coding: utf-8
#
# feed_sifter.py
# takes data from feedparser/feedcache and repackages it 
# so as to be displays in 'streams' or sets of feeds.
#
#
#

import shelve
import time

import cache
from settings import *

#
# CLASSES TO HOLD THE REPACKAGED DATA
#
class FeedInfo(object):
    """ Represents an RSS or Atom feed """

    def __init__(self, link, title, logo):
        self.link = link
        self.title = title
        self.logo = logo     
    def __str__(self):
        return "FeedInfo object: title: %s, link: %s, logo: %s." % (self.title, self.link, self.logo)


class StreamItem(object):
    """ Contains all the data needed to display one item / post / tweet in a stream """

    def __init__(self, feed_obj, link, title, author, description, content, date, images, audio, video):
        self.feed_obj = feed_obj
        self.link = link
        self.title = title
        self.author = author
        self.description = description
        self.content = content
        self.date = date
        self.nice_date = time.strftime("%a, %d %b %Y", date)
        self.images = images               # A list of urls
        self.audio = audio                 # A list of urls
        self.video = video                 # A list of urls

    def __str__(self):
        return "StreamItem object, title: %s." % self.title



class Stream(object):
    """ A 'stream' or set of feeds whose feed items are to be displayed together """

    def __init__(self, title, slug, feeds, stream_items):
        self.title = title
        self.slug = slug
        self.filepath = "%s%s.html" % (OUTPUT_DIR, slug)
        self.feeds = feeds
        self.stream_items = stream_items

    def __str__(self):
        return "Stream object with title: %s" % self.title



#
# FUNCTIONS FOR REPACKAGING FEED DATA
#
def get_info( stream_data ):
    """ Takes the feedparser/feedcache data for a stream
        and packages it as a list of StreamItem objects """

    stream_items = []
    for d in stream_data:
        feed_info_obj = FeedInfo( get_feed_link(d.feed), 
            get_feed_title(d.feed), get_feed_logo(d.feed) )

        for e in d.entries:
            e_info_obj = StreamItem(feed_info_obj, get_entry_link(e), 
                get_entry_title(e), get_entry_author(e), 
                get_entry_description(e), get_entry_content(e), 
                get_entry_date(e), get_images(e), get_audio(e), get_video(e))
            stream_items.append(e_info_obj)

    return sorted(stream_items, key=lambda e: e.date, reverse=True)


def get_feed_title(feed):
    """ Takes a feedparser feed object """
    try:
        return feed.title
    except:
        return "FEED TITLE UNKNOWN"

def get_feed_link(feed):
    """ Takes a feedparser feed object """
    try:
        return feed.link
    except:
        return "FEED LINK UNKNOWN"

def get_feed_logo(feed):
    """ Takes a feedparser feed object """
    try:
        return feed.logo
    except:
        try:
            return feed.image.href
        except:
            try:
                return feed.image
            except:
                return "FEED LOGO UNKNOWN"

def get_entry_link(e):
    """ Takes a feedparser entry object """
    try:
        return e.link
    except:
        return "ENTRY LINK UNKNOWN"

def get_entry_title(e):
    """ Takes a feedparser entry object """
    try:
        return e.title
    except:
        return "ENTRY TITLE UNKNOWN"

def get_entry_author(e):
    try:
        return e.author
    except:
        return "?"

def get_entry_description(e):
    return e.description
    """
    try:
        return e.description
    except:
        return "UNKNOWN"
    """

def get_entry_content(e):
    try:
        return e.content.value
    except:
        try:
            return e.content
        except:
            return 0

def get_entry_date(e):
    try:
        return e.updated_parsed
    except:
        try:
            return e.pubDate_parsed
        except:
            try:
                return e.published_parsed
            except:
                return "UNKNOWN"

def get_images(e):
    """ Returns a list of image urls """
    images = []
    for enclo in e.enclosures:
        if enclo.type[:5] == 'image':
            images.append(enclo.url)
    return images

def get_audio(e):
    """ Returns a list of urls """
    urls = []
    for enclo in e.enclosures:
        if enclo.type[:5] == 'audio':
            urls.append(enclo.url)
    return urls

def get_video(e):
    """ Returns a list of urls """
    urls = []
    for enclo in e.enclosures:
        if enclo.type[:5] == 'video':
            urls.append(enclo.url)
    return urls


