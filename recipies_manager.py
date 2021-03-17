from typing import List

from bases import Recette


def optimisateur(recettes: List[Recette]):
    actions = []
    for recette in recettes:
        for action in recette.actions:
            actions.append(action)
    return actions


def lecteur_de_recettes(recettes: List[Recette]):
    actions = optimisateur(recettes)
    stade = 0
    for action in actions:
        print(action)
