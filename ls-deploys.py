#!/usr/bin/python
# coding=UTF-8
from calendar import monthrange

__author__ = 'agustin'

import os, sys, getopt, locale, argparse, calendar
from datetime import datetime, timedelta

ahora = datetime.now()
locale.setlocale(locale.LC_TIME, "es_ES")

# Arguments parsing

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directorio", help="Especifica el directorio raíz del arbol de deploys.")
parser.add_argument("-m", "--meses", help="Especifica la cantidad de meses que se quiere que el resumen abarque. Por ejemplo -m 6 hace un resumen de los últimos 6 meses.",
                    type=int)
# parser.add_argument("-l", "--largo", help="Despliega información más detallada de los deploys.", action="store_true")
parser.add_argument("-hist", "--histograma", help="Despliega un histograma de los deploys.", action="store_true")
args = parser.parse_args()

if args.directorio:
    BASEDIR = args.directorio
else:
    BASEDIR = '.'

# TODO mejorar el cálculo de los meses
# TODO considerar meses vacíos en el histograma
# TODO ver cuál es  la etiqueta de mes más larga y dejar ese espacio para el histograma
if args.meses:
    desde = ahora - timedelta(days=30*args.meses)
else:
    desde = datetime(year=2014, month=1, day=1)

histograma = args.histograma


apps = dict() # { app1 : [(deploy1, date1), (deploy2, date 2)], ... }
histogram = dict() # { mes1 : [app1, app2], ... }

for app in os.listdir(BASEDIR):

    appDir = "%s/%s" % (BASEDIR, app)

    if not os.path.isdir(appDir):
        continue

    deploys = []
    for deploy in os.listdir(appDir):

        deployDir = "%s/%s" % (appDir, deploy)

        if not os.path.isdir(deployDir):
            continue

        if deploy[0] is '.' or deploy[0] is '..':
            continue

        date = datetime.strptime(deploy[:8], "%Y%m%d")
        if date < desde:
            continue

        deploys.append((deploy, date))
        try:
            histogram[calendar.month_name[date.month]].append(app)
        except KeyError:
            histogram[calendar.month_name[date.month]] = [app]

    apps[app] = deploys

# Summary generation

# for app in apps.keys():
#     deploys = apps[app]
#
#     if len(deploys) == 0:
#         continue
#
#     print app
#     for deploy in deploys:
#         fecha = deploy[1]
#         print "\t%s\t%s" % (deploy[0], fecha.strftime('%x'))

# Per-month summary

for month in histogram.keys():
    # monthlyApps = list(set(histogram[month])) # get unique instances
    monthlyApps = histogram[month]

    if len(monthlyApps) == 0:
        continue

    print month
    unicas = dict()
    for monthlyApp in monthlyApps:
        # print unicas.keys()
        try: unicas[monthlyApp] += 1
        except KeyError: unicas[monthlyApp] = 1

    for unica in unicas.keys():
        print "\t%s (%s)" % (unica, unicas[unica])

# Print histogram

if histograma:
    print "\nHistograma\n===\n"
    for h in histogram.keys():
        count = len(histogram[h])
        print "%s (%s) %s" % (h, count, '|' * count)