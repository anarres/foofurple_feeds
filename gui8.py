from feed_controller import fetch_feeds
from settings import *
import easygui as eg
import sys

image1 = "%simages/message1.gif" % MEDIA_DIR
image2 = "%simages/message2.gif" % MEDIA_DIR
msg     = "It'll take a few moments, a box will pop up to let you know when it's all done."

choices = ["Fetch feeds","Quit"]
reply   = eg.buttonbox(msg,image=image1,choices=choices)

if reply == "Fetch feeds":
    fetch_feeds()
else:
    sys.exit()

eg.msgbox(msg="OK, all done.",image=image2)

