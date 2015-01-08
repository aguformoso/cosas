__author__ = 'agustin'

import os

BASEDIR = '.'
for app in os.listdir(BASEDIR):
    for deploy in os.listdir("%s/%s" % BASEDIR, app):
