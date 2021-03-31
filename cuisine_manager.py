from json import dumps
from pathlib import Path
from typing import List
from stock_manager import Ingredient


class UstensileCuisine:
    def __init__(self, nom, nombre):
        self.nom = nom
        self.nombre = nombre

    def write_json(self):
        txt = {'nom': self.nom, 'nombre': self.nombre}
        return txt


class Cuisine:
    def __init__(self, nom: str, ustensiles: List[UstensileCuisine], ingredients: List[Ingredient]):
        self.nom = nom
        self.ustensiles = ustensiles
        self.ingredients = ingredients

    def write_json(self):
        liste_u = []
        for ustensile in self.ustensiles:
            liste_u.append(ustensile.write_json())
        liste_i = []
        for ingredient in self.ingredients:
            liste_i.append(ingredient.write_json())
        texte = {'nom': self.nom}
        return texte


def saver(cuisine: Cuisine):
    with open(f'cuisines/{cuisine.nom}.cuisine.json', mode='w') as file:
        texte = cuisine.write_json()
        file.write(dumps(texte))


def cherche_cuisine():
    p = Path.cwd()
    for f in p.iterdir():
        if str(f.parts[-1]) == 'cuisines':
            cuisines = []
            for c in f.iterdir():
                with open(c) as file:
                    cuisine = []
                    for line in file:
                        cuisine.append(line)
                    cuisines.append(cuisine)
    else:
        p.mkdir()
        return None
