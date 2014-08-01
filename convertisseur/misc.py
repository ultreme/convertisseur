# -*- coding: utf-8 -*-

import base64


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


def conv_langage_sms(string):
    return replace_string_with_mapping(string, {
        'salut': 'slt',
        'bonjour': 'bjr',
        'ca va': 'sava',
        'comment vas-tu ?': 'sava?',
        'coucou': 'cc',
        'huitre': '8r',
        'saucisson': 'so6on',
        'trois': 3, 'troi': 3, 'troa': 3,
        'eaux': 'o', 'aux': 'o', 'eau': 'o', 'au': 'o',
        'eux': 'e', 'eu': 'e',
        're ': 'r ',
        'est': 'e',
        'rt ': 'r ',
        'lait': 'lai',
    })


def conv_rot13(string):
    mapping = {}
    base = 'abcdefghijklmnopqrstuvwxyz'
    for i in xrange(len(base)):
        mapping[base[i]] = '{}{}'.format(base, base)[i + 13]
    return replace_string_with_mapping(string, mapping)


def conv_base64(string):
    return base64.b64encode(string)


# braille
# morse
# markhov
# translage bot
