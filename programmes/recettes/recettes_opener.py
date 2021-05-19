from json import loads
from pathlib import Path
from typing import List, Dict
from programmes.bases import Recette, Action, Produit, Ingredient, Ustensile
from programmes.recettes.recettes import recettes_preinstallees


def ingredient_produit(txt: Dict):
    if len(txt) == 5:
        return Produit(txt['nom'],
                       txt['quantite'],
                       txt['unite'],
                       txt['temps_min'],
                       txt['temps_max'])
    return Ingredient(txt['nom'],
                      txt['quantite'],
                      txt['unite'],
                      txt['temps_min'],
                      txt['temps_max'],
                      txt['nom_scientifique'])


def ustensile_f(txt: Dict):
    return Ustensile(txt['nom'])


def action_f(txt: Dict):
    ingredients = []
    ustensiles = []
    for ingredient in txt['ingredients']:
        ingredients.append(ingredient_produit(ingredient))
    for ustensile in txt['ustensiles']:
        ustensiles.append(ustensile_f(ustensile))
    return Action(txt['nom_produit'],
                  txt['action_effectue'],
                  txt['attention'],
                  txt['temps_estime'],
                  txt['temps_min'],
                  txt['temps_max'],
                  txt['proportionnel'],
                  ingredients,
                  ustensiles,
                  txt['commentaires'])


def version_1_0(text: List[Dict]):
    text = text[0]
    actions = []
    for action in text['actions']:
        actions.append(action_f(action))
    recette = Recette(text['nom'], -1, actions)
    return recette


def version_1_1(text: List[Dict]):
    text = text[0]
    actions = []
    for action in text['actions']:
        actions.append(action_f(action))
    recette = Recette(text['nom'], text['nbr_p'], actions)
    return recette


def decodage(recette: str):
    for recet in recettes_preinstallees:
        if recet.nom == recette:
            return recet
    with open('recettes/' + recette + '.menu') as file:
        text = []
        version = 0
        for ligne in file:
            dictionnaire = loads(ligne)
            if 'version' in dictionnaire:
                version = float(dictionnaire['version'])
            text.append(dictionnaire)
    if version == 1.0:
        return version_1_0(text)
    if version == 1.1:
        return version_1_1(text)


def ouvreur_des_recettes():
    p = Path.cwd()
    recettes = []
    for f in p.iterdir():
        if str(f.parts[-1])[-5:] == '.menu':
            recettes.append(decodage(str(f.parts[-1])))
    recettes.extend(recettes_preinstallees)
    return recettes
