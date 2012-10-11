from jinja2 import Template
import re
import utils_foo
from config import feeds_config

OUTPUT_DIR = "output/"

_slugify_strip_re = re.compile(r'[^\w\s-]')
_slugify_hyphenate_re = re.compile(r'[-\s]+')
def _slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    
    From Django's "django/template/defaultfilters.py".
    """
    import unicodedata
    if not isinstance(value, unicode):
        value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(_slugify_strip_re.sub('', value).strip().lower())
    return _slugify_hyphenate_re.sub('-', value)


item_template = open('templates/item','r').read()
page_template = open('templates/page','r').read()
list_template = open('templates/list','r').read()

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

"""
feeds1 = SetOfFeeds('Blogs, in general', 
    [{'name':'Captain awkward','url':'http://www.captainawkward.com/feed'}, 
    {'name':'BoingBoing','url':'http://boingboing.net/feed'}])

feeds2 = SetOfFeeds("Blogs, less frequently updated", 
    [{'name':'Hoyden About Town','url':'http://hoydenabouttown.com/feed/'}, 
    {'name':'Feminist Action Cambridge','url':'http://www.feministactioncambridge.wordpress.com/feed'}])

feeds3 = SetOfFeeds("Data, programming", 
    [{'name':'Whimsley','url':'http://whimsley.typepad.com/whimsley/atom.xml'}, 
    {'name':'Social Media Collective','url':'http://socialmediacollective.org/feed/'},
    {'name': 'Bad Science', 'url':'http://www.badscience.net/feed/'},
    {'name': 'Buddycloud blog', 'url':'http://blog.buddycloud.com/rss'},
    {'name': 'Dreamwidth news', 'url':'http://dw-news.dreamwidth.org/data/atom'},
    {'name': 'Dreamwidth dev', 'url':'http://dw-dev.dreamwidth.org/data/atom'},
    {'name': 'bengoldacre secondary blog', 'url':'http://bengoldacre.posterous.com/rss.xml'}])

feeds4 = SetOfFeeds('Auf Deutsch',
    [{'name':'SWR Wissen','url':'http://www1.swr.de/podcast/xml/swr2/wissen.xml'},
    {'name':'Softmetz', 'url':'http://identi.ca/api/statuses/user_timeline/85379.atom'},
    {'name':'Sendung mit der Maus','url':'http://podcast.wdr.de/maus.xml'},
    {'name':'Quanks und co', 'url':'http://podcast.wdr.de/quarks.xml'},
    {'name':'DW.DW Journal Reporer','url':'http://rss.dw.de/xml/podcast_journal-reporter'}])

sets_of_feeds = [feeds1, feeds2, feeds3, feeds4]
"""
sets_of_feeds = []

for s in feeds_config:
    sets_of_feeds.append( SetOfFeeds(s['stream_name'], s['feeds']) )


nav_template = """<ul>%s<li><a href='about.html'>About</a></li><li><a href='config.html'>Configuration</a></li></ul>"""
html = ""
for s in sets_of_feeds:
    html += """<li><a href='%s'>%s</a></li>""" % (s.get_filename(), s.title)
nav = nav_template % html

t = Template(item_template)
t2 = Template(page_template)
#t3 = Template(list_template)

# Make the static 'about' page
about_content = """
    <h2>Welcome to the Foofurple Feed Reader!</h2>
    <p>I should put some text here sometime.</p>
    """

about = t2.render({'main_content':about_content, 'title':'About: Foofurple Feed Reader', 'nav':nav}) 
f = open('about.html', 'w')
f.write(about)
f.close()

for s in sets_of_feeds:

    parsed_datums = utils_foo.feedcache_foo(s.get_urls())
    entry_info_objects = utils_foo.get_info(parsed_datums)
    #list_html = ""
    items_html = ""
    for e in entry_info_objects:
        #list_html += t3.render( e.get_dict() )
        items_html += t.render( e.get_dict() )
    output_html = t2.render({'main_content':items_html, 'title':s.title, 'nav':nav}) 

    f = open(s.get_filename(), 'w')
    f.write(output_html)
    f.close()

