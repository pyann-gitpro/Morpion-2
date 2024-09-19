import numpy as np
from module.grid import taille_grille



def match_nul(grille):
    return np.all(grille != '')

def victoire(grille, joueur_actuel):
    for i in range(taille_grille):
        if all(cell == joueur_actuel for cell in grille[i]) or all(grille[j][i] == joueur_actuel for j in range(taille_grille)):
            return True
    if all(grille[i][i] == joueur_actuel for i in range(taille_grille)) or all(grille[i][taille_grille - 1 - i] == joueur_actuel for i in range(taille_grille)):
        return True
    return False
