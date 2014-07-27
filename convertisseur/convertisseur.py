#!/usr/bin/env python


class Convertissage:
    def __init__(self, value, output_type, input_type=None):
        self.value = value
        self.output_type = output_type
        self.input_type = input_type


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

        infos = []
        if family == 'number':
            infos.append('un nombre')

            if value < 0:
                infos.append('negatif')
            elif value > 0:
                infos.append('positif')
            else:
                infos.append('nul')

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

    def integer_get_results(self):
        value = self.clean_value

        return [
            Convertissage(hex(value), 'en hexadecimal', 'en base 10'),
        ]


    def float_get_results(self):
        return []

    def number_get_results(self):
        value = self.clean_value

        results = [
            Convertissage(value * 1000, 'g', 'kg'),
            Convertissage(value / 1000, 'kg', 'g'),
            Convertissage(value / 1024, 'octets', 'kilo-octets'),
        ]
        if isinstance(value, int):
            results += self.integer_get_results()
        elif isinstance(value, float):
            results += self.float_get_results()
        return results

    def string_get_results(self):
        value = self.clean_value
        return [
            Convertissage(len(value), 'caracteres'),
            Convertissage(value[::-1], 'en verlant'),
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
