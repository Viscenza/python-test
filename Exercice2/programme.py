""" Voici une version alternative du programme en utilisant des boucles et des conditions :"""

# Création de lst1
lst1 = []
for i in range(1200, 2000, 135):
    lst1.append(i)

# Création de lst2
lst2 = []
for i in lst1:
    if i % 2 == 0:
        lst2.append(i * 2)

# Création de o et e
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
o = []
e = []
for x in numbers:
    if x % 2 == 0:
        o.append(x)
    else:
        e.append(x)

# Affichage des listes
print(lst1)
print(lst2)
print(o)
print(e)
