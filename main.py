from pathlib import Path

from programmes.stock.stock_manager import IngredientStock
from programmes.bases import Date
from programmes.cuisines.cuisine_manager import saver_de_cuisine, Cuisine, UstensileCuisine
from programmes.affichage_dev import aff_main_menu
from programmes.cuisines.configer import saver_de_config, Config, opener_de_config


# Todo: traducteur, stockage


def mise_en_place():
    p = Path.cwd()
    for ficher in ('cuisines', 'recettes', 'utilisateurs'):
        for f in p.iterdir():
            if str(f.parts[-1]) == ficher:
                break
        else:
            d = p / ficher
            d.mkdir()


mise_en_place()
cuisine = Cuisine('Villecresnes',
                  [UstensileCuisine('plaque de cuisson', 4),
                   UstensileCuisine('four', 1)],
                  [IngredientStock('Riz', 1000, 'g', Date(2022, 1, 1), -1),
                   IngredientStock('Yaourt', 36, 'u', Date(2021, 1, 5), 3600)])
saver_de_cuisine(cuisine)
saver_de_config(Config('Oscar Chevalier', cuisine, ['fr', 'en', 'de']))
opener_de_config('Oscar Chevalier')
aff_main_menu()
