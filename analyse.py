fichier = open("data.txt", "r")

liste_temp = []

for ligne in fichier:

    position = ligne.find("Temp")

    if position == -1:
        print("pas trouvé")
    else:
        position = position + 5

        nombre = ""

        while ligne[position] == " ":
            position += 1

        while position < len(ligne) and ligne[position].isdigit():
            nombre += ligne[position]
            position += 1

        if nombre == "":
            print("pas de valeur")
        else:
            temp = int(nombre)
            liste_temp.append(temp)

fichier.close()

print("min:", min(liste_temp))
print("max:", max(liste_temp))
print("moyenne:", sum(liste_temp) / len(liste_temp))
