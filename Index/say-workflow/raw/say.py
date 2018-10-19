# -*- coding: utf-8 -*
__version__ = '0.1_alfred'
import os
import sys

langs = {'jp':'Kyoko','en':'Daniel'}

query = sys.argv[1]

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