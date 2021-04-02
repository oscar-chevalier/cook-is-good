from json import dumps, loads
from pathlib import Path
from typing import List, Dict
from programmes.stock.stock_manager import IngredientStock, ingredient_creator


class UstensileCuisine:
    def __init__(self, nom, nombre):
        self.nom = nom
        self.nombre = nombre

    def write_json(self):
        txt = {'nom': self.nom, 'nombre': self.nombre}
        return txt


def ustensile_creator(dico: Dict):
    return UstensileCuisine(dico['nom'], dico['nombre'])


class Cuisine:
    def __init__(self, nom: str, ustensiles: List[UstensileCuisine], ingredients: List[IngredientStock]):
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
        texte = {'nom': self.nom, 'ustensiles': liste_u, 'ingredients': liste_i}
        return texte


def saver_de_cuisine(cuisine: Cuisine):
    p = Path.cwd()
    for f in p.iterdir():
        if str(f.parts[-1]) == 'cuisines':
            break
    else:
        d = p / 'cuisines'
        d.mkdir()
        print(str(d))
    with open(f'cuisines/{cuisine.nom}.cuisine.json', mode='w') as file:
        texte = cuisine.write_json()
        file.write(dumps(texte))


def cuisine_opener(nom_cuisine: str):
    p = Path.cwd()
    d = p / 'cuisines'
    for f in p.iterdir():
        if str(f.parts[-1]) == 'cuisines':
            break
    else:
        d.mkdir()
        return None
    for f in d.iterdir():
        if str(f.parts[-1]) == f'{nom_cuisine}.json':
            fichier = ''
            with open(f'cuisines/{nom_cuisine}.json') as file:
                for line in file:
                    fichier += line
            dico = loads(fichier)
            liste_i = []
            for ingredient in dico['ingredients']:
                liste_i.append(ingredient_creator(ingredient))
            liste_u = []
            for ustensile in dico['ustensiles']:
                liste_u.append(ustensile_creator(ustensile))
            return Cuisine(dico['nom'], liste_u, liste_i)


def chercheur_de_cuisines():
    p = Path.cwd()
    p = p / 'cuisines'
    cuisines = []
    for f in p.iterdir():
        if str(f.parts[-1])[-5:] == '.json':
            cuisines.append(str(f.parts[-1][:-5]))
    return cuisines
