fichier = open("data.txt", "r")

compteur_low = 0
compteur_warning = 0
total = 0

for ligne in fichier:
    total += 1

    if "LOW TEMP" in ligne:
        compteur_low += 1
    if "WARNING" in ligne:
        compteur_warning += 1

fichier.close()

print("total des relevés: ", total)
print("total low: ", compteur_low)
print("total warning: ", compteur_warning)
