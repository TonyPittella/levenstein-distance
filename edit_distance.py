from itertools import zip_longest
from pprint import pprint as pp
from difflib import ndiff, Differ


def easy_leven(str_1, str_2):
    LevensteinDict = {'Insertions': 0, 'Substitutions': 0, 'Distance Total': 0}
    list_string1 = list(str_1.split())
    list_string2 = list(str_2.split())
    length_string1 = len(str_1)
    length_string2 = len(str_2)
    distanceForTest = 0
    if str_1 == str_2:
        return 0
    if length_string1 == length_string2:
        for index, x in enumerate(str_1):
            if x != str_2[index]:
                LevensteinDict['Distance Total'] += 1
                LevensteinDict['Substitutions'] += 1
                distanceForTest += 1
            return distanceForTest , LevensteinDict
    elif length_string1 != length_string2:
        if length_string1 > length_string2:
            for index, x in enumerate(str_1):
                if index < length_string2:
                    if x != str_2[index]:
                        LevensteinDict['Distance Total'] += 1
                        LevensteinDict['Substitutions'] += 1
                        distanceForTest += 1
                elif index >= length_string2:
                    LevensteinDict['Distance Total'] += 1
                    LevensteinDict['Insertions'] += 1
                    distanceForTest += 1
            return distanceForTest , LevensteinDict
        if length_string2 > length_string1:
            for index, x in enumerate(str_2):
                if index < length_string1:
                    if x != str_1[index]:
                        LevensteinDict['Distance Total'] += 1
                        LevensteinDict['Substitutions'] += 1
                        distanceForTest += 1
                elif index >= length_string1:
                    LevensteinDict['Distance Total'] += 1
                    LevensteinDict['Insertions'] += 1
                    distanceForTest += 1
            return distanceForTest , LevensteinDict

pp(easy_leven("that is correct", "the"))
