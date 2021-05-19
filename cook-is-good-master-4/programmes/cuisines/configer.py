from json import dumps, loads
from pathlib import Path
from typing import List

from programmes.cuisines.cuisine_manager import Cuisine, cuisine_opener
from programmes.langue.langue import langue_opener


class Config:
    def __init__(self, nom_utilisateur: str, cuisine: Cuisine, langues: List[str]):
        self.nom_utilisateur = nom_utilisateur  # Unique
        self.cuisine = cuisine
        self.langues = langues  # Dans l'ordre de preference
        self.langue = langue_opener(langues)

    def write_json(self):
        liste_l = []
        for langue in self.langues:
            liste_l.append(langue)
        texte = {'nom_utilisateur': self.nom_utilisateur,
                 'cuisine': self.cuisine.nom,
                 'langues': liste_l}
        return texte

    def __str__(self):
        aff = self.nom_utilisateur + '\n'
        aff += self.cuisine.__str__() + '\n'
        aff += str(self.langues)
        return aff


def saver_de_config(config: Config):
    p = Path.cwd()
    for f in p.iterdir():
        if str(f.parts[-1]) == 'utilisateurs':
            break
    else:
        d = p / 'utilisateurs'
        d.mkdir()
    for f in p.iterdir():
        if str(f.parts[-1]) == 'utilisateurs':
            with open(f'utilisateurs/{config.nom_utilisateur}.json', mode='w') as file:
                file.write(dumps(config.write_json()))


def opener_de_config(nom_config: str):
    with open(f'utilisateurs/{nom_config}.json') as file:
        texte = ''
        for ligne in file:
            texte += ligne
    dico = loads(texte)
    liste_l = []
    for langue in dico['langues']:
        liste_l.append(langue)
    cuisine = cuisine_opener(dico['cuisine'])
    return Config(dico['nom_utilisateur'], cuisine, liste_l)


def createur_de_config(nom_config: str):
    with open('utilisateurs/config.json', mode='w') as file:
        file.write(dumps({'nom_config': nom_config}))


def trouveur_de_config():
    p = Path.cwd()
    for f in p.iterdir():
        if str(f.parts[-1]) == 'utilisateurs':
            d = p / 'utilisateurs'
            break
    else:
        d = p / 'utilisateurs'
        d.mkdir()
    for f in d.iterdir():
        if str(f.parts[-1]) == 'config.json':
            with open(f'utilisateurs/config.json') as file:
                for ligne in file:
                    dico = loads(ligne)
            if dico['nom_config'] == '':
                return None
            config = opener_de_config(dico['nom_config'])
            return config
    return None


def chercheur_de_toutes_les_configs():
    p = Path.cwd()
    d = p / 'utilisateurs'
    utilisateurs = []
    for f in d.iterdir():
        if str(f.parts[-1])[-5:] == '.json' and str(f.parts[-1]) != 'config.json':
            utilisateurs.append(str(f.parts[-1])[:-5])
    return utilisateurs


def supprimer_config(nom_config: str):
    p = Path.cwd()
    nom_config += '.json'
    p = p / 'utilisateurs' / nom_config
    print(str(p))
    p.unlink()
