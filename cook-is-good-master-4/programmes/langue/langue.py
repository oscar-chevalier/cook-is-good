from pathlib import Path
from typing import Dict, List
from json import loads, dumps


from programmes.langue.langues import liste_langues


class Langue:
    def __init__(self, langue: str, dictionnaire: Dict):
        self.langue = langue
        self.dictionnaire = dictionnaire


def langue_opener(langues: List[str]) -> Langue:
    p = Path.cwd()
    d = p / 'langues'
    for f in p.iterdir():
        if str(f.parts[-1]) == 'langues':
            break
    else:
        d.mkdir()
    langues_disponibles = []
    for f in p.iterdir():
        if str(f.parts[-1])[:-5] in langues:
            langues_disponibles.append(str(f.parts[-1])[:-5])
    for langue in langues:
        for langue_disponible in langues_disponibles:
            if langue == langue_disponible:
                dico = ''
                with open(d / f'{langue_disponible}.json') as file:
                    for ligne in file:
                        dico += ligne.strip()
                return Langue(langue, loads(dico))
    for langue in langues:
        if langue in liste_langues:
            return Langue(langue, liste_langues[langue])


def langue_saver(la: str, mots: Dict):
    langue = langue_opener([la])
    for key, value in mots.items():
        langue.dictionnaire[key] = value
    p = Path.cwd()
    d = p / 'langues'
    with open(d / f'{la}.json', mode='w') as file:
        file.write(dumps(langue.dictionnaire))
