from jinja2 import Template
import utils_foo

item_template = """
<div class='streamItem'>
    <div class="feed_icon">
        <a href='{{ feed_link }}'>
            <img src='{{ feed_logo }}' alt='{{ feed_title }}' style="width:60px;clear:both;" />
        </a>
    </div> <!--.feed_icon-->
    <div class='item_main'>
        <a href='{{ entry_link }}'>{{ entry_title }}</a> by {{ entry_author }}, {{ entry_date }}
        <br>
        {{ entry_content }}
        <div class='read_more'>
            <a href='{{ entry_link }}'>Read more</a>
        </div> <!--.read_more-->
    </div> <!--.item_main-->
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

urls = ['http://www.captainawkward.com/feed/', 'http://www.feministactioncambridge.wordpress.com/feed/', 'http://boingboing.net/feed', 'http://identi.ca/api/statuses/public_timeline.rss', 'http://www1.swr.de/podcast/xml/swr2/wissen.xml']

parsed_datums = utils_foo.let_feedcache_do_its_thing(urls)
entry_info_objects = utils_foo.get_entry_info_objects( parsed_datums )



#entry_info_objects = entry_info_objects.sort(key=lambda e: e.date)





t = Template(item_template)

items_html = ""
for e in entry_info_objects:
    items_html += t.render( e.get_dict() )

t2 = Template(page_template)

output_html = t2.render({'main_content':items_html}) 

f = open('output.html', 'w')
f.write(output_html)
f.close()



