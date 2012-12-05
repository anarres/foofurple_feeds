import datetime

def date_msg():
    msg = "Feeds were last updated on "
    msg += datetime.datetime.now().strftime('%c')
    return msg

print date_msg()
