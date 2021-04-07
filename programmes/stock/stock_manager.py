from typing import Dict

from programmes.bases import Date, date_creator


class IngredientStock:
    def __init__(self, nom: str, quantite: int, unite: str, date_de_peremption: Date, jours_apres_ouverture: int = -1):
        self.nom = nom
        self.quantite = quantite
        self.unite = unite
        self.date_de_peremption = date_de_peremption
        self.jours_apres_ouverture = jours_apres_ouverture

    def write_json(self):
        return {'nom': self.nom, 'quantite': self.quantite, 'unite': self.unite,
                'ddp': self.date_de_peremption.write_json(),
                'jao': self.jours_apres_ouverture}

    def __str__(self):
        return f'{self.nom} : {self.quantite} {self.unite}, {str(self.date_de_peremption)}'


def ingredient_creator(dico: Dict):
    date_de_peremption = date_creator(dico['ddp']['jour'], dico['ddp']['mois'], dico['ddp']['annee'])
    return IngredientStock(dico['nom'], dico['quantite'], dico['unite'],
                           date_de_peremption, dico['jao'])
