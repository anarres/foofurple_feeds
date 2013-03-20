#!/usr/bin/env python
# coding: utf-8

import json
import shelve
import webbrowser
import feedparser

import cache
import webpagifier
import feed_sifter
from settings import OUTPUT_DIR, JS_DIR, TEMPLATES_DIR
from utils import slugify

def display_wait_page():
    webbrowser.open('%swait.html' % TEMPLATES_DIR)

def display_home_page():
    webbrowser.open('%sindex.html' % OUTPUT_DIR)

def get_parsed_data(urls=[]):
    """ Use Feedcache and FeedParser to get and cache the feeds """
    parsed_datums = []
    print "Saving feed data to ./.feedcache"
    storage = shelve.open('.feedcache')
    try:
        fc = cache.Cache(storage)
        for url in urls:
            parsed_data = fc.fetch(url)
            parsed_datums.append(parsed_data)
    finally:
        storage.close()
    return parsed_datums


def title_match(streams,s_name):
    """ Used to make sure stream titles and slugs are unique """
    result = False
    for stream in streams:
        if stream.title == s_name:
            result = True
            break
    return result

def slug_match(streams,s_slug):
    """ Used to make sure stream titles and slugs are unique """
    result = False
    for stream in streams:
        if stream.slug == s_slug:
            result = True
            break
    return result

def unique_title_and_slug(streams,s):
    """ Used to make sure stream titles and slugs are unique """
    title = s['stream_name']
    if title_match(streams, title):
        c = 1
        while True:
            c += 1
            title = s['stream_name'] + str(c)
            if not title_match(streams, title):
                break
    slug = slugify(title)
    if slug_match(streams, slug):
        c = 1
        while True:
            c += 1
            slug = slugify(title) + str(c)
            if not slug_match(streams, slug):
                break
    return (title, slug)


def main():
    display_wait_page()
    json_foo = open('%sjsonFoo.js' % JS_DIR,'r').read()
    start_delimiter = """/*STARTJSON*/"""
    end_delimiter = """/*ENDJSON*/"""
    json_foo = json_foo.split(start_delimiter)[1]
    json_foo = json_foo.split(end_delimiter)[0]
    json_streams = json.loads(json_foo)

    # Check if any feeds are in need of a title
    overwrite_json = False
    for s in json_streams:

        for f in s['feeds']:

            if f['name'] == "New feed":
                overwrite_json = True
                d = feedparser.parse(f['url'])
                try:
                    f['name'] = d['feed']['title']
                except:
                    pass


    if overwrite_json:
        output = "var jsonStreams = /*STARTJSON*/%s/*ENDJSON*/;" % json.dumps(json_streams)
        f = open("%sjsonFoo.js" % JS_DIR, 'w')
        f.write(output)
        f.close()

    streams = []
    for s in json_streams:
        (stream_name, stream_slug) = unique_title_and_slug(streams, s)
        urls = []
        feeds = []
        for f in s['feeds']:
            urls.append(f['url'])
            new_dict = {'url':f['url'],'name':f['name']}
            feeds.append(new_dict)

        parsed_datums = get_parsed_data(urls=urls)
        entry_info_objects = feed_sifter.get_info(parsed_datums)
        streams.append( feed_sifter.Stream(stream_name, stream_slug, feeds, entry_info_objects) )

    webpagifier.make_all_the_webpages(streams)
    display_home_page()

main()



