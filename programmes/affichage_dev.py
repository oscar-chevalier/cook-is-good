from typing import List, Tuple

from programmes.recettes.recette_manager import conseiller_recette
from programmes.cuisines.configer import chercheur_de_toutes_les_configs


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


def reponses(texte: str, rep_poss: Tuple, boucle: bool):
    texte += '\n\nreponses : '
    rep = input(texte)
    while rep not in rep_poss and boucle:
        rep = input(texte)
    return rep


def aff_main_menu():
    aff = 'Fichier | a Propos | Configuration\n'
    aff += rectange(50, 10, 'Recettes conseillees', conseiller_recette())
    rep = reponses(aff, ('F', 'P', 'C'), True)
    if rep == 'C':
        aff_configuration()


def aff_utilisateur():
    liste = ['Utilisateurs (supRimer)']
    liste.extend(chercheur_de_toutes_les_configs())
    for i in range(1, len(liste)):
        liste[i] = str(i-1) + ' ' + liste[i]
    aff = rectange(50, 10, 'Utilisateur', liste)
    rep = ''
    while rep != 'Q':
        rep = reponses(aff, (), False)
        if


def aff_configuration():
    aff = rectange(50, 10, 'Configuration', ['[U] : modifier profile Utilisateur'])
    rep = reponses(aff, ('U', 'M'), True)
    if rep == 'U':
        aff_utilisateur()
