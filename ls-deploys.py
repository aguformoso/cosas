#!/usr/bin/python

__author__ = 'agustin'

import os, sys

BASEDIR = '.'
if len(sys.argv) == 2:
    BASEDIR = sys.argv[1]

for app in os.listdir(BASEDIR):

    print app
    if not os.path.isdir(app):
        print "no es"
        continue

    for deploy in os.listdir("%s/%s" % (BASEDIR, app)):
        if not os.path.isdir(deploy):
            continue

        print app
        print deploy