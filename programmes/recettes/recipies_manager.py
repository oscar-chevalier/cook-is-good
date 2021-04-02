from typing import List


from programmes.bases import Recette, Action, Ingredient


class ArbreProduits:
    def __init__(self, action: Action, enfants: List):
        self.action = action
        self.enfants = enfants
        self.decendants = []

    def aff(self, n):
        aff = 'def' + str(self.action.noms_produit)
        for enfant in self.enfants:
            aff += f'(e : {enfant.aff(n+1)}, {type(enfant)}, {n})'
        return aff

    def f_decendants(self):
        self.decendants.extend(self.enfants)
        for enfant in self.enfants:
            self.decendants.extend(enfant.f_decendants())
        return self.decendants


def optimisateur_recursif(ar: ArbreProduits):
    """Permet de creer l'arbre recursivement"""
    for ing in ar.action.ingredients:
        if ing.ref_produit is not None:
            enf = optimisateur_recursif(ArbreProduits(ing.ref_produit, []))
            ar.enfants.append(enf)
    return ar


def denombrement(n, m):
    if n == 1:
        n_listes = []
        for i in range(m):
            n_listes.append([i])
        return n_listes
    listes = denombrement(n - 1, m)
    n_listes = []
    for liste in listes:
        for i in range(m):
            if i not in liste:
                n_listes.append((liste + [i]))
    return n_listes


def og_recursif(root):
    if len(root.enfants) == 0:
        return [[]]
    listes = []
    for enfant in root.enfants:
        listes.extend(og_recursif(enfant))
    n_listes = []
    for liste in listes:
        poss = denombrement(len(root.enfants), len(root.enfants))
        for pos in poss:
            liste_t = []
            for n in pos:
                liste_t.append(root.enfants[n])
            n_listes.append(liste + liste_t)
    return n_listes


def converter(roots: List[List[List[ArbreProduits]]]) -> List[List[List[Action]]]:
    actions_possibles = []
    for root in roots:
        r = []
        for liste in root:
            l = []
            for ap in liste:
                l.append(ap.action)
            r.append(l)
        actions_possibles.append(r)
    return actions_possibles


def ordonnanceur(actions_possibles: List[List[List[Action]]]):
    print(actions_possibles)
    ingredients = []
    for _ in range(len(actions_possibles)):
        ingredients.append([])
    produits = []
    for _ in range(len(actions_possibles)):
        produits.append([])
    for nr, recette in enumerate(actions_possibles):
        for liste_actions in recette:
            for action in liste_actions:
                for ingredient in action.ingredients:
                    if ingredient.nom not in ingredients[nr] and type(ingredient) is Ingredient:
                        ingredients[nr].append(ingredient.nom)
                for produit in action.produits:
                    if produit.nom not in produits[nr]:
                        produits[nr].append(produit.nom)
    ingredients_en_commun = {}
    ingredients_deja_vu = {}
    for i, recette in enumerate(ingredients):
        for ingredient in recette:
            if ingredient not in ingredients_deja_vu:
                ingredients_deja_vu[ingredient] = [i]
            else:
                ingredients_deja_vu[ingredient].append(i)


def optimisateur(recettes: List[Recette]):
    roots = []
    for recette in recettes:
        root = optimisateur_recursif(ArbreProduits(recette.actions[-1], []))
        roots.append(root)
    for root in roots:
        root.f_decendants()
    liste_roots = []
    for root in roots:
        liste_roots.append(og_recursif(root))
    actions_possibles = converter(liste_roots)
    ordre_actions = ordonnanceur(actions_possibles)
    return ordre_actions


def lecteur_de_recettes(recettes: List[Recette]):
    ordre_actions = optimisateur(recettes)
    stade = 0
    print(ordre_actions)
    for action in ordre_actions:
        print(action)
