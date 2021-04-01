from typing import List, Tuple

from recette_manager import conseiller_recette


def rectange(x, y, nom, texte: List[str]):
    aff = ',['
    aff += nom
    aff += ']' + '-'*(x-4-len(nom))
    aff += ',\n'
    for yy in range(y):
        if yy < len(texte):
            aff += '|' + texte[yy] + ' '*(x-2-len(texte[yy])) + '|\n'
        else:
            aff += '|' + ' '*(x-2) + '|\n'
    aff += '\'' + '-'*(x-2) + '\''
    return aff


def reponses(texte: str, rep_poss: Tuple):
    texte += '\n\nreponses : '
    rep = ''
    while rep not in rep_poss:
        input(texte)
    return rep


def aff_main_menu():
    aff = 'Fichier | a Propos | Configuration\n'
    aff += rectange(50, 10, 'Recettes conseillees', conseiller_recette())
    rep = reponses(aff, ('C', 'P', 'C'))
    if rep == 'C':
        aff_configuration()


def aff_configuration():
    aff = rectange(50, 10, 'Configuration', ['[U] : modifier profile Utilisateur'])
    rep = reponses(aff, ('U', 'M'))
    if rep == 'U':
        pass
