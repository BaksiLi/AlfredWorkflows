#!/usr/bin/python
# -*- coding: utf-8 -*
__version__ = '0.3_alfred'
import os
import sys

query = sys.argv[1]

if "’" in query:
    query = query.replace("’", "'")

voices = {'en':'Daniel','jp':'Kyoko','ch':'Sin-ji','fr':'Thomas', 'kr': 'Yuna'}
voice_default = 'en'  # not `really default'

try:  # try to recognise any voice names
    recog = query[:2].lower()  # the first two letters
except IndexError:
	recog = voice_default  # if failed, use the `default voice'

if recog in voices:
    says = '-v ' + voices[recog] + ' '
    for i in range(2, len(query)):
        says += query[i]
elif query == '?':  # Easter Egg!
    says = 'I am your assistant.'
else:
    says = query

os.system('say ' + says)
