# Capteur Température - V1

## Objectif

Simuler un capteur de température en C et analyser les données en Python.

---

## Fonctionnement

### C (capteur)

* Génère 10 valeurs de température aléatoires
* Applique règles :

  * < 15 → LOW TEMP
  * 15–80 → NOMINAL
  * > 80 → WARNING
* Affiche les résultats

### Python (analyse)

* Analyse une liste de relevés
* Compte :

  * LOW TEMP
  * WARNING
* Affiche un résumé

---

## Exemple de sortie (C)

```
Cycle 1 | Temp: 32 | Status: NOMINAL
Cycle 2 | Temp: 12 | Status: LOW TEMP
Cycle 3 | Temp: 91 | Status: WARNING
```

---

## Lancer le projet

### Compilation et exécution C

```bash
gcc capteur_temp101.c -o capteur_temp101
./capteur_temp101
```

### Exécution Python

```bash
python3 analyse.py
```

---

## Version

V1 : version simple, fonctionnelle (MVP)

---

## Améliorations prévues (V2)

* Écriture des données du C dans un fichier
* Lecture du fichier en Python
* Parsing des données
* Statistiques plus avancées
