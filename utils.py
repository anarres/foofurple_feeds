from time import localtime
import re

def day_of_the_week(int_day):
    days = ('Monday','Tuesday','Wednesday','Thursday',
        'Friday','Saturday','Sunday')
    return days[int_day]

def month(int_month):
    index = int_month - 1
    months = ('January','February','March','April','May', 
     'June','July','August','September','October','November','December')
    return months[index]

def nice_now():
    t = localtime()
    day_name = day_of_the_week(t[6])
    month_name = month(t[1])
    return "%s %s %s at %s:%s" % (day_name, str(t[2]), month_name, 
        str(t[3]).zfill(2), str(t[4]).zfill(2))


def slugify(value):

    _slugify_strip_re = re.compile(r'[^\w\s-]')
    _slugify_hyphenate_re = re.compile(r'[-\s]+')

    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    
    From Django's "django/template/defaultfilters.py".
    """
    import unicodedata
    if not isinstance(value, unicode):
        value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(_slugify_strip_re.sub('', value).strip().lower())
    return _slugify_hyphenate_re.sub('-', value)

