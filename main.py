from pathlib import Path

from programmes.affichage_dev import aff_main_menu


# Todo: traducteur, finir recette_manager, recherche par nom, stock de base (pour liste de course)


def mise_en_place():
    p = Path.cwd()
    for ficher in ('cuisines', 'recettes', 'utilisateurs', 'langues'):
        for f in p.iterdir():
            if str(f.parts[-1]) == ficher:
                break
        else:
            d = p / ficher
            d.mkdir()


aff_main_menu()
print('Fin')
