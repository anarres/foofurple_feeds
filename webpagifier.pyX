# coding: utf-8

from jinja2 import Template
import json
import feed_sifter
import logging
import webbrowser

from settings import *
from feed_utils import _slugify

def display_wait_page():
    webbrowser.open('file://%swait.html' % OUTPUT_DIR)

def display_home_page():
    webbrowser.open('file://%sindex.html' % OUTPUT_DIR)

settings_nav = """
<ul>

    <li><a href='index.html'>Home</a></li>
    <li><a href='settings.html'>Set-up</a></li>
    <li><a href='appearance.html'>Appearance</a></li>
    <li><a href='about.html'>About</a></li>

</ul>
"""
settings_nav_index = """
<ul>

    <li class='current'><a href='index.html'>Home</a></li>
    <li><a href='settings.html'>Set-up</a></li>
    <li><a href='appearance.html'>Appearance</a></li>
    <li><a href='about.html'>About</a></li>

</ul>
"""
settings_nav_settings = """
<ul>

    <li><a href='index.html'>Home</a></li>
    <li class='current'><a href='settings.html'>Set-up</a></li>
    <li><a href='appearance.html'>Appearance</a></li>
    <li><a href='about.html'>About</a></li>

</ul>
"""
settings_nav_appearance = """
<ul>

    <li><a href='index.html'>Home</a></li>
    <li><a href='settings.html'>Set-up</a></li>
    <li class='current'><a href='appearance.html'>Appearance</a></li>
    <li><a href='about.html'>About</a></li>

</ul>
"""
settings_nav_about = """
<ul>

    <li><a href='index.html'>Home</a></li>
    <li><a href='settings.html'>Set-up</a></li>
    <li><a href='appearance.html'>Appearance</a></li>
    <li class='current'><a href='about.html'>About</a></li>
</ul>
"""



# Takes a list of Stream objects
def make_nav(streams_list, current_stream_title=""):
    html = "<h2>My Streams:</h2><ul>"
    for s in streams_list:
        if s.title == current_stream_title:
            html += "<li class='current'><a href='%s'>%s</a></li>" % (s.get_filename(), s.title)
        else:
            html += "<li class='current'><a href='%s'>%s</a></li>" % (s.get_filename(), s.title)
    html += "</ul>"
    return html


# Takes a single Stream object
def make_main_content(streams_list, s):
    items_html = ""
    for e in s.entry_info_objects:
        items_html += item_template.render( e.get_dict() )
    return items_html


def make_all_the_webpages(streams_list):

    # Write the stream pages 
    for s in streams_list:
        nav = make_nav(streams_list, current_stream_title=s.title)
        main_content = make_main_content(streams_list, s)
        output_html = page_template.render({'main_content':main_content, 
            'title':s.title, 'nav':nav, 'settings_nav':settings_nav, 'javascript':'','GLOBS':GLOBS})
        f = open(s.get_filename(), 'w')
        f.write(output_html.encode('utf-8'))
        f.close()
        print "%s written." % s.get_filename()

    nav = make_nav(streams_list)

    # Write the index page
    index_main_content = "<h2>My Streams:</h2>"
    for s in streams_list:
        index_main_content += index_template.render({'stream_title':s.title, 'stream_url':s.get_filename()})
    index_html = page_template.render({'main_content':index_main_content, 
        'title':'Home', 'nav':'', 'settings_nav':settings_nav_index, 'javascript':'','GLOBS':GLOBS})
    f = open('%sindex.html' % OUTPUT_DIR, 'w')
    f.write(index_html)
    f.close()

    # Write the settings page
    settings_js = "<script type='text/javascript' src='%sjs/settings.js'></script>" % MEDIA_DIR
    settings_main_content = open('%ssettings_main_content' % TEMPLATES_DIR,'r').read()

    for s in streams_list:
        settings_main_content += stream_template.render({'stream_title':s.title, 
            'stream_url':s.get_filename(), 'stream_feeds':s.feeds_list})
    settings_main_content += "</div> <!--#streamGoHere-->"
    settings_main_content += "<button onclick='addStream()'>Create a new stream</button>"
    settings_main_content += "<button class='bigButton' onclick='saveAllChanges()'>SAVE ALL CHANGES</button>"
    settings_html = page_template.render({'main_content':settings_main_content, 
        'title':'Home', 'nav':nav, 'settings_nav':settings_nav_settings, 
        'javascript':settings_js,'GLOBS':GLOBS})
    f = open('%ssettings.html' % OUTPUT_DIR, 'w')
    f.write(settings_html)
    f.close()

    # Write the appearance page
    appearance_js = "<script type='text/javascript' src='%sjs/appearanceSettings.js'></script>" % MEDIA_DIR
    appearance_html = page_template.render({'main_content':appearance_main_content, 
        'title':'Appearance', 'nav':nav, 'settings_nav':settings_nav_appearance, 
        'javascript':appearance_js,'GLOBS':GLOBS})
    f = open('%sappearance.html' % OUTPUT_DIR, 'w')
    f.write(appearance_html)
    f.close()

    # Write the about page
    about_html = page_template.render({'main_content':about, 
        'title':'About', 'nav':nav, 'settings_nav':settings_nav_about, 
        'javascript':'','GLOBS':GLOBS})
    f = open('%sabout.html' % OUTPUT_DIR, 'w')
    f.write(about_html)
    f.close()


