# coding: utf-8

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
JS_DIR = os.path.join(BASE_DIR, "js")

JSON_PATH = os.path.join(OUTPUT_DIR, "jsonFoo.js")
LOGO_PATH = os.path.join(IMAGES_DIR, "dinoLogo.png")
ICON_PATH = os.path.join(IMAGES_DIR, "dinoIcon2.png")


GLOBS = {'BASE_DIR':BASE_DIR,'OUTPUT_DIR':OUTPUT_DIR,'IMAGES_DIR':IMAGES_DIR,
    'TEMPLATES_DIR':TEMPLATES_DIR, 'JS_DIR':JS_DIR, 'JSON_PATH':JSON_PATH,
    'LOGO_PATH':LOGO_PATH,'ICON_PATH':ICON_PATH}



