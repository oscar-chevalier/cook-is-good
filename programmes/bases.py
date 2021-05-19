from typing import List

nom_scientifique = {'sucre': 'saccharose', 'farine de ble': 'triticum aestivum', 'noisette': 'corylus avellana'}
unites_sing = {'@CS': 'cuilliere à soupe', '@S': 'sachet', '@P': 'pincee'}
unites_plur = {'@CS': 'cuillieres à soupe', '@S': 'sachets', '@P': 'pincees'}


def f_pluriel(nom):
    plur = {'feuille': 's', 'morceau': 'x'}
    mots = nom.strip().lower().split()
    if mots[0] in plur:
        mots[0] += plur[mots[0]]
        return ' '.join(mots)
    return nom + 's'


class Ustensile:
    def __init__(self, nom: str):
        self.nom = nom

    def write_json(self):
        return {'nom': self.nom}


class Date:
    def __init__(self, jour: int, mois: int, annee: int):
        self.annee = annee
        self.mois = mois
        self.jour = jour

    def write_json(self):
        return {'jour': self.jour, 'mois': self.mois, 'annee': self.annee}

    def __str__(self):
        return f'{self.jour}/{self.mois}/{self.annee}'


def date_creator(jour, mois, annee):
    return Date(jour, mois, annee)


def est_plus_proche_que(date1: Date, date2: Date):
    if date1.annee < date2.annee:
        return True
    if date1.mois < date2.mois and date1.annee == date2.annee:
        return True
    if date1.jour < date2.jour and date1.mois == date2.mois and date1.annee == date2.annee:
        return True
    return False


class Produit:
    def __init__(self, nom: str, quantite: int = 0, unite: str = '', temps_min: int = 0, temps_max: int = 0):
        if quantite >= 2 and unite == '@U':
            self.nom_ecriture = f_pluriel(nom)
        else:
            self.nom_ecriture = nom
        self.nom = nom
        self.quantite = quantite
        self.temps_min = temps_min  # en seconde
        self.temps_max = temps_max  # en seconde
        self.unite = unite
        self.ref_produit = None

    def __str__(self):
        if self.quantite == 0:
            return f'{self.nom_ecriture}'
        if self.unite in unites_sing:
            if self.quantite > 1:
                return f'{self.quantite} {unites_plur[self.unite]} de {self.nom_ecriture}'
            return f'{self.quantite} {unites_sing[self.unite]} de {self.nom_ecriture}'
        if self.unite in ('@U', ''):
            if self.quantite > 0:
                return f'{self.quantite} {self.nom_ecriture}'
            return f'{self.nom_ecriture}'
        return f'{self.quantite} {self.unite} de {self.nom_ecriture}'

    def aff(self):
        return self.__str__()

    def write_json(self):
        txt = {'nom': self.nom,
               'quantite': self.quantite,
               'unite': self.unite,
               'temps_min': self.temps_min,
               'temps_max': self.temps_max}
        return txt

    def arbre(self):
        if self.ref_produit is None:
            return f'ar-   {self.nom} ({self.ref_produit}, {type(self.ref_produit)})'
        return f'ar+   {self.nom} ({self.ref_produit}, {type(self.ref_produit)}, {self.ref_produit.noms_produit})'


class Ingredient(Produit):
    def __init__(self, nom: str, quantite: int = 0, unite: str = '', temps_min: int = 0, temps_max: int = 0,
                 nom_scientifique: str = None):
        super().__init__(nom, quantite, unite, temps_min, temps_max)
        if nom_scientifique is None:
            if dans_nom_scientifique(self.nom):
                self.nom_scientifique = create_nom_scientifique(nom)
            else:
                self.nom_scientifique = ''
        else:
            self.nom_scientifique = nom_scientifique

    def write_json(self):
        txt = {'nom': self.nom,
               'quantite': self.quantite,
               'unite': self.unite,
               'temps_min': self.temps_min,
               'temps_max': self.temps_max,
               'nom_scientifique': self.nom_scientifique}
        return txt


def create_nom_scientifique(nom: str):
    return nom_scientifique[nom.lower()]


def dans_nom_scientifique(nom: str):
    return nom.lower() in nom_scientifique


