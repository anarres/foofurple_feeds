from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


from settings import *

env = Environment()
env.loader = FileSystemLoader('./templates/')
tmpl = env.get_template('about.html')
print tmpl.render({'title':'About'})


