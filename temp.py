# coding: utf-8

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
JS_DIR = os.path.join(BASE_DIR, "js")

GLOBS = {'BASE_DIR':BASE_DIR,'OUTPUT_DIR':OUTPUT_DIR,'IMAGES_DIR':IMAGES_DIR,
    'TEMPLATES_DIR':TEMPLATES_DIR, 'JS_DIR':JS_DIR}


#print os.path.join(TEMPLATES_DIR, "" + "." + format)


#print BASE_DIR

filename = "foo.py"
foo = os.path.join(BASE_DIR, filename)
print foo

