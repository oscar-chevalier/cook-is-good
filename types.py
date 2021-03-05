# from typing import List

nom_scientifique = {'sucre': 'saccharose', 'farine de ble': 'triticum aestivum', 'noisette': 'corylus avellana'}


class Produit:
    def __init__(self, nom: str, quantite: int = 0, unite: str = '', temps_min: int = 0, temps_max: int = 0):
        self.nom = nom
        self.quantite = quantite
        self.temps_min = temps_min  # en seconde
        self.temps_max = temps_max  # en seconde
        self.unite = unite

    def __str__(self):
        return f'{self.quantite} {self.unite} {self.nom}'


class Ingredient(Produit):
    def __init__(self, nom, quantite: int = 0, unite: str = '', temps_min: int = 0, temps_max: int = 0,
                 nom_scientifique: str = None):
        super().__init__(nom, quantite, unite, temps_min, temps_max)
        if nom_scientifique is None:
            if dans_nom_scientifique(self.nom):
                self.nom_scientifique = create_nom_scientifique(nom)
            else:
                self.nom_scientifique = ''
        else:
            self.nom_scientifique = nom_scientifique


def create_nom_scientifique(nom: str):
    return nom_scientifique[nom.lower()]


def dans_nom_scientifique(nom: str):
    return nom.lower() in nom_scientifique


class Action:
    def __init__(self, nom_produit, action_effectue: str, attention: bool, temps_estime: int, temps_min: int,
                 temps_max: int, ingredients):
        self.ingredients = ingredients
        self.action_effectue = action_effectue  # Ce que l'on fait (ex. melanger)
        self.attention = attention  # demande
        self.temps_estime = temps_estime  # en seconde
        self.nom_produit = nom_produit
        self.temps_min = temps_min
        self.temps_max = temps_max
        self.produit = self.create_produit()

    def create_produit(self):
        quantite = 0
        unite = ''
        for ingredient in self.ingredients:
            quantite += ingredient.quantite
            if unite != ingredient.unite:
                unite = None
                break
            unite = ingredient.unite
        return Produit(self.nom_produit, quantite, unite, self.temps_min, self.temps_max)

    def __str__(self):
        aff = self.action_effectue
        for ingredient in self.ingredients:
            aff += f' {ingredient.__str__()}, '
        return aff + '\n'


class Recette:
    def __init__(self, nom, actions):
        self.nom = nom
        self.actions = actions
        produits = {}
        for action in actions:
            produits[action.nom_produit] = action.produit
            for i in range(len(action.ingredients)):
                ing = action.ingredients[i]
                if ing.nom in produits:
                    action.ingredients[i] = produits[ing.nom]
        print(produits)
        for action in actions:
            print(action.ingredients)
            print(action.produit)

    def __str__(self):
        aff = f'{self.nom} :\n'
        for i, action in enumerate(self.actions):
            aff += f'{i} : {action.__str__()}'
        return aff


def th(x):
    return x * 3600


def tmin(x):
    return x * 60


def tj(x):
    return th(x) * 24
