from jinja2 import Template
import re
import utils_foo


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



item_template = open('item_template','r').read()
page_template =  open('page_template','r').read()

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
        return "%s.html" % _slugify(self.title)



feeds1 = SetOfFeeds('Feeds page 1', 
    [{'name':'Captain awkward','url':'http://www.captainawkward.com/feed'}, 
    {'name':'BoingBoing','url':'http://boingboing.net/feed'}])

feeds2 = SetOfFeeds('Feeds page 2 - auf Deutsch', 
    [{'name':'SWR Wissen','url':'http://www1.swr.de/podcast/xml/swr2/wissen.xml'}, 
    {'name':'DW.DW Journal Reporer','url':'http://rss.dw.de/xml/podcast_journal-reporter'}])

sets_of_feeds = [feeds1, feeds2]

nav_template = """<ul>%s<li><a href='about.html'>About</a></li></ul>"""
html = ""
for s in sets_of_feeds:
    html += """<li><a href='%s'>%s</a></li>""" % (s.get_filename(), s.title)
nav = nav_template % html

t = Template(item_template)
t2 = Template(page_template)

for s in sets_of_feeds:

    parsed_datums = utils_foo.feedcache_foo(s.get_urls())
    entry_info_objects = utils_foo.get_info(parsed_datums)
    items_html = ""
    for e in entry_info_objects:
        items_html += t.render( e.get_dict() )
    output_html = t2.render({'main_content':items_html, 'title':s.title, 'nav':nav}) 

    f = open(s.get_filename(), 'w')
    f.write(output_html)
    f.close()

