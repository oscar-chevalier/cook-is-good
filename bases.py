from typing import List

nom_scientifique = {'sucre': 'saccharose', 'farine de ble': 'triticum aestivum', 'noisette': 'corylus avellana'}


def f_pluriel(nom):
    mots = nom.strip().lower().split()
    if mots[0] in ('feuille', 'morceau'):
        mots[0] += 's'
        return ' '.join(mots)
    return nom + 's'


class Produit:
    def __init__(self, nom: str, quantite: int = 0, unite: str = '', temps_min: int = 0, temps_max: int = 0):
        if quantite >= 2 and unite == 'u':
            self.nom = f_pluriel(nom)
        else:
            self.nom = nom
        f_pluriel(nom)
        self.quantite = quantite
        self.temps_min = temps_min  # en seconde
        self.temps_max = temps_max  # en seconde
        self.unite = unite

    def __str__(self):
        if self.quantite == 0:
            return f'{self.nom}'
        if self.unite in ('u', ''):
            if self.quantite > 0:
                return f'{self.quantite} {self.nom}'
            return f'{self.nom}'
        return f'{self.quantite} {self.unite} de {self.nom}'

    def write_json(self):
        txt = {'nom': self.nom,
               'quantite': self.quantite,
               'unite': self.unite,
               'temps_min': self.temps_min,
               'temps_max': self.temps_max}
        return txt


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
    def __init__(self, nom_produit: str, action_effectue: str, attention: bool, temps_estime: int, temps_min: int,
                 temps_max: int, ingredients: List):
        self.nom_produit = nom_produit
        self.action_effectue = action_effectue  # Ce que l'on fait (ex. melanger)
        self.attention = attention  # demande
        self.temps_estime = temps_estime  # en seconde
        self.temps_min = temps_min
        self.temps_max = temps_max
        self.ingredients = ingredients
        self.produit = self.create_produit()

    def create_produit(self):
        return Produit(self.nom_produit, 0, '', self.temps_min, self.temps_max)

    def __str__(self):
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

    def write_json(self):
        txt = {'nom_produit': self.nom_produit,
               'action_effectue': self.action_effectue,
               'attention': self.attention,
               'temps_estime': self.temps_estime,
               'temps_min': self.temps_min,
               'temps_max': self.temps_max}
        liste = []
        for ingredient in self.ingredients:
            liste.append(ingredient.write_json())
        txt['ingredients'] = liste
        return txt


class Recette:
    def __init__(self, nom, actions: List[Action]):
        self.nom = nom
        self.actions = actions
        produits = {}
        for action in actions:
            produits[action.nom_produit] = action.produit
            for i in range(len(action.ingredients)):
                ing = action.ingredients[i]
                if ing.nom in produits:
                    action.ingredients[i] = produits[ing.nom]

    def __str__(self):
        aff = f'{self.nom} :\n'
        for i, action in enumerate(self.actions):
            aff += f'{i} : {action.__str__()}'
        return aff

    def write_json(self):
        liste = []
        for action in self.actions:
            liste.append(action.write_json())
        txt = {'nom': self.nom, 'actions': liste}
        return txt


def th(x):
    return x * 3600


def tmin(x):
    return x * 60


def tj(x):
    return th(x) * 24
