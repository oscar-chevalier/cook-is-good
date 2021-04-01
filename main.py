from recettes import creusois, crepes
from stock_manager import Ingredient
from bases import Date
from opener import decodage
from saver import encodage
from recipies_manager import lecteur_de_recettes
from cuisine_manager import saver_de_cuisine, Cuisine, UstensileCuisine
from affichage_dev import aff_main_menu
from configer import saver_de_config, Config, opener_de_config

cuisine = Cuisine('Villecresnes',
                  [UstensileCuisine('plaque de cuisson', 4),
                   UstensileCuisine('four', 1)],
                  [Ingredient('Riz', 1000, 'g', Date(2022, 1, 1), -1),
                   Ingredient('Yaourt', 36, 'u', Date(2021, 1, 5), 3600)])
saver_de_cuisine(cuisine)
saver_de_config(Config('Oscar Chevalier', cuisine, ['fr', 'en', 'de']))
opener_de_config('Oscar Chevalier')
aff_main_menu()
