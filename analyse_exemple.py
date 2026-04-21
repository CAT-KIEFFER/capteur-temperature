fichier = open("data.txt", "r")

liste_temp = []

for ligne in fichier:

    position = ligne.find("Temp:")

    if position != -1:
        position = position + 5

        while ligne[position] == " ":
            position += 1

        nombre = ""

        while ligne[position].isdigit():
            nombre += ligne[position]
            position += 1

        temp = int(nombre)

        liste_temp.append(temp)

fichier.close()

min_temp = min(liste_temp)
max_temp = max(liste_temp)
moyenne = sum(liste_temp) / len(liste_temp)

print("min:", min_temp)
print("max:", max_temp)
print("moyenne:", moyenne)
print("total:", len(liste_temp))


