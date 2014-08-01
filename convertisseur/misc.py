# -*- coding: utf-8 -*-


def replace_string_with_mapping(string, mapping):
    for k, v in mapping.items():
        string = string.replace(k, str(v))
    return string


def conv_1337(string):
    mapping = {
        'l': 1, 'L': 1,
        'z': 2, 'Z': 2,
        'e': 3, 'E': 3,
        'a': 4, 'A': 4,
        's': 5, 'S': 5,
        'G': 6,
        't': 7, 'T': 7,
        'b': 8, 'B': 8,
        'g': 9,
    }
    return replace_string_with_mapping(string, mapping)


def conv_sms_grand_pere(string):
    string += '...bisous mon grand..papi'
    string = replace_string_with_mapping(string, {
        ' ': '.',
    })
    string = string.upper()
    return string
