class Silly(object):
    def __init__(self, greet, when):
        self.greet = greet
        self.when = when


# File: datetime-example-1.py

import datetime

now = datetime.datetime(2003, 8, 4, 12, 30, 45)

print now
print repr(now)
print type(now)
print now.year, now.month, now.day
print now.hour, now.minute, now.second
print now.microsecond


"""
a = Silly('hi!', datetime.datetime(2004, 2, 4, 12, 30, 45))
b = Silly('hi!', datetime.datetime(2011, 8, 4, 12, 30, 45))
c = Silly('hi!', datetime.datetime(2003, 6, 4, 12, 30, 45))
d = Silly('hi!', datetime.datetime(1999, 8, 4, 12, 30, 45))

foolist = [a,b,c,d]
print foolist

newlist = sorted(foolist, key=lambda s: s.when, reverse=True)
for n in newlist:
    print n.when
"""
