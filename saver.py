from bases import Recette
from json import dumps


def encodage(recette: Recette):
    with open(f'recettes/{recette.nom}.menu', 'w') as file:
        txt = recette.write_json()
        txt['version'] = 1.1
        file.write(dumps(txt))
