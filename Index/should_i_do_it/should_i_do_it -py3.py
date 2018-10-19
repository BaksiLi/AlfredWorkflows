#!/usr/bin/python
# -*- coding: utf-8 -*
__version__ = '0.1 - python3'
import random


def whe():
    whether = random.randint(1,9)
    if whether % 2 != 0:
        print('just do it!\n')
    else:
        txt ='"not all those who wonder are lost... But you are!\n"'+\
              'just take a rest and think about it again!\n'
        print(txt)

start = input('')
whe()

input('')
