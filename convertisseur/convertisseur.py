#!/usr/bin/env python

import random

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
        type_ = type(value)

        infos = []
        if family == 'number':
            infos.append('un nombre')
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
        else:
            raise NotImplementedError()

        return infos

    def number_get_results(self):
        value = self.clean_value
        type_ = type(value)
        return [
            {'in': 'kg', 'out': 'g', 'value': value * 1000},
            {'in': 'g', 'out': 'kg', 'value': value / 1000},
            {'in': 'octets', 'out': 'kilo-octets', 'value': value / 1024 },
        ]

    def string_get_results(self):
        value = self.clean_value
        type_ = type(value)
        return [
            {'out': 'caracteres de long', 'value': len(value)},
            {'out': 'en verlant', 'value': value[::-1]},
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
