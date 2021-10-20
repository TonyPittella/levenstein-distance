import csv
import string
from copy import copy
from Levenshtein import easy_leven
#from Levenshtein import *

def clean_text(wd):
    wd = wd.strip().lower()
    return wd.translate(str.maketrans('', '', string.punctuation))


with open('data/random_text.txt', 'r') as wds_file:
    words = list(map(clean_text, wds_file.read().split()))
    words_copy = copy(words)
    words.reverse()

with open('data/wordlist.csv', 'w') as wdlist:
    for wd1, wd2 in zip(words_copy, words):
        dist = easy_leven(wd1, wd2)
        writer = csv.writer(wdlist)
        writer.writerow([wd1, wd2, str(dist)])
