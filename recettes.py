from types import Recette, Action, Ingredient, Produit, tj, th, tmin

creusois = Recette('Creusois',
                   [Action('1er melange', 'Melanger', True, 60, 0, 0,
                           [Ingredient('Sucre', 160, 'g', 0, 0, 'saccharose'),
                            Ingredient('Farine', 80, 'g', 0, 0),
                            Ingredient('Noisette', 80, 'g', 0, 0)]),
                    Action('Beurre fondue', 'Fondre', False, 60, 0, tmin(2),
                           [Ingredient('Beurre', 80, 'g', 0, tmin(10))]),
                    Action('2eme melange', 'Melanger', True, 60, 0, 0,
                           [Produit('1er melange'),
                            Produit('Beurre fondue')]),
                    Action('Blanc en neige', 'Battre', True, tmin(10), 0, tmin(20),
                           [Ingredient('Oeuf', 4, 'u', 0, 0)]),
                    Action('Melange finale', 'Melanger', True, tmin(10), 0, tmin(20),
                           [Produit('2eme melange'),
                            Produit('Blanc en neige')]),
                    Action('fin', 'Cuire', False, tmin(30), th(1), tj(5),
                           [Produit('Melange finale')])])
