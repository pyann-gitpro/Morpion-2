
# Jeu de Morpion

Ce projet est un simple jeu de Morpion en Python avec une interface d'affichage graphique de la grille à l'aide de `matplotlib`. Le jeu se joue à deux joueurs et s'arrête lorsqu'un joueur gagne ou lorsque la partie se termine par un match nul.

## Modules

Le projet est organisé en plusieurs modules :

1. **game.py** : Le fichier principal qui contrôle le déroulement du jeu. Il utilise les fonctions des autres modules pour gérer la grille, les réponses des joueurs et la vérification des conditions de victoire ou de match nul.

2. **reponse.py** : Ce module gère les entrées des joueurs. Il demande à l'utilisateur d'entrer la ligne et la colonne où il souhaite placer son marqueur (X ou O).

3. **grid.py** : Ce module contient la grille du jeu et une fonction pour afficher la grille à l'aide de `matplotlib`.

4. **victoire_nul.py** : Ce module contient les fonctions qui vérifient si un joueur a gagné ou si le match est nul.

## Prérequis

- Python 3.x
- Les bibliothèques suivantes doivent être installées :
    - `numpy`
    - `matplotlib`

Vous pouvez installer ces bibliothèques avec la commande suivante :

```bash
pip install -r requirements.txt
```

## Exécution du jeu

Pour démarrer le jeu, exécutez simplement le fichier `game.py` :

```bash
python game.py
```

Le jeu affichera la grille à chaque tour, et les joueurs devront entrer les numéros de ligne et de colonne pour placer leur marqueur. Le jeu continue jusqu'à ce qu'un joueur gagne ou qu'il y ait match nul.

## Structure des fichiers

Voici l'arborescence du projet :

```bash
.
├── .github/
│        ├──workflows/
│            ├── tests.yml/
├── .venv/
├── public/
├       ├──module/
│       │    ├── __pycache__/
│       │    ├── grid.py
│       │    ├── reponse.py
│       │    └── victoire_nul.py
│       ├──tests/
│            ├── __pycache__/
│            └── test_morpion.py
├── game.py
├── .gitignore
├── readme.md
├── requirements.txt
```

## Règles du jeu

- Le jeu se joue à deux joueurs. Le premier joueur utilise le marqueur "X" et le second "O".
- Chaque joueur, à son tour, entre un numéro de ligne et un numéro de colonne pour placer son marqueur.
- Le premier joueur à aligner trois marqueurs (horizontalement, verticalement ou en diagonale) gagne la partie.
- Si toutes les cases sont remplies sans qu'aucun joueur n'aligne trois marqueurs, la partie se termine par un match nul.

## Tests Unitaires / Github Actions et Workflows

- **Créer un fichier de workflow** : Dans votre dépôt GitHub, créez un fichier `.github/workflows/tests.yml` (ou un nom similaire). Ce fichier YAML définit les étapes de votre workflow d'automatisation.
- **Définir les déclencheurs** : Indiquez quand vous souhaitez que vos tests soient exécutés (par exemple, à chaque push sur la branche main, lors de la création d'une pull request, etc.).
- **Configurer l'environnement** : Spécifiez l'environnement d'exécution de vos tests (système d'exploitation, version de Python, dépendances, etc.).
- **Exécuter les tests** : Utilisez les actions appropriées pour installer vos dépendances, puis lancez vos tests avec la commande de votre framework de test (pytest, unittest, etc.).
- **Afficher les résultats** : Utilisez les actions pour afficher les résultats des tests directement sur GitHub, par exemple en les publiant dans les commentaires de la pull request.

***Voici un exemple simple de workflow pour pytest :***

```yaml
name: Python application CI/CD
on:
  push:
    branches: [ main, dev ]  # Branch to survey
  pull_request:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11"]
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements_train.txt
        # Add any specific installation commands for libcpab
        pip install -e libcpab


    # tests
    - name: Run unit tests (un fichier)
      run: |
        pytest tests/test_0.py
    - name: Run unit tests (un autre fichier)
      run: |
        pytest tests/test_1.py
```

## Créateurs

- [Guillaume Thomas](mailto:g.thomas83200@gmail.com)
- [Yamine Aissani](mailto:yamineaissani1@gmail.com)
- [Yann Paaeho](mailto:paaeho.yann.pro@gmail.com)
