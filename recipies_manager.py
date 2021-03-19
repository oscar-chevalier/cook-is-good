from typing import List


from bases import Recette, Action


class ArbreProduits:
    def __init__(self, action: Action, enfants: List):
        self.action = action
        self.enfants = enfants

    def aff(self, n):
        aff = 'def' + str(self.action.noms_produit)
        for enfant in self.enfants:
            aff += f'(e : {enfant.aff(n+1)}, {type(enfant)}, {n})'
        return aff

    def decendants(self):
        for enfant in self.enfants:
            self.enfants.extend(enfant.decendants)
        return self.enfants


def optimisateur_recursif(ar: ArbreProduits):
    """Permet de creer l'arbre recursivement"""
    for ing in ar.action.ingredients:
        if ing.ref_produit is not None:
            enf = optimisateur_recursif(ArbreProduits(ing.ref_produit, []))
            ar.enfants.append(enf)
    return ar


def ordonnanceur_recursif(ar: ArbreProduits):
    ordre_actions = []
    for enfant in ar.enfants:
        ordre_actions.extend(ordonnanceur_recursif(enfant))
    ordre_actions.append(ar.action)
    return ordre_actions


def ordonnanceur(roots: List[ArbreProduits]):
    ordre_actions = []
    for root in roots:
        ordre_actions.extend(ordonnanceur_recursif(root))
    return ordre_actions


def og_recursif(n, listes, actions):
    if len(listes[0]) == n:
        return listes
    new_listes = []
    for liste in listes:
        for i in actions:
            if i not in liste:
                new_listes.append(liste + [i])
    return og_recursif(n, new_listes, actions)


def optimisateur_general(ordre_actions: List[Action]):
    print(len(ordre_actions))
    listes = og_recursif(len(ordre_actions), [[]], ordre_actions)
    print(listes)


def optimisateur(recettes: List[Recette]):
    roots = []
    for recette in recettes:
        root = optimisateur_recursif(ArbreProduits(recette.actions[-1], []))
        roots.append(root)
    for root in roots:
        root.decendants()
    ordre_actions = ordonnanceur(roots)
    optimisateur_general(ordre_actions)
    return ordre_actions


def lecteur_de_recettes(recettes: List[Recette]):
    ordre_actions = optimisateur(recettes)
    stade = 0
    print(ordre_actions)
    for action in ordre_actions:
        print(action)
