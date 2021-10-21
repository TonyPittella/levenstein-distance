from pprint import pprint as pp

# from flask import Flask
# from flask_caching import Cache

leven_on_a_prayer_cache = {}


def easy_leven(str_1, str_2):
    """
    This is a Levenshtine distance calculator
    """
    levenshtine_dict = {'Insertions': 0,
                        'Substitutions': 0, 'Distance Total': 0}
    length_string1 = len(str_1)
    length_string2 = len(str_2)
    distance_counter = 0
    if str_1 and str_2 in leven_on_a_prayer_cache:
        return leven_on_a_prayer_cache[str_1], leven_on_a_prayer_cache[str_2]
    if str_1 == str_2:
        return 0
    if length_string1 == length_string2:
        for index, value_var in enumerate(str_1):
            if str_2[index] != value_var:
                levenshtine_dict['Distance Total'] += 1
                levenshtine_dict['Substitutions'] += 1
                distance_counter += 1
            return distance_counter  # , levenshtine_dict
    elif length_string1 != length_string2:
        if length_string1 > length_string2:
            for index, value_var in enumerate(str_1):
                if index < length_string2:
                    if value_var != str_2[index]:
                        levenshtine_dict['Distance Total'] += 1
                        levenshtine_dict['Substitutions'] += 1
                        distance_counter += 1
                elif index >= length_string2:
                    levenshtine_dict['Distance Total'] += 1
                    levenshtine_dict['Insertions'] += 1
                    distance_counter += 1
            return distance_counter  # , levenshtine_dict
        if length_string2 > length_string1:
            for index, value_var in enumerate(str_2):
                if index < length_string1:
                    if value_var != str_1[index]:
                        levenshtine_dict['Distance Total'] += 1
                        levenshtine_dict['Substitutions'] += 1
                        distance_counter += 1
                elif index >= length_string1:
                    levenshtine_dict['Distance Total'] += 1
                    levenshtine_dict['Insertions'] += 1
                    distance_counter += 1
            return distance_counter  # , levenshtine_dict
    leven_on_a_prayer_cache[str_1] = distance_counter
    leven_on_a_prayer_cache[str_2] = distance_counter


    # return leven_on_a_prayer_cache
#pp(easy_leven("the", "that is correct"))

if __name__ == '__main__':
    pp(easy_leven("the", "that is correct"))