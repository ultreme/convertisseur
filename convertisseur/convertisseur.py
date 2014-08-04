#!/usr/bin/env python

from .misc import (
    conv_1337, conv_sms_grand_pere, conv_langage_sms, conv_rot13, conv_base64,
    conv_pronounced_letters, conv_mega1337,
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
        input_type = self.input_type
        if not input_type:
            input_type = ''
        comment = self.comment
        if not comment:
            comment = ''
        else:
            comment = '({})'.format(comment)
        return '{} {} ca fait {} {} {}'.format(self.base_value, input_type,
                                               self.value, self.output_type,
                                               comment)


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
            }
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
            self._result(value / 1024, 'octets', 'kilo-octets environ'),
            self._result(value, 'kilo de plomb', 'kilo de plumes')
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
            self._result(value[::-1], 'en verlant'),
            self._result(value[::2], 'un caractere sur deux'),
            self._result(conv_1337(value), 'en 1337'),
            self._result(conv_mega1337(value), 'en mega 1337 de la mort'),
            self._result(conv_sms_grand_pere(value), 'en sms de grand pere'),
            self._result(conv_langage_sms(value), 'en langage sms'),
            self._result(conv_base64(value), 'en base64'),
            self._result(conv_rot13(value), 'en rot13'),
            self._result(conv_pronounced_letters(value),
                         'en prononcant les caracteres'),
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
