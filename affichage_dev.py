from typing import List


def rectange(x, y, nom, texte: List[str]):
    aff = ','
    aff += nom
    aff += '-'*(x-2-len(nom))
    aff += ',\n'
    for yy in y:
        if yy < len(texte):
            aff += '|' + texte[yy] + ' '*(x-2-len(texte[yy])) + '|\n'
        else:
            aff += '|' + ' '*(x-2) + '|\n'
    aff += '\'' + '-'*(x-2) + '\''
    return aff


def aff_main_menu():
    pass
