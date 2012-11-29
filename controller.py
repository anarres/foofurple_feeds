import json
import shelve

import cache
import webpagifier
import feed_sifter


# Use Feedcache and FeedParser to get and cache the feeds
def get_parsed_data(urls=[]):
    parsed_datums = []
    print 'Saving feed data to ./.feedcache'
    storage = shelve.open('.feedcache')
    try:
        fc = cache.Cache(storage)
        for url in urls:
            parsed_data = fc.fetch(url)
            parsed_datums.append(parsed_data)
    finally:
        storage.close()
    return parsed_datums


def main():
    webpagifier.display_wait_page()
    streams = json.loads(open('streams.json','r').read())
    sets_of_feeds = []

    for s in streams:
        sets_of_feeds.append( feed_sifter.Stream(s['stream_name'], s['feeds']) )

    for s in sets_of_feeds:
        parsed_datums = get_parsed_data(urls=s.get_urls())
        s.entry_info_objects = feed_sifter.get_info(parsed_datums)

    webpagifier.make_all_the_webpages(sets_of_feeds)
    webpagifier.display_home_page()


main()

