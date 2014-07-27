# -*- coding: utf-8 -*-

import sys

from convertisseur import Convertisseur


def convertisseur_cli():
    if len(sys.argv) < 2:
        print("Usage: {} <input>".format(sys.argv[0]))
        sys.exit(-1)
    input_ = sys.argv[1]
    convertisseur = Convertisseur(input_)

    print(input_)
    print('')

    print('Infos')
    print('-----')
    for info in convertisseur.get_infos():
        print('- {}'.format(info))

    print('')
    print('Results')
    print('-------')
    for result in convertisseur.get_results():
        print('- {}'.format(result))


if __name__ == '__main__':
    convertisseur_cli()
