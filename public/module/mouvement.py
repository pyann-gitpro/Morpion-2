
# module/mouvement.py

def placer_marque(grille, ligne, colonne, joueur):
    """
    Place la marque du joueur ('X' ou 'O') dans la grille à la position spécifiée.
    """
    grille[ligne][colonne] = joueur  # Utiliser la notation correcte pour les listes

