#!/usr/bin/env python


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
        if not comment:
            comment = ''
        else:
            comment = '({})'.format(comment)
        return '{} {} ca fait {} {} {}'.format(self.base_value, self.input_type,
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
