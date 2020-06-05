from tinydb import TinyDB, Query, where
from pprint import pprint

# * TinyDB - Représente ta base de donnée
# * Query - Permet d'interroger ta base de donnée
# * where - Permet d'affiner tes requêtes


# * CRÉATION DE LA BDD ET DE LA TABLE FRUITS
db = TinyDB('db.json')
fruits = db.table('fruits')



# # * INSÉRER DES ITEMS
# fruits.insert({'type': '🍓', 'quantite': 4})
# fruits.insert({'type': '🍊', 'quantite': 1})
# fruits.insert({'type': '🍌', 'quantite': 7})



# # * SÉLECTIONNER DES ITEMS

# # * Récupérer tous les items
# pprint(fruits.all())

# # * Itérer sur chacun des items
# for fruit in fruits:
#     pprint(fruit)

# # * Sélectionner un item en particulier
# # ! 3 façons de faire
# # 1 -Syntaxe longue
# Fruit = Query()
# fraise = fruits.search(Fruit.type == '🍓')
# pprint(fraise)

# # 2 - Syntaxe courte
# fraise = fruits.search(where('type') == '🍓')
# pprint(fraise)

# # 3 - Via le Document ID
# fraise = fruits.get(doc_id=1)
# pprint(fraise)

# # * On peut utiliser des opérateurs logiques et/ou des opérateurs de comparaison pour cibler
# pprint(fruits.search((Fruit.quantite > 1) & (Fruit.quantite < 20)))


# # * METTRE À JOUR UN ITEM
# fruits.update({'quantite': 8}, Fruit.type == '🍓')
# pprint(fruits.all())

# # * SUPPRIMER UN ITEM
# fruits.remove(where('type') == '🍊')
# pprint(fruits.all())

# # * VIDER UNE TABLE
# fruits.truncate()
# pprint(fruits.all())
