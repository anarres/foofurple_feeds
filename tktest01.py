#http://zetcode.com/gui/tkinter/introduction/

import Tkinter 
from Tkinter import *
root = Tk()

def callback():
    print "click!"

root.title('Foofurple Feed Reader')

Button(root, text='Get new feed items!', command=callback, fg='black', bg='white').pack(side=LEFT,padx=50,pady=40)

root.mainloop()





