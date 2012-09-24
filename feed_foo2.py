import sys
import shelve
import cache

"""
CLASSES FOR PUTTING FEED DATA INTO THE FORMAT I WANT TO DISPLAY,
(NOTHING TO DO WITH FEEDPARSER OR FEEDCACHE)
"""
class EntryInfo(object):
    def __init__(self, link, title, author, description, content, date, feed_obj):
        self.link = link
        self.title = title
        self.author = author
        self.description = description
        self.content = content
        self.date = date
        self.feed_obj = feed_obj   # How are u sposed to do this?
    def __str__(self):
        return "EntryInfo object, title: %s." % self.title

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
        return "AUTHOR UNKNOWN"

def get_entry_description(e):
    try:
        return e.description
    except:
        return "UNKNOWN"

def get_entry_content(e):
    try:
        return e.content
    except:
        return "UNKNOWN"

def get_entry_date(e):
    try:
        return e.updated
    except:
        try:
            return e.pubDate
        except:
            try:
                return e.published
            except:
                return "UNKNOWN"
"""
"
"""
def let_feedcache_do_its_thing(urls=[]):
    """ Returns a list containing parsed data for each feed url """
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


def get_entry_info_objects( parsed_datums ):
    for d in parsed_datums:
        f = d.feed
        feed_info_obj = FeedInfo( get_feed_link(f), get_feed_title(f), get_feed_logo(f) )
        entry_info_objs = []
        for e in d.entries:
            e_info_obj = EntryInfo( get_entry_link(e), get_entry_title(e), get_entry_author(e), get_entry_description(e), get_entry_content(e), get_entry_date(e), feed_info_obj )
            entry_info_objs.append(e_info_obj)
    return entry_info_objs
        
urls = ['http://www.captainawkward.com/feed/', 'http://www.feministactioncambridge.wordpress.com/feed/', 'http://boingboing.net/feed', 'http://identi.ca/api/statuses/public_timeline.rss']

parsed_datums = let_feedcache_do_its_thing(urls)
entry_info_objects = get_entry_info_objects( parsed_datums )

for o in entry_info_objects:
    print o.title
    print o.author 
