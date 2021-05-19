from programmes.bases import RecetteEvidente, Action, Ingredient, Ustensile, tmin, tj


RecetteEvidente('separation d\'oeuf',
                [Action(['jaune d\'oeuf', 'blanc d\'oeuf'], 'separer', True, tmin(1), 0, tj(2), 0.9,
                        [Ingredient('oeuf', 1, '@u')],
                        [Ustensile('Bol')])])

RecetteEvidente('fonte du beurre',
                [Action(['beurre fondue'], 'fondre', False, tmin(1), 0, tmin(10), 0,
                        [Ingredient('beurre', 1, 'g')],
                        [Ustensile('Micro-onde')])])
