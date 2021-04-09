from re import match
from typing import List, Tuple

from programmes.recettes.recettes_manager import conseiller_recette
from programmes.cuisines.configer import chercheur_de_toutes_les_configs, supprimer_config, Config, trouveur_de_config, \
    createur_de_config, saver_de_config
from programmes.cuisines.cuisine_manager import cuisine_opener, chercheur_de_cuisines, Cuisine
from programmes.bases import crediter, Date
from programmes.stock.stock_manager import IngredientStock


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
    while (rep not in rep_poss and len(rep_poss) != 0) and boucle:
        rep = input(texte)
    return rep


def aff_main_menu():
    config = trouveur_de_config()
    langue = config.langue.dictionnaire['affichage_dev']
    aff = langue[0]
    r1 = Rectangle(50, 10, langue[1], conseiller_recette(config))
    r2 = Rectangle(50, 10, langue[2], config.cuisine.ingredients_bientot_perimes(0, 8))
    aff += merge_rectangle([r1, r2])
    rep = ''
    while rep != 'Q':
        rep = reponses(aff, ('F', 'P', 'C', 'Q', 'S'), True)
        if rep == 'C':
            config = aff_configuration(config)
        if rep == 'P':
            reponses(Rectangle(50, 10, langue[3], crediter).aff(True), (), False)
        if rep == 'S':
            print('S')
            if config is not None:
                print('C')
                aff_gestion_stock(config)
            else:
                reponses(Rectangle(50, 10, langue[4], [langue[5]]).aff(True), (), False)


def aff_gestion_stock(config: Config):
    rep = ''
    langue = config.langue.dictionnaire['affichage_dev']
    while rep != 'Q':
        rec = Rectangle(50, 12, langue[6], config.cuisine.liste_stock(0, 8))
        rep = reponses(rec.aff(True), (), True)
        reg = match(r'(?P<nom>.+) (?P<nombre>.+) (?P<unite>.+) (?P<jour>\d+)/(?P<mois>\d+)/(?P<annee>\d+)$', rep)
        if reg is not None:
            config.cuisine.add_ingredients(IngredientStock(reg['nom'], int(reg['nombre']), reg['unite'],
                                                           Date(int(reg['jour']), int(reg['mois']), int(reg['annee']))))
            print('ok')


def aff_utilisateur(config: Config):
    rep = ''
    langue = config.langue.dictionnaire['affichage_dev']
    while rep != 'Q':
        liste = [langue[7]]
        utilisateur_actuel = trouveur_de_config()
        liste_utilisateurs = chercheur_de_toutes_les_configs()
        liste.extend(liste_utilisateurs)
        for i in range(1, len(liste)):
            if liste[i] == utilisateur_actuel.nom_utilisateur:
                liste[i] = '-' + str(i - 1) + ' ' + liste[i]
            else:
                liste[i] = ' ' + str(i - 1) + ' ' + liste[i]
        liste.extend([langue[8], langue[9]])
        aff = Rectangle(50, 10, langue[10], liste).aff(True)
        rep = reponses(aff, ('R', 'C', 'U'), False)
        if len(rep) == 2 and int(rep[0]) < len(liste_utilisateurs):
            if rep[1] == 'R':
                aff = Rectangle(100, 2, langue[11], [langue[12]]).aff(True)
                rep2 = reponses(aff, (), False)
                if rep2 == 'O':
                    supprimer_config(liste_utilisateurs[int(rep[0])])
            elif rep[1] == 'U':
                createur_de_config(liste_utilisateurs[int(rep[0])])
        elif rep == 'C':
            nom = input(langue[13])
            aff = [langue[14]]
            liste_cuisines = chercheur_de_cuisines()
            for i, cuis in enumerate(liste_cuisines):
                aff.append(f'{i} {cuis}')
            aff.append(langue[15])
            cuisine = None
            while cuisine is None:
                rec = Rectangle(100, 10, langue[16], aff)
                rep = reponses(rec.aff(True), (), False)
                if rep == 'N':
                    nom_cuisine = input(langue[17])
                    cuisine = Cuisine(nom_cuisine, [], [])
                else:
                    cuisine = cuisine_opener(liste_cuisines[int(rep)])
            config = Config(nom, cuisine, config.langues)
            createur_de_config(config.nom_utilisateur)
            saver_de_config(config)
    config = trouveur_de_config()
    return config


def aff_configuration(config: Config):
    langue = config.langue.dictionnaire['affichage_dev']
    aff = Rectangle(50, 10, langue[18], [langue[19]]).aff(True)
    rep = reponses(aff, ('U', 'M'), True)
    if rep == 'U':
        config = aff_utilisateur(config)
        return config
