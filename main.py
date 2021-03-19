from recettes import creusois, crepes
from opener import decodage
from saver import encodage
from recipies_manager import lecteur_de_recettes


print(creusois.arbre())
lecteur_de_recettes([creusois, crepes])
