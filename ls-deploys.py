#!/usr/bin/python

__author__ = 'agustin'

import os, sys, getopt, locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, "es_ES")

BASEDIR = '.'
if len(sys.argv) == 2:
    BASEDIR = sys.argv[1]

apps = dict()

for app in os.listdir(BASEDIR):

    appDir = "%s/%s" % (BASEDIR, app)

    if not os.path.isdir(appDir):
        continue

    deploys = []
    for deploy in os.listdir(appDir):

        deployDir = "%s/%s" % (appDir, deploy)

        if not os.path.isdir(deployDir):
            continue

        if deploy[0] is '.':
            continue

        date = datetime.strptime(deploy[:8], "%Y%m%d")
        deploys.append((deploy, date))

    apps[app] = deploys

for app in apps.keys():
    deploys = apps[app]
    if len(deploys) == 0:
        continue

    print app
    for deploy in deploys:
        print "\t%s\t%s" % (deploy[0], deploy[1].strftime('%x'))