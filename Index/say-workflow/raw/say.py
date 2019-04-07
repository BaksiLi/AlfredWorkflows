#!/usr/bin/python
# -*- coding: utf-8 -*
__version__ = '0.2_alfred'
import os
import sys

langs = {'jp':'Kyoko','en':'Daniel','ch':'Sin-ji','fr':'Thomas'}

query = sys.argv[1]

if "'" in query:
    query = query.replace("'", "’")

recog = query[0] + query[1]
if recog in langs:
    says = '-v ' + langs[recog] + ' '
    for i in range(2, len(query)):
        says += query[i]
elif query == 'who you are':
    says = 'I am your assistant.'
else:
    says = query

os.system('say ' + says)