class Action:
    def __init__(self, noms_produit: List, action_effectue: str, attention: bool, temps_estime: int, temps_min: int,
                 temps_max: int, proportionnel: float, ingredients: List, ustensiles=None, commentaires: str = '', lien: str = ''):
        if ustensiles is None:
            ustensiles = []
        self.noms_produit = noms_produit
        self.action_effectue = action_effectue  # Ce que l'on fait (ex. melanger)
        self.attention = attention  # demande
        self.temps_estime = temps_estime  # en seconde
        self.temps_min = temps_min
        self.temps_max = temps_max
        self.proportionnel = proportionnel  # la proportionnallite du temps par rapport au nombre d'ingredient
        self.ingredients = ingredients
        self.produits = self.create_produit()
        self.ustensiles = ustensiles
        self.commentaires = commentaires
        self.lien = lien

    def create_produit(self):
        liste = []
        for n_p in self.noms_produit:
            liste.append(Produit(n_p, 0, '', self.temps_min, self.temps_max))
        return liste

    def __str__(self):
        if self.commentaires != '':
            return self.commentaires + '\n'
        aff = self.action_effectue + ' '
        nbr_ingredients = len(self.ingredients)
        for i, ingredient in enumerate(self.ingredients):
            if i == nbr_ingredients - 2 and nbr_ingredients > 1:
                aff += f'{ingredient.__str__()} et '
            elif i == nbr_ingredients - 1:
                aff += f'{ingredient.__str__()}'
            else:
                aff += f'{ingredient.__str__()}, '
        return aff + '\n'

    def aff_str(self):
        if self.commentaires != '':
            return self.commentaires
        aff = self.action_effectue + ' '
        nbr_ingredients = len(self.ingredients)
        for i, ingredient in enumerate(self.ingredients):
            if i == nbr_ingredients - 2 and nbr_ingredients > 1:
                aff += f'{ingredient.__str__()} et '
            elif i == nbr_ingredients - 1:
                aff += f'{ingredient.__str__()}'
            else:
                aff += f'{ingredient.__str__()}, '
        return aff

    def aff(self):
        txt = {'action': self.action_effectue, 'ingredients': []}
        for ingredient in self.ingredients:
            txt['ingredients'].append(ingredient.aff)
        return txt

    def write_json(self):
        txt = {'nom_produit': self.noms_produit,
               'action_effectue': self.action_effectue,
               'attention': self.attention,
               'temps_estime': self.temps_estime,
               'temps_min': self.temps_min,
               'temps_max': self.temps_max,
               'proportionnel': self.proportionnel,
               'commentaires': self.commentaires,
               'lien': self.lien}
        liste = []
        for ingredient in self.ingredients:
            liste.append(ingredient.write_json())
        txt['ingredients'] = liste
        liste = []
        for ustensile in self.ustensiles:
            liste.append(ustensile.write_json())
        txt['ustensiles'] = liste
        return txt

    def arbre(self):
        aff = f'  {self.noms_produit} :\n'
        for ing in self.ingredients:
            aff += f'{ing.arbre()} ({type(ing)})\n'
        return aff

    def temps(self, multi: float):
        return self.temps_estime + self.temps_estime*(1-multi)*self.proportionnel

x²
class Recette:
    def __init__(self, nom, nbr_personnes: int, actions: List[Action]):
        self.nom = nom
        self.actions = actions
        self.nbr_personnes = nbr_personnes
        produits = {}
        for a, action in enumerate(self.actions):
            for nom_produit in action.noms_produit:
                produits[nom_produit] = a
        for a, action in enumerate(self.actions):
            for i, ing in enumerate(action.ingredients):
                if ing.nom in produits:
                    self.actions[a].ingredients[i].ref_produit = self.actions[produits[ing.nom]]
        self.ingredients = []
        for action in actions:
            for ingredient in action.ingredients:
                if type(ingredient) is Ingredient:
                    self.ingredients.append(ingredient)

    def __str__(self):
        aff = f'{self.nom} :\n'
        for i, action in enumerate(self.actions):
            aff += f'{i} : {action.__str__()}'
        return aff

    def write_json(self):
        liste = []
        for action in self.actions:
            liste.append(action.write_json())
        txt = {'nom': self.nom, 'nbr_p': self.nbr_personnes, 'actions': liste}
        return txt

    def arbre(self):
        aff = f'{self.nom} :\n'
        for action in self.actions:
            aff += action.arbre()
        return aff


class RecetteEvidente(Recette):
    def __init__(self, nom: str, nbr_personnes: int, actions: List[Action]):
        super().__init__(nom, nbr_personnes, actions)


def th(x):
    return x * 3600


def tmin(x):
    return x * 60


def tj(x):
    return th(x) * 24


crediter = ['icons by freepik',
            'Original idea by Marc Chevalier',
            'UI by Maxime Bezot',
            'management by Oscar Chevalier']
