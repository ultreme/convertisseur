#!/usr/bin/env python

import math

from .misc import (
    conv_1337, conv_sms_grand_pere, conv_langage_sms, conv_rot13, conv_base64,
    conv_pronounced_letters, conv_mega1337, conv_verlant,
)


class Convertissage:
    def __init__(self, base_value, value, output_type, input_type=None):
        self.base_value = base_value
        self.value = value
        self.output_type = output_type
        self.input_type = input_type

    @property
    def comment(self):
        if str(self.base_value) == str(self.value):
            return 'c\'est pareil !'

    def get_line(self):
        comment = self.comment
        if comment:
            comment = '({})'.format(comment)
        parts = [
            self.base_value, self.input_type, 'ca fait', self.value,
            self.output_type, comment
        ]
        return ' '.join([str(part) for part in parts if part is not None])


class Convertisseur:
    def __init__(self, input_value):
        self.input_value = input_value

    @property
    def input_family(self):
        try:
            float(self.input_value.replace(',', '.'))
            return 'number'
        except:
            return 'string'

    def _result(self, value, output_type, input_type=None):
        return Convertissage(self.input_value, value, output_type, input_type)

    @property
    def clean_value(self):
        if self.input_family == 'number':
            value = float(self.input_value.replace(',', '.'))
            if value == int(value):
                return int(value)
            return value
        return str(self.input_value)

    def get_infos(self):
        value = self.clean_value
        family = self.input_family

        infos = []
        if family == 'number':
            infos.append('un nombre')

            if value < 0:
                infos.append('negatif')
            elif value > 0:
                infos.append('positif')
            else:
                infos.append('nul')

            special_numbers = {
                '42': 'la grande reponse a la vie, l\'univers et tout le reste',
                '4242': 'la grande reponse a la vie, l\'univers et tout le '
                'reste, fois 2',
                '1337': 'ca veut dire leet (elite) en langage gamer/hacker',
                '31337': 'ca veut dire elite en langage gamer/hacker',
                '3.1415': 'c\'est pi',
            }
            special_numbers[str(math.pi)] = special_numbers.get('3.1415')
            if str(value) in special_numbers:
                infos.append(special_numbers[str(value)])

            if isinstance(value, int):
                infos.append('sans virgule')
            elif isinstance(value, float):
                infos.append('avec virgule')

        elif family == 'string':
            infos.append('un ensemble de caracteres')
            if value.find(' '):
                infos.append('une phrase contenant des mots')
            else:
                infos.append('un mot')

            cleaned_value = value.lower().strip().replace('.', '')

            special_words = {
                'camembert au lait crew': 'le nom d\'un groupe de copains qui '
                'font de la musique tres super',
                'calc': 'les initials de camembert au lait crew',
            }
            if cleaned_value in special_words:
                infos.append(special_words[cleaned_value])
        else:
            raise NotImplementedError()

        return infos

    def integer_get_results(self):
        value = self.clean_value

        # FIXME add other base conversions
        return [
            self._result(hex(value), 'en hexadecimal', 'en base 10'),
        ]

    def float_get_results(self):
        return []

    def number_get_results(self):
        value = self.clean_value

        # FIXME: add all octets conversions
        # FIXME: add all weight conversions
        results = [
            self._result(value * 1000, 'g', 'kg'),
            self._result(float(value) / 1000, 'kg', 'g'),
            self._result(int(math.ceil(value / 1024)), 'kilo-octets environ',
                         'octets'),
            self._result(int(math.ceil(value / 1024 / 1024)),
                         'mega-octets environ', 'octets'),
            self._result(value, 'kg de plomb', 'kg de plumes'),
            self._result(int(value * 1.6942), 'carottes (ah non enfaite)',
                         'patates'),
            self._result(value * value, 'au carre'),
            self._result(value * value * math.pi, 'de surface de cercle',
                         'de rayon'),
            self._result(value * 4, 'de contour de carre', 'de cote')
        ]
        if isinstance(value, int):
            results += self.integer_get_results()
        elif isinstance(value, float):
            results += self.float_get_results()
        return results

    def string_get_results(self):
        value = self.clean_value
        return [
            self._result(len(value), 'caracteres'),
            self._result(value[::-1], 'a l\'envers'),
            self._result(value[::2], 'un caractere sur deux'),
            self._result(conv_1337(value), 'en 1337'),
            self._result(conv_mega1337(value), 'en mega 1337 de la mort'),
            self._result(conv_sms_grand_pere(value), 'en sms de grand pere'),
            self._result(conv_langage_sms(value), 'en langage sms'),
            self._result(conv_base64(value), 'en base64'),
            self._result(conv_rot13(value), 'en rot13'),
            self._result(conv_pronounced_letters(value),
                         'en prononcant les caracteres'),
            self._result(conv_verlant(value),
                         'en verlant (je suis pas tres fort)'),
        ]

    def common_get_results(self):
        return []

    def get_results(self):
        family = self.input_family

        results = []
        results += self.common_get_results()
        if family == 'number':
            results += self.number_get_results()
        elif family == 'string':
            results += self.string_get_results()
        else:
            raise NotImpementedError()

        return results
