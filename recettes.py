from bases import Recette, Action, Ingredient, Produit, tj, th, tmin

creusois = Recette('Creusois',
                   [Action('le 1er melange', 'Melanger', True, 60, 0, 0,
                           [Ingredient('sucre', 160, 'g', 0, 0, 'saccharose'),
                            Ingredient('farine', 80, 'g', 0, 0),
                            Ingredient('noisette', 80, 'g', 0, 0)]),
                    Action('le beurre fondue', 'Fondre', False, 60, 0, tmin(2),
                           [Ingredient('beurre', 80, 'g', 0, tmin(10))]),
                    Action('le 2eme melange', 'Melanger', True, 60, 0, 0,
                           [Produit('le 1er melange'),
                            Produit('le beurre fondue')]),
                    Action('les blancs en neige', 'Battre', True, tmin(10), 0, tmin(20),
                           [Ingredient('oeuf', 4, 'u', 0, 0)]),
                    Action('le melange finale', 'Melanger', True, tmin(10), 0, tmin(20),
                           [Produit('le 2eme melange'),
                            Produit('les blancs en neige')]),
                    Action('fin', 'Cuire', False, tmin(30), th(1), tj(5),
                           [Produit('le melange final')])])
