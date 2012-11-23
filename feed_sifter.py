# coding: utf-8

import sys
import time
import shelve
import cache

"""
CLASSES FOR PUTTING FEED DATA INTO THE FORMAT I WANT TO DISPLAY
"""
class EntryInfo(object):
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
        return "EntryInfo object, title: %s." % self.title

    def get_dict(self):
        my_dict = {'entry_link':self.link, 'entry_title':self.title, 'entry_author':self.author, 'entry_description':self.description, 'entry_content':self.content, 'entry_date':self.nice_date, 'feed_link':self.feed_obj.link, 'feed_title':self.feed_obj.title, 'feed_logo':self.feed_obj.logo, 'images':self.images, 'audio':self.audio, 'video':self.video}

        if self.content == 0:
            my_dict['entry_content'] = "<p>%s</p>" % self.description
        return my_dict

class FeedInfo(object):
    def __init__(self, link, title, logo):
        self.link = link
        self.title = title
        self.logo = logo     
    def __str__(self):
        return "FeedInfo object: title: %s, link: %s, logo: %s." % (self.title, self.link, self.logo)


"""
FUNCTIONS FOR CONVERTING PARSED FEED INTO THE INFO I WANT TO DISPLAY
"""
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


"""
Feedcache - FIXME credit
"""
def feedcache_foo(urls=[]):
    """ Uses feedcache to return a list containing parsed data for each feed url """

    print 'Saving feed data to ./.feedcache'
    storage = shelve.open('.feedcache')
    try:
        fc = cache.Cache(storage)
        parsed_datums = []
        for url in urls:
            parsed_datums.append( fc.fetch(url) )
    finally:
        storage.close()
    return parsed_datums


def get_info( parsed_datums ):
    entry_info_objs = []
    for d in parsed_datums:
        f = d.feed
        feed_info_obj = FeedInfo( get_feed_link(f), get_feed_title(f), get_feed_logo(f) )

        for e in d.entries:
            e_info_obj = EntryInfo( feed_info_obj, get_entry_link(e), get_entry_title(e), get_entry_author(e), get_entry_description(e), get_entry_content(e), get_entry_date(e), get_images(e), get_audio(e), get_video(e) )
            entry_info_objs.append(e_info_obj)
    return sorted(entry_info_objs, key=lambda e: e.date, reverse=True)



