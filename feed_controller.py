from jinja2 import Template
import re
import feed_sifter
from config import feeds_config

OUTPUT_DIR = "/home/katie/prog/foofurple_feeds/output/"
MEDIA_DIR = "/home/katie/prog/foofurple_feeds/media/"
TEMPLATES_DIR = "/home/katie/prog/foofurple_feeds/templates/"

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


item_template = open('%sitem' % TEMPLATES_DIR,'r').read()
page_template = open('%spage' % TEMPLATES_DIR,'r').read()
list_template = open('%slist' % TEMPLATES_DIR,'r').read()

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

    parsed_datums = feed_sifter.feedcache_foo(s.get_urls())
    entry_info_objects = feed_sifter.get_info(parsed_datums)
    #list_html = ""
    items_html = ""
    for e in entry_info_objects:
        #list_html += t3.render( e.get_dict() )
        items_html += t.render( e.get_dict() )
    output_html = t2.render({'main_content':items_html, 'title':s.title, 'nav':nav}) 

    f = open(s.get_filename(), 'w')
    f.write(output_html)
    f.close()

    print "%s written." % s.get_filename()

