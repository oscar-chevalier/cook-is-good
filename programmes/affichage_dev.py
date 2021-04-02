from typing import List, Tuple

from programmes.recettes.recettes_manager import conseiller_recette
from programmes.cuisines.configer import chercheur_de_toutes_les_configs, supprimer_config, Config
from programmes.cuisines.cuisine_manager import cuisine_opener
from programmes.bases import crediter


class Rectangle:
    def __init__(self, x, y, nom, texte: List[str]):
        self.x = x
        self.y = y
        self.nom = nom
        self.texte = texte

    def aff_ligne(self, ligne: int):
        if ligne == 0:
            aff = ',['
            aff += self.nom
            aff += ']' + '-' * (self.x - 4 - len(self.nom))
            aff += ','
            return aff
        elif ligne == self.y:
            return '\'' + '-' * (self.x - 2) + '\''
        if ligne-1 < len(self.texte):
            return '|' + self.texte[ligne-1] + ' ' * (self.x - 2 - len(self.texte[ligne-1])) + '|'
        return '|' + ' ' * (self.x - 2) + '|'

    def aff(self, retour_a_la_ligne: bool):
        aff = self.aff_ligne(0)
        if retour_a_la_ligne:
            aff += '\n'
        for yy in range(1, self.y):
            aff += self.aff_ligne(yy)
            if retour_a_la_ligne:
                aff += '\n'
        aff += self.aff_ligne(self.y)
        return aff


def merge_rectangle(liste_rec: list):
    maxi = 0
    for rec in liste_rec:
        maxi = max(rec.y, maxi)
    aff = ''
    for i in range(maxi+1):
        for rec in liste_rec:
            aff += rec.aff_ligne(i)
        aff += '\n'
    return aff


def reponses(texte: str, rep_poss: Tuple, boucle: bool):
    texte += '\n\nreponses : '
    rep = input(texte)
    while rep not in rep_poss and boucle:
        rep = input(texte)
    return rep


def aff_main_menu():
    aff = 'Fichier | a Propos | Configuration\n'
    r1 = Rectangle(50, 10, 'Recettes conseillees', conseiller_recette())
    r2 = Rectangle(50, 10, 'Produits bientot perimes', [])
    aff += merge_rectangle([r1, r2])
    rep = ''
    while rep != 'Q':
        rep = reponses(aff, ('F', 'P', 'C', 'Q'), True)
        if rep == 'C':
            aff_configuration()
        if rep == 'P':
            reponses(Rectangle(50, 10, 'A propos', crediter).aff(True), (), False)


def aff_utilisateur():
    liste = ['Utilisateurs (supRimer)']
    liste_utilisateurs = chercheur_de_toutes_les_configs()
    liste.extend(liste_utilisateurs)
    for i in range(1, len(liste)):
        liste[i] = str(i-1) + ' ' + liste[i]
    liste.extend(['commandes :', 'Creer utilisateur'])
    aff = Rectangle(50, 10, 'Utilisateur', liste).aff(True)
    rep = ''
    while rep != 'Q':
        rep = reponses(aff, (), False)
        print(int(rep[0])+1, len(liste), rep[1], int(rep[0]) < len(liste))
        if int(rep[0]) < len(liste_utilisateurs):
            if rep[1] == 'R':
                supprimer_config(liste_utilisateurs[int(rep[0])+1])
                print('suppr')
        if rep == 'C':
            nom = input('nom_utilisateur : ')
            cuisine = cuisine_opener(input('nom_cuisine : '))
            Config(nom, cuisine, ['fr'])


def aff_configuration():
    aff = Rectangle(50, 10, 'Configuration', ['[U] : modifier profile Utilisateur']).aff(True)
    rep = reponses(aff, ('U', 'M'), True)
    if rep == 'U':
        aff_utilisateur()
