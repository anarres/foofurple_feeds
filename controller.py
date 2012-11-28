import webbrowser
import json
import shelve

import cache
import webpagifier
import feed_sifter
from feed_sifter import SetOfFeeds


def get_parsed_data(urls=[]):

    parsed_datums = []

    print 'Saving feed data to ./.feedcache'
    storage = shelve.open('.feedcache')
    try:
        fc = cache.Cache(storage)
        for url in urls:
            parsed_data = fc.fetch(url)
            """
            for entry in parsed_data.entries:
                parsed_datums.append(entry)
            """
            parsed_datums.append(parsed_data)
    finally:
        storage.close()
    return parsed_datums


def main():

    webbrowser.open('file:///home/katie/prog/foofurple_feeds/wait.html')

    # Get the list of streams and feeds
    streams = json.loads(open('streams.json','r').read())
    sets_of_feeds = []

    # Create SetOfFeeds objects
    for s in streams:
        sets_of_feeds.append( SetOfFeeds(s['stream_name'], s['feeds']) )

    for s in sets_of_feeds:
        parsed_datums = get_parsed_data(urls=s.get_urls())
        s.entry_info_objects = feed_sifter.get_info(parsed_datums)

    webpagifier.make_all_the_webpages(sets_of_feeds)

    webbrowser.open('file:///home/katie/prog/foofurple_feeds/wait.html')


main()

