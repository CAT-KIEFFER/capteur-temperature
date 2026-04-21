fichier = open("data.txt", "r")

for ligne in fichier:

    position = ligne.find("Temp")

    if position == -1:
        print("pas trouver")
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
            print("temp:", temp)

fichier.close()
