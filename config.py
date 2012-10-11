OUTPUT_DIR = "/home/katie/prog/foofurple_feeds/output/"
MEDIA_DIR = "/home/katie/prog/foofurple_feeds/media/"
TEMPLATES_DIR = "/home/katie/prog/foofurple_feeds/templates/"

feeds_config = [

{ 'stream_name':'Blogs, in general',
'feeds':
[{'name':'Captain awkward','url':'http://www.captainawkward.com/feed'},
    {'name':'BoingBoing','url':'http://boingboing.net/feed'}] },


{ 'stream_name':'Blogs, less frequently updated',
'feeds':
[{'name':'Hoyden About Town','url':'http://hoydenabouttown.com/feed/'},
    {'name':'Feminist Action Cambridge','url':'http://www.feministactioncambridge.wordpress.com/feed'}] },


{ 'stream_name':'Data, programming',
'feeds':
[{'name':'Whimsley','url':'http://whimsley.typepad.com/whimsley/atom.xml'},
    {'name':'Social Media Collective','url':'http://socialmediacollective.org/feed/'},
    {'name': 'Bad Science', 'url':'http://www.badscience.net/feed/'},
    {'name': 'Buddycloud blog', 'url':'http://blog.buddycloud.com/rss'},
    {'name': 'Dreamwidth news', 'url':'http://dw-news.dreamwidth.org/data/atom'},
    {'name': 'Dreamwidth dev', 'url':'http://dw-dev.dreamwidth.org/data/atom'},
    {'name': 'bengoldacre secondary blog', 'url':'http://bengoldacre.posterous.com/rss.xml'}] },


{ 'stream_name':'Auf Deutsch',
'feeds':
 [{'name':'SWR Wissen','url':'http://www1.swr.de/podcast/xml/swr2/wissen.xml'},
    {'name':'Softmetz', 'url':'http://identi.ca/api/statuses/user_timeline/85379.atom'},
    {'name':'Sendung mit der Maus','url':'http://podcast.wdr.de/maus.xml'},
    {'name':'Quanks und co', 'url':'http://podcast.wdr.de/quarks.xml'},
    {'name':'DW.DW Journal Reporer','url':'http://rss.dw.de/xml/podcast_journal-reporter'}] }

]
