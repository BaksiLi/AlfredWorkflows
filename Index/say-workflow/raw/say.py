#!/usr/bin/python
# -*- coding: utf-8 -*
__version__ = '0.4_alfred'
import os
import sys


def is_anagram(word1, word2):
    if len(word1.lower()) != len(word2.lower()):
        return False
    return sorted(word1.lower()) == sorted(word2.lower())


# ---

# Settings
voice_default = 'en'
voices = {
    'en': 'Daniel',
    'jp': 'Kyoko',
    'ch': 'Sin-ji',
    'fr': 'Thomas',
    'kr': 'Yuna'
}  # dic of voices
replace_words = {
    '’': "'",
    '`': "'",
    'fuck': 'f-word'
}  # dict of words to replace

# Read query
query = sys.argv[1]

# Replace words
for word in replace_words:
    if word in query:
        query = query.replace(word, replace_words[word])

# Text processing
try:  # try to recognise any voice names
    recog = query[:2]  # the first two letters
    for voice in voices:
        if is_anagram(recog, voice):
            recog = voice
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

# Run command
os.system('say ' + says)
