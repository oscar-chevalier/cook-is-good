class Date:
    def __init__(self, annee: int, mois: int, jour: int):
        self.annee = annee
        self.mois = mois
        self.jour = jour


class Ingredient:
    def __init__(self, nom: str, quantite: int, date_de_peremption: Date, jours_apres_ouverture: int):
        self.nom = nom
        self.quantite = quantite
        self.date_de_peremption = date_de_peremption
        self.jours_apres_ouverture = jours_apres_ouverture
