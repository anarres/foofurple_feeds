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

f = FeedInfo('http://example.com/rss', 'My awesome RSS feed', 'FIXME')

e = EntryInfo('link', 'Hamlet', 'W. Shakespeare', 'Something is rotten in the state of Denmark', 'none', '15 Sept 1695', f)

print e

a_dict = {'feed_link': f.link, 'feed_title': f.title, 'feed_logo':f.logo, 'entry_description': e.description}

item_template = """
<div class='streamItem'>
    <div class="id_bar">
        <a href='{{ feed_link }}' alt='{{ feed_title }}'>
            <img src='{{ feed_logo }}' style="width:60px;clear:both;" />
        </a>
    </div>
    {{ entry_description }}
</div>
"""

page_template = """
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
<title>Super awesome fun custom feed reader</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div id="nav">
<ul>
    <li><a href="">Alligators</a></li>
    <li><a href="">Some other stuff</a></li>
    <li><a href="">Gazelles</a></li>
    <li><a href="">Aardvarks</a></li>
</ul>
</div> <!--#nav-->
<div id="header">
<h1>Super awesome fun custom feed reader</h1>
</div> <!--#header-->
<div id="main">

{{ main_content }}

</div> <!--#main-->
<div id="footer">
<p>This is the bottom of the page. Hope you've enjoyed reading.</p>
</div> <!--#footer-->
</body>
</html>"""



from jinja2 import Template
t = Template(foo)
print t.render(a_dict)
