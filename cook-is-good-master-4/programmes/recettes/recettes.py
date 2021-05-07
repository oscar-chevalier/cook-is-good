from programmes.bases import Recette, Action, Ingredient, Produit, Ustensile, tj, th, tmin


def lait(volume):
    return Ingredient('lait', volume, 'mL', 0, tmin(10))


def sucre(masse, unite):
    return Ingredient('sucre', masse, unite, 0, 0)


def casserole():
    return Ustensile('casserole')


def oeufs(nbr):
    return Ingredient('oeuf', nbr, '@U')


creusois = Recette('Creusois', 2,
                   [Action(['le 1er melange'], 'Melanger', True, 60, 0, 0, 0,
                           [Ingredient('sucre', 80, 'g', 0, 0, 'saccharose'),
                            Ingredient('farine', 80, 'g', 0, 0),
                            Ingredient('noisette', 80, 'g', 0, 0)]),
                    Action(['le beurre fondue'], 'Fondre', False, 60, 0, tmin(2), 0.5,
                           [Ingredient('beurre', 80, 'g', 0, tmin(10))]),
                    Action(['le 2eme melange'], 'Melanger', True, 60, 0, 0, 0.1,
                           [Produit('le 1er melange'),
                            Produit('le beurre fondue')]),
                    Action(['blancs d\'oeufs', 'jaunes d\'oeufs'], 'Separer', True, tmin(2), 0, th(1), 0.2,
                           [oeufs(4)]),
                    Action(['les blancs en neige'], 'Battre', True, tmin(10), 0, tmin(20), 1,
                           [Ingredient('blancs d\'oeuf', 4, '@U', 0, 0)]),
                    Action(['le melange finale'], 'Melanger', True, tmin(10), 0, tmin(20), 0.2,
                           [Produit('le 2eme melange'),
                            Produit('les blancs en neige')],),
                    Action(['fin'], 'Cuire', False, tmin(30), th(1), tj(5), 0,
                           [Produit('le melange finale')])])

crepes = Recette('Crepes', 4,
                 [Action(['le beurre fondue'], 'Fondre', False, 60, 0, tmin(5), 0.2,
                         [Ingredient('beurre', 50, 'g', 0, tmin(10))],
                         [Ustensile('Micro-onde'),
                          Ustensile('Bol')]),
                  Action(['le lait tiede'], 'Chauffer', False, tmin(5), 0, tmin(10), 0,
                         [lait(450)],
                         [casserole()]),
                  Action(['le 1er melange'], 'Melanger', True, 120, 0, 0, 0,
                         [sucre(2, '@CS'),
                          Ingredient('sel', 1, '@P', 0, 0),
                          Ingredient('farine tamisée', 250, 'g', 0, 0)],
                         [Ustensile('Saladier')]),
                  Action(['le 2eme melange'], 'Ajouter', True, tmin(5), 0, 0, 1,
                         [oeufs(4),
                          Produit('le beurre fondue'),
                          Produit('le lait tiede'),
                          Produit('le 1er melange')],
                         [Ustensile('Saladier')],
                         'Ajouter le beurre fondue et doucement le lait'),
                  Action(['le 3eme melange'], 'Ajouter', True, tmin(5), tmin(30), 0, 0,
                         [Ingredient('biere', 100, 'mL', 0, 0),
                          Ingredient('vanille', 1, '@S', 0, 0),
                          Produit('le 2eme melange')],
                         [Ustensile('Saladier')]),
                  Action(['fin'], 'Cuire', True, tmin(15), 0, tj(7), 1,
                         [Produit('le 3eme melange')],
                         [Ustensile('Poile')])])

gnocchis_a_la_creme_fraiche = Recette('Gnocchis_a_la_creme_fraiche', 2,
                                      [Action(['gnocchis_cruits'], 'Cuire', False, tmin(5), 0, tmin(10), 0.2,
                                              [Ingredient('gnocchis', 200, 'g')],
                                              [Ustensile('Poile'),
                                               Ustensile('Plaque de cuisson')]),
                                       Action(['fin'], 'Ajouter', True, 30, 0, tmin(5), 0.2,
                                              [Ingredient('craime fraiche', 10, 'cL')],
                                              [Ustensile('Poile')])])

recettes_preinstallees = [crepes, creusois, gnocchis_a_la_creme_fraiche]
