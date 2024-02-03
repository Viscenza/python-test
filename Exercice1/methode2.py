def transform(chain):
    # Convertir les chaînes en listes d'entiers
    list1 = [int(x) for x in chain[0].split(', ')]
    list2 = [int(x) for x in chain[1].split(', ')]

    # Trouver l'intersection des deux listes (entiers communs)
    common_integers = sorted(set(list1) & set(list2))

    # Nom, prénom et classe
    infos_personnelles = "Bar AdjaYacine Master1"

    # Former une nouvelle chaîne en concaténant les entiers et les informations personnelles
    if common_integers:
        nouvelle_chaine = ', '.join(map(str, common_integers))
        resultat_final = f"{nouvelle_chaine}:{infos_personnelles}"
        return resultat_final
    else:
        return None

# Test
if __name__ == "__main__":
    arr1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    out = transform(arr1)
    print(out)  # doit afficher ---> 1, 4, 13:VotreNom VotrePrenom VotreClasse

    arr3 = ["9, 3, 5, 7, 14", "10, 2, 6, 16, 15"]
    out = transform(arr3)
    print(out)  # doit afficher ---> None