import os
import sys
import pytest
sys.path.insert(0,
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                        ".."
                    )
                ))

# from module.grid import grille, taille_grille
# test_morpion.py

import pytest
from module.mouvement import placer_marque  # Importation correcte
from module.victoire_nul import victoire, match_nul
from game import jeu
from unittest.mock import patch

# Importe ta fonction jeu
from game import jeu

def test_partie_victoire_x():
    mouvements = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]  # X gagne
    with patch('builtins.input', side_effect=['n']):  # Simuler l'entrée pour "non"
        jeu(mouvements=mouvements)

def test_victoire():
    # Configuration d'une grille gagnante pour 'X'
    grille_test = [['X', 'X', 'X'], ['', '', ''], ['', '', '']]
    assert victoire(grille_test, 'X') == True

def test_match_nul():
    # Configuration d'une grille nulle
    grille_test = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
    assert match_nul(grille_test) == True

def test_placer_marque():
    # Test pour vérifier si la marque est bien placée
    grille_test = [['', '', ''], ['', '', ''], ['', '', '']]
    placer_marque(grille_test, 1, 1, 'O')
    assert grille_test[1][1] == 'O'
