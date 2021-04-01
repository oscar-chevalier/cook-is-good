from opener import ouvreur_des_recettes
from configer import trouveur_de_config


def conseiller_recette():
    config = trouveur_de_config()
    if config is None:
        return []
    recettes = ouvreur_des_recettes()
    recettes_possibles = []
    for recette in recettes:
        for ingredient in recette.ingredients:
            if ingredient not in config.cuisine.ingredients:
                break
        else:
            recettes_possibles.append(recette)
    return recettes_possibles
