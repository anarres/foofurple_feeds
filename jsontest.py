import json

infoo = '["foo", {"bar":["baz", null, 1.0, 2]}]'

infoo = '{"stream_name":"Blogs, in general","feeds":[{"name":"Captain awkward","url":"http://www.captainawkward.com/feed"}]}'



infoo = """
{
"stream_name":"Blogs, in general",
"feeds":[{"name":"Captain awkward","url":"http://www.captainawkward.com/feed"}]
}
"""

infoo = open('test.json','r').read()



infoo = open('streams.json','r').read()


bar = json.loads(infoo)

print bar
