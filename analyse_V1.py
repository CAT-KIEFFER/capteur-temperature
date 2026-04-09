lignes = ["Cycle 1 | Temp: 25 | Status: NOMINAL", "Cycle 2 | Temp: 60 | Status: NOMINAL",
 "Cycle 3 | Temp: 81 | Status: WARNING", "Cycle 4 | Temp: 43 | Status: NOMINAL",
 "Cycle 5 | Temp: 17 | Status: NOMINAL", "Cycle 6 | Temp: 10 | Status: LOW TEMP",
 "Cycle 7 | Temp: 0 | Status: LOW TEMP", "Cycle 8 | Temp: 60 | Status: NOMINAL",
 "Cycle 9 | Temp: 100 | Status: WARNING", "Cycle 10 | Temp: 13 | Status: LOW TEMP"]

compteur_low = 0
compteur_warning = 0

for ligne in lignes:
    if "LOW TEMP" in ligne:
        compteur_low += 1
    if "WARNING" in ligne:
        compteur_warning += 1
print("total des relevés: ", len(lignes))
print("total low: ", compteur_low)
print("total warning: ", compteur_warning)
