from tkinter import *
from configuration import *
import numpy
import random
import time


# toutes les fonctions lie le jeux sont integralisé dans la classe jeux donc toutes les fonctions sont construite avec\
# "self"
class JEUX:
    def __init__(self, canvas, cpu):
        self.cpu = cpu
        self.canvas = canvas
        self.case = []
        self.tour = 0
        self.joueur = 1
        self.cpu_not_playing = True
        self.tableau = numpy.zeros((NB_RANGÉE, NB_COLONNE))
        self.game_over = False
        self.canvas.bind("<Button-1>", self.pointeur)
        self.dessiner_fond(self.canvas, self.case)

    def afficher_tableau(self):
        """
        Cette fonction affiche, dans le terminal le tableau de 0 qui correspond au tableau de jeu.
        :return:
        """
        print(numpy.flip(self.tableau), 0)

    def colonne_libre(self, colonne):
        """
        Cette fonction vérifie si la colonne choisit est libre (si on peut y placer un jeton).
        :param colonne:
        :return:
        """
        return self.tableau[NB_RANGÉE - 1][colonne] == 0

    def range_libre(self, colonne):
        """
        Cette fonction définie sur quel rangee le pions va se placer dans la colonne choisit.
        :param colonne:
        :return:
        """
        for r in range(NB_RANGÉE):
            if self.tableau[r][colonne] == 0:
                return r

    def placer_jetons(self, rangee, colonne):
        """
        Cette fonction place le jetons dans la colonne desiré en changeant la couleur du rond.
        :param rangee:
        :param colonne:
        :return:
        """
        self.tableau[rangee][colonne] = self.joueur
        rangee = NB_RANGÉE-rangee-1
        self.canvas.itemconfig(self.case[colonne][rangee], fill=COULEUR[self.joueur])
        if self.joueur == 1 or not self.cpu:
            self.canvas.update()
        else:
            time.sleep(1)
            self.canvas.update()

    def coup_de_grace(self):
        """
        Cette fonction verifie si il y a 4 pions alignés, si il y en a effectivement 4 alors elle renvoit True ce qui \
        arrete la partie et fait gagner un des deux joueurs.
        :return:
        """
        jetons = self.joueur
        # Vérifier l'horizontale
        for c in range(NB_COLONNE - 3):
            for r in range(NB_RANGÉE):
                if self.tableau[r][c] == jetons and self.tableau[r][c + 1] == jetons and self.tableau[r][c + 2] == jetons and \
                        self.tableau[r][c + 3] == jetons:
                    return True

        # Vérifier la verticale
        for c in range(NB_COLONNE):
            for r in range(NB_RANGÉE - 3):
                if self.tableau[r][c] == jetons and self.tableau[r + 1][c] == jetons and self.tableau[r + 2][c] == jetons and \
                        self.tableau[r + 3][c] == jetons:
                    return True

        # Vérifier la diagonale croissante
        for c in range(NB_COLONNE - 3):
            for r in range(NB_RANGÉE - 3):
                if self.tableau[r][c] == jetons and self.tableau[r + 1][c + 1] == jetons and self.tableau[r + 2][c + 2] == jetons and \
                        self.tableau[r + 3][c + 3] == jetons:
                    return True

        # Vérifier la diagonale décroissante
        for c in range(NB_COLONNE - 3):
            for r in range(3, NB_RANGÉE):
                if self.tableau[r][c] == jetons and self.tableau[r - 1][c + 1] == jetons and self.tableau[r - 2][c + 2] == jetons and \
                        self.tableau[r - 3][c + 3] == jetons:
                    return True

    def dessiner_fond(self, canvas, case):
        """
        Cette fonction dessine le tableau de jeu (7 colonnes par 6 rangees avec dans chaques cases un rond noir)
        :param canvas:
        :param case:
        :return:
        """
        for i in range(NB_COLONNE):
            case.append([])
            for j in range(NB_RANGÉE):
                case[i].append(canvas.create_oval(4 + CASE * i, 4 + CASE * j, 96 + CASE * i, 96 + CASE * j, fill="black"))

    def draw(self):
        """
        Cette fonction ecrit sur le canvas 'Égalité' si il n'y a pas de gagnant
        :return:
        """
        print("Égalité")
        self.game_over = True
        self.canvas.create_text(350, 300, fill="white", font=(" ", 100), text="Égalité")

    def gagne(self, joueur):
        """
        Cette fonction ecrit sur le canvas le joueur gagnant.
        :param joueur:
        :return:
        """
        print("le joueur", joueur, "a gagné")
        self.game_over = True
        if joueur == 1:
            self.canvas.create_text(350, 100, fill="red", font=(" ", 50), text="le joueur 1 a gagné")
        elif self.cpu:
            self.canvas.create_text(350, 100, fill="yellow", font=(" ", 50), text="L'ordinateur a gagné")
        else:
            self.canvas.create_text(350, 100, fill="yellow", font=(" ", 50), text="le joueur 2 a gagné")

    def colonnes_disponibles(self):
        """
        Cette fonction créer et renvoie une liste des colonnes disponibles, (celles où l'on peut placer un jetons).
        :return:
        """
        colonnes_libres = []
        for colonne in range(NB_COLONNE):
            if self.colonne_libre(colonne):
                colonnes_libres.append(colonne)
        return colonnes_libres

    def winning_move(self, jetons, ancienne_colone="default"):
        """
        Cette fonction renvoi une colonne quand il y a 3 jetons alignés afin de gagner ou de blocker le puissance 4 de\
        l'adversaire, quand ce n'est pas le cas elle renvoit une colonne au hasard dans les colonnes disponibles si\
        il y en a, sinon elle renvoit 'impossible' vu qu'il n'y a pas de colonnes disponibles.
        :param jetons:
        :param ancienne_colone:
        :return:
        """

        # Verifie les horizontales en partant de la gauche
        for c in range(NB_COLONNE - 3):
            for r in range(NB_RANGÉE):
                if self.tableau[r][c] == jetons and self.tableau[r][c + 1] == jetons and self.tableau[r][c + 2] == jetons\
                        and self.tableau[r][c + 3] == 0:
                    return c + 3

        # Verifie les horizontales en partant de la droite
        for c in range(NB_COLONNE - 3):
            for r in range(NB_RANGÉE):
                if self.tableau[r][c] == 0 and self.tableau[r][c + 1] == jetons and self.tableau[r][c + 2] == jetons and\
                        self.tableau[r][c + 3] == jetons:
                    return c

        for c in range(NB_COLONNE - 3):
            for r in range(NB_RANGÉE):
                if self.tableau[r][c] == jetons and self.tableau[r][c + 1] == 0 and self.tableau[r][c + 2] == jetons and\
                        self.tableau[r][c + 3] == jetons:
                    return c + 1

        for c in range(NB_COLONNE - 3):
            for r in range(NB_RANGÉE):
                if self.tableau[r][c] == jetons and self.tableau[r][c + 1] == jetons and self.tableau[r][c + 2] == 0 and\
                        self.tableau[r][c + 3] == jetons:
                    return c + 2

        # Verifie les verticales
        for c in range(NB_COLONNE):
            for r in range(NB_RANGÉE - 3):
                if self.tableau[r][c] == jetons and self.tableau[r + 1][c] == jetons and self.tableau[r + 2][c] == jetons\
                        and self.tableau[r + 3][c] == 0:
                    return c

        # Verifie les diagonales croissantes
        for c in range(NB_COLONNE - 3):
            for r in range(NB_RANGÉE - 3):
                if self.tableau[r][c] == jetons and self.tableau[r + 1][c + 1] == jetons and self.tableau[r + 2][c + 2]\
                        == jetons and self.tableau[r + 3][c + 3] == 0:
                    return c + 3

        for c in range(NB_COLONNE - 3):
            for r in range(NB_RANGÉE - 3):
                if self.tableau[r][c] == 0 and self.tableau[r + 1][c + 1] == jetons and self.tableau[r + 2][c + 2]\
                        == jetons and self.tableau[r + 3][c + 3] == jetons:
                    return c

        for c in range(NB_COLONNE - 3):
            for r in range(NB_RANGÉE - 3):
                if self.tableau[r][c] == jetons and self.tableau[r + 1][c + 1] == 0 and self.tableau[r + 2][c + 2]\
                        == jetons and self.tableau[r + 3][c + 3] == jetons:
                    return c + 1

        for c in range(NB_COLONNE - 3):
            for r in range(NB_RANGÉE - 3):
                if self.tableau[r][c] == jetons and self.tableau[r + 1][c + 1] == jetons and self.tableau[r + 2][c + 2]\
                        == 0 and self.tableau[r + 3][c + 3] == jetons:
                    return c + 2

        # Verifie les diagonales decroissantes
        for c in range(NB_COLONNE - 3):
            for r in range(3, NB_RANGÉE):
                if self.tableau[r][c] == 0 and self.tableau[r - 1][c + 1] == jetons and self.tableau[r - 2][c + 2] ==\
                        jetons and self.tableau[r - 3][c + 3] == jetons:
                    return c

        for c in range(NB_COLONNE - 3):
            for r in range(3, NB_RANGÉE):
                if self.tableau[r][c] == jetons and self.tableau[r - 1][c + 1] == jetons and self.tableau[r - 2][c + 2] ==\
                        jetons and self.tableau[r - 3][c + 3] == 0:
                    return c + 3

        for c in range(NB_COLONNE - 3):
            for r in range(3, NB_RANGÉE):
                if self.tableau[r][c] == jetons and self.tableau[r - 1][c + 1] == 0 and self.tableau[r - 2][c + 2] ==\
                        jetons and self.tableau[r - 3][c + 3] == jetons:
                    return c + 1

        for c in range(NB_COLONNE - 3):
            for r in range(3, NB_RANGÉE):
                if self.tableau[r][c] == jetons and self.tableau[r - 1][c + 1] == jetons and self.tableau[r - 2][c + 2] ==\
                        0 and self.tableau[r - 3][c + 3] == jetons:
                    return c + 2

        if jetons == 2:
            return ancienne_colone

        elif len(self.colonnes_disponibles()) != 0:
            return random.choice(self.colonnes_disponibles())
        else:
            return "impossible"

    def cpu_action(self):
        """
        Cette fonction modelise l'ordinateur, elle place un jeton dans la colonne recu quand il y a 3 jetons alignés ou\
        elle le place dans une colonne aleatoire..
        :return:
        """
        self.joueur = 2
        self.cpu_not_playing = False

        colonne_bloquer = self.winning_move(1)
        colonne_gagner_ou_bloquer = self.winning_move(2, colonne_bloquer)
        print(colonne_bloquer)
        if colonne_gagner_ou_bloquer != "impossible":
            if self.colonne_libre(colonne_gagner_ou_bloquer) and not self.game_over:
                rangee = self.range_libre(colonne_gagner_ou_bloquer)
                self.placer_jetons(rangee, colonne_gagner_ou_bloquer)
                self.afficher_tableau()

                if self.coup_de_grace():
                    self.gagne(self.joueur)

                self.cpu_not_playing = True

    def jouer_humain(self, colonne):
        """
        Cette fonction modelise une partie de jeux de 2 joueurs humains qui joue l'un contre l'autre.
        :param colonne:
        :return:
        """
        if self.tour == 0:
            self.joueur = 1
            if self.colonne_libre(colonne):
                rangee = self.range_libre(colonne)
                self.placer_jetons(rangee, colonne)
                self.afficher_tableau()
                self.tour += 1

                if self.coup_de_grace():
                    self.gagne(self.joueur)

        else:
            self.joueur = 2
            if self.colonne_libre(colonne):
                rangee = self.range_libre(colonne)
                self.placer_jetons(rangee, colonne)
                self.afficher_tableau()
                self.tour += 1

                if self.coup_de_grace():
                    self.gagne(self.joueur)

    def jouer_ordi(self, colonne):
        """
        Cette fonction modelise la partie entre le joueur et l'ordinateur.
        :param colonne:
        :return:
        """
        self.joueur = 1
        if self.colonne_libre(colonne) and self.cpu_not_playing:
            rangee = self.range_libre(colonne)
            self.placer_jetons(rangee, colonne)
            self.afficher_tableau()

            if self.coup_de_grace():
                self.gagne(self.joueur)

            self.cpu_action()

    def pointeur(self, event):
        """
        Cette fonction lance le jeu lorsque un clic est detecté, si dans le menu on a choisit de jouer contre \
        l'ordinateur, alors elle lance la partie avec l'ordinateur sinon elle lance la partie de 1 contre 1 avec des \
        joueurs réels
        :param event:
        :return:
        """
        print(event.x, event.y)
        colonne = int(event.x//CASE)
        if not self.game_over:
            if self.cpu:
                self.jouer_ordi(colonne)
            else:
                self.jouer_humain(colonne)
                self.tour = self.tour % 2

        if numpy.all(self.tableau != 0):
            self.draw()


def nouvelle_partie(cpu):
    """
    Cette fonction affiche le tableau de jeux et lance une nouvelle partie quand elle est appelée par le menu.
    :param cpu:
    :return:
    """
    fenetre = Tk()
    fenetre.geometry("700x600+410+50")
    fenetre.title("Puissance 4")
    canvas = Canvas(master=fenetre, width=7*CASE, height=6*CASE)
    canvas.pack()
    canvas.create_rectangle(0, 0, 700, 600, fill="#00F")
    JEUX(canvas, cpu)
    fenetre.mainloop();