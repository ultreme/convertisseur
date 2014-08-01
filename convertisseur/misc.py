# -*- coding: utf-8 -*-

import base64


def replace_string_with_mapping(string, mapping):
    output = ''
    for i in xrange(len(string)):
        found = False
        for k, v in mapping.items():
            if string[i:i + len(k)] == k:
                found = True
                output += str(v)
                break
        if not found:
            output += string[i]
    return output


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
        'o': 0, 'O': 0,
    }
    return replace_string_with_mapping(string, mapping)


def conv_mega1337(string):
    string = string.upper()
    mapping = {
        'A': 4,
        'B': 8,
        'C': '<',
        'D': '|>',
        'E': 3,
        #'F':
        'G': 6,
        'H': '|-|',
        'I': '|',
        'J': '_|',
        'K': '|<',
        'L': '|_',
        'M': '|v|',
        'N': '|\\|',
        'O': 0,
        #'P':
        'Q': 'O,',
        #'R':
        'S': 5,
        'T': 7,
        #'U':
        'V': '\\/',
        'W': '\\/\\/',
        'X': '><',
        #'Y':
        'Z': 2,
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


def conv_pronounced_letters(string):
    mapping = {
        'a': 'ha',
        'b': 'bay',
        'c': 'say',
        'd': 'day',
        'e': 'euh',
        'f': 'ayf',
        'g': 'jay',
        'h': 'ach',
        'i': 'hi',
        'j': 'ji',
        'k': 'ka',
        'l': 'ail',
        'm': 'aim',
        'n': 'ain',
        'o': 'ho',
        'p': 'pay',
        'q': 'ku',
        'r': 'air',
        's': 'aisse',
        't': 'tay',
        'u': 'hu',
        'v': 'vay',
        'x': 'ix',
        'y': 'igrek',
        'z': 'zayd',
        '1': 'un',
        '2': 'deu',
        '3': 'troa',
        '4': 'katr',
        '5': 'sunk',
        '6': 'cice',
        '7': 'cete',
        '8': 'uite',
        '9': 'neuf',
    }
    return replace_string_with_mapping(string, mapping)


# lettre militaire
# braille
# morse
# markhov
# translage bot
