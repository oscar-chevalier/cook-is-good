from recettes import creusois, crepes
from opener import decodage
from saver import encodage
from recipies_manager import lecteur_de_recettes


print(str(creusois))
encodage(creusois)
print(decodage('creusois'))
lecteur_de_recettes([creusois])
print(str(crepes))
print(crepes.arbre())
encodage(crepes)
lecteur_de_recettes([creusois, crepes])
