from json import dumps, loads
from pathlib import Path
from typing import List, Dict


from programmes.stock.stock_manager import IngredientStock, ingredient_creator
from programmes.bases import est_plus_proche_que


class UstensileCuisine:
    def __init__(self, nom, nombre):
        self.nom = nom
        self.nombre = nombre

    def write_json(self):
        txt = {'nom': self.nom, 'nombre': self.nombre}
        return txt

    def __str__(self):
        return f'{self.nom} {self.nombre}'


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

    def add_ingredients(self, ingredients: IngredientStock):
        self.ingredients.append(ingredients)

    def liste_stock(self, debut: int, fin: int):
        liste = []
        for ing in self.ingredients[debut:fin]:
            liste.append(str(ing))
        return liste

    def __str__(self):
        aff = self.nom + '\nUstensiles :\n'
        for ust in self.ustensiles:
            aff += str(ust) + '\n'
        aff += 'Ingredients :\n'
        for ing in self.ingredients:
            aff += str(ing) + '\n'
        return aff

    def ingredients_bientot_perimes(self, d, f):
        self.ingredients = sort_ingredients(self.ingredients)
        liste = []
        for ingredient in self.ingredients[d:f]:
            liste.append(str(ingredient))
        return liste


def sort_ingredients(liste_ingredient: List[IngredientStock]):
    def fusion(tab1, tab2):
        tabf = []
        l1 = len(tab1)
        l2 = len(tab2)
        n1 = 0
        n2 = 0
        while True:
            if n1 < l1 and n2 < l2:
                if est_plus_proche_que(tab1[n1].date_de_peremption, tab2[n2].date_de_peremption):
                    tabf.append(tab1[n1])
                    n1 += 1
                else:
                    tabf.append(tab2[n2])
                    n2 += 1
            elif n1 >= l1:
                tabf.extend(tab2[n2:])
                return tabf
            else:
                tabf.extend(tab1[n1:])
                return tabf

    def tri_fusion(tableau):
        le = len(tableau)
        if le <= 1:
            return tableau
        return fusion(tri_fusion(tableau[:le // 2]), tri_fusion(tableau[le // 2:]))

    return tri_fusion(liste_ingredient)


def cuisine_saver(cuisine: Cuisine):
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
        if str(f.parts[-1]) == f'{nom_cuisine}.cuisine.json':
            fichier = ''
            with open(f'cuisines/{nom_cuisine}.cuisine.json') as file:
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


def chercheur_de_cuisines() -> List[str]:
    p = Path.cwd()
    p = p / 'cuisines'
    cuisines = []
    for f in p.iterdir():
        if str(f.parts[-1])[-5:] == '.json':
            cuisines.append(str(f.parts[-1][:-13]))
    return cuisines
