# game.py

from module.grid import afficher_grille, grille, taille_grille
from module.reponse import reponse
from module.victoire_nul import victoire, match_nul
from module.mouvement import placer_marque
import time  # Pour ajouter un délai à la fin du jeu

def interaction_utilisateur(grille):
    """
    Demande les coordonnées à l'utilisateur via input().
    """
    while True:
        try:
            ligne = int(input(f"Entrez le numéro de la ligne (1-{taille_grille}): ")) - 1
            colonne = int(input(f"Entrez le numéro de la colonne (1-{taille_grille}): ")) - 1
            return reponse(grille, ligne, colonne)
        except ValueError as e:
            print(e)
            print("Veuillez entrer des coordonnées valides.")

def jeu(mouvements=None, interaction=None):
    """
    Fonction principale du jeu.
    - `mouvements`: Liste de tuples (ligne, colonne) pour simuler les mouvements.
    - `interaction`: Fonction pour obtenir les coordonnées si `mouvements` est `None`.
    """
    joueur_actuel = 'X'
    mouvement_index = 0

    while True:
        afficher_grille(grille)

        if mouvements:
            # Utilise les mouvements prédéfinis si fournis (pour les tests)
            ligne, colonne = mouvements[mouvement_index]
            mouvement_index += 1
        else:
            # Sinon, utilise l'interaction utilisateur
            if interaction:
                ligne, colonne = interaction(grille)
            else:
                raise ValueError("Aucune méthode d'interaction fournie pour récupérer les mouvements.")

        placer_marque(grille, ligne, colonne, joueur_actuel)

        if victoire(grille, joueur_actuel):
            afficher_grille(grille)
            print(f"Le joueur {joueur_actuel} a gagné!")
            time.sleep(1)  # Petite pause pour que le joueur puisse voir le message
            break
        elif match_nul(grille):
            afficher_grille(grille)
            print("Match nul!")
            time.sleep(1)  # Petite pause pour afficher le message
            break

        # Changer de joueur
        joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'

    # Option pour rejouer ou quitter
    fin_jeu()

def fin_jeu():
    """
    Fonction pour demander si l'utilisateur souhaite rejouer ou quitter.
    """
    while True:
        choix = input("Voulez-vous rejouer ? (o/n) : ").lower()
        if choix == 'o':
            # Réinitialiser la grille et relancer le jeu
            global grille
            grille = [['', '', ''], ['', '', ''], ['', '', '']]  # Réinitialiser la grille
            jeu(interaction=interaction_utilisateur)  # Relancer une nouvelle partie
            break
        elif choix == 'n':
            print("Merci d'avoir joué ! À bientôt.")
            time.sleep(1)  # Pause avant de quitter
            break
        else:
            print("Veuillez entrer 'o' pour rejouer ou 'n' pour quitter.")

# Appel principal du jeu avec interaction utilisateur
if __name__ == "__main__":
    jeu(interaction=interaction_utilisateur)
