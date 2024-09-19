from module.grid import taille_grille

def reponse(grille, ligne, colonne):
    # Vérifier si la ligne et la colonne sont valides
    if ligne in range(taille_grille) and colonne in range(taille_grille) and grille[ligne, colonne] == '':
        return ligne, colonne
    else:
        raise ValueError("Case déjà occupée ou hors de la grille.")
