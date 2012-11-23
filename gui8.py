from feed_controller import fetch_feeds

import easygui as eg
import sys

image   = "message1.gif"
msg     = "It'll take a few moments, a box will pop up to let you know when it's all done."
choices = ["Fetch feeds","Quit"]
reply   = eg.buttonbox(msg,image=image,choices=choices)

if reply == "Fetch feeds":
    fetch_feeds()
else:
    sys.exit()

eg.msgbox(msg="OK, all done.",image="message2.gif")

