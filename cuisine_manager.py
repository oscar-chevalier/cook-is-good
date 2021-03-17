from typing import List


class UstensileCuisine:
    def __init__(self, nom, nombre):
        self.nom = nom
        self.nombre = nombre


class Cuisine:
    def __init__(self, nom: str, ustensiles: List[UstensileCuisine]):
        self.nom = nom
        self.ustensiles = ustensiles
