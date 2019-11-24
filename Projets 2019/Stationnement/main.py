from tkinter import *
import PIL.Image as img
import PIL.ImageTk as imgTk



def stationnement_voiture(canvas):
    """0: la place est vide

    1: la place est occupée

    -1: la porte de sortie

    2: notre position

     Cette fonction nous indique la position des voitures sur la grille, en fonction du niveau 1 """


    stationnement_voiture = [[0] * 6 for _ in range(6)]
    stationnement_voiture[2][5] = -1
    stationnement_voiture[0][0] = 2
    stationnement_voiture[3][3] = 1
    stationnement_voiture[2][3] = 1
    stationnement_voiture[4][1] = 1

    canvas.data["stationnement_voiture"] = stationnement_voiture
    canvas.data["mouvement"] = 0
    canvas.data["difficulte"] = 20

    canvas.data["voiture_rouge"] = img.open('Vrouge.png').resize((100,100), img.ANTIALIAS)
    canvas.data["voiture_rouge"] = imgTk.PhotoImage(image=canvas.data["voiture_rouge"])

    canvas.data["voiture_bleue"] = img.open('Vbleu.png').resize((100,100), img.ANTIALIAS)
    canvas.data["voiture_bleue"] = imgTk.PhotoImage(image=canvas.data["voiture_bleue"])

    canvas.data["exit"] = img.open('image.png').resize((100,100), img.ANTIALIAS)
    canvas.data["exit"] = imgTk.PhotoImage(image=canvas.data["exit"])

    TrouverVoiture(canvas)




def stationnement_voiture2(canvas):
    """# 0: la place est vide

        # 1: la place est occupée

        # -1: la porte de sortie

        # 2: notre position

        Cette fonction nous indique la position des voitures sur la grille, en fonction du niveau 2"""

    stationnement_voiture = [[0] * 6 for _ in range(6)]
    stationnement_voiture[2][5] = -1
    stationnement_voiture[0][0] = 2
    stationnement_voiture[0][2] = 1
    stationnement_voiture[1][0] = 1
    stationnement_voiture[4][1] = 1
    stationnement_voiture[3][2] = 1
    stationnement_voiture[1][3] = 1
    stationnement_voiture[4][4] = 1





    canvas.data["stationnement_voiture"] = stationnement_voiture
    canvas.data["mouvement"] = 0
    canvas.data["difficulte"] = 7

    canvas.data["voiture_rouge"] = img.open('Vrouge.png').resize((100,100), img.ANTIALIAS)
    canvas.data["voiture_rouge"] = imgTk.PhotoImage(image=canvas.data["voiture_rouge"])

    canvas.data["voiture_bleue"] = img.open('Vbleu.png').resize((100,100), img.ANTIALIAS)
    canvas.data["voiture_bleue"] = imgTk.PhotoImage(image=canvas.data["voiture_bleue"])


    TrouverVoiture(canvas)



def TrouverVoiture(canvas):

    """ Cette fonction nous permet de trouvez l'emplcament de la voiture,  en foncion de la rangée [ran] et la colonne [col],
    et de stocker cet emplacement au debut de la rangee et au debut de la colonne  (head Row, head Col) """

    stationnement_voiture = canvas.data["stationnement_voiture"]

    rans = len(stationnement_voiture)

    cols = len(stationnement_voiture[0])

    voitureRan = 0

    voitureCol = 0

    for ran in range(rans):

        for col in range(cols):

            if stationnement_voiture[ran][col] == 2:

                voitureRan = ran

                voitureCol = col

    canvas.data["voitureRan"] = voitureRan

    canvas.data["voitureCol"] = voitureCol





def deplacementvoiture(canvas, ran, col ): #d

    """ Cette fonction nous permet de developper la voiture d'une case dans la direction voulu"""

    stationnement_voiture = canvas.data["stationnement_voiture"]

    rans = len(stationnement_voiture)

    cols = len(stationnement_voiture[0])

    voitureRan = canvas.data["voitureRan"]

    voitureCol = canvas.data["voitureCol"]

    difficulte = canvas.data["difficulte"]

    mouvement = canvas.data["mouvement"]

    nouvellevoitureRan = voitureRan + ran #d

    nouvellevoitureCol = voitureCol + col #d

    canvas.data["mouvement"] = canvas.data["mouvement"] + 1


    if (nouvellevoitureCol<0) or (nouvellevoitureCol >= cols) or (nouvellevoitureRan<0) or (nouvellevoitureRan >= rans) or (mouvement+1>difficulte):

        canvas.data["Perdu"] = True



    else:



        if (stationnement_voiture[nouvellevoitureRan][nouvellevoitureCol] == 0):

            stationnement_voiture[nouvellevoitureRan][nouvellevoitureCol] = 2

            stationnement_voiture[voitureRan][voitureCol] = 0

            canvas.data["voitureRan"] = nouvellevoitureRan

            canvas.data["voitureCol"] = nouvellevoitureCol



        elif (stationnement_voiture[nouvellevoitureRan][nouvellevoitureCol] == 1):

            canvas.data["Perdu"] = True



        elif (stationnement_voiture[nouvellevoitureRan][nouvellevoitureCol] == -1):

            stationnement_voiture[nouvellevoitureRan][nouvellevoitureCol] = 2

            stationnement_voiture[voitureRan][voitureCol] = 0

            canvas.data["voitureRan"] = nouvellevoitureRan

            canvas.data["voitureCol"] = nouvellevoitureCol

            canvas.data["Gagné"] = True





def ToucheClavier(evenement):

    canvas = evenement.widget.canvas



    if (evenement.char == "r"):

        init(canvas)

    if (evenement.char == "n"):

        init2(canvas)



    if (canvas.data["Perdu"] == False) and (canvas.data["Gagné"] == False):

        if (evenement.keysym == "Up"):

            deplacementvoiture(canvas, -1, 0)

        elif (evenement.keysym == "Down"):

            deplacementvoiture(canvas, +1, 0)

        elif (evenement.keysym == "Left"):

            deplacementvoiture(canvas, 0,-1)

        elif (evenement.keysym == "Right"):

            deplacementvoiture(canvas, 0,+1)

        ToutRedessinner(canvas)



def ToutRedessinner(canvas):
    """ Cette fonction permet d'actualliser, le canvas a chaque intervention du joueur"""

    canvas.delete(ALL)

    DessinerGrille(canvas)

    if (canvas.data["Perdu"] == True):

        cx = 300

        cy = 300

        canvas.create_text(cx, cy, text="Perdu!", font=("Helvetica", 72, "bold"))



    if (canvas.data["Gagné"] == True):

        cx = 300

        cy = 300

        canvas.create_text(cx, cy, text="Bravo!", font=("Helvetica", 72, "bold"))





def DessinerGrille(canvas):



    stationnement_voiture = canvas.data["stationnement_voiture"]

    rans = len(stationnement_voiture)

    cols = len(stationnement_voiture[0])

    for ran in range(rans):

        for col in range(cols):

            DessinerCaseVoiture(canvas, stationnement_voiture, ran, col)

    canvas.create_text((335, 640), fill="white", font="Times 15  bold",
                       text="Faire parvenir la voiture bleue à la sortie en respectant le nombre de mouvements imposés.")
    canvas.create_text((335, 665), fill="white", font="Times 15  bold",
                       text="Utiliser les fléches présentes sur le clavier pour se déplacer vers le haut, bas, gauche et droite.")
    canvas.create_text((335, 690), fill="white", font="Times 15  bold",
                       text="Appuyez sur r pour recommencer et sur n pour passer au niveau suivant.")
    canvas.create_text((300, 10), fill="white", font="Times 15  bold", text='Il vous reste ' + str(canvas.data["difficulte"] - canvas.data["mouvement"]) + ' mouvements!')


""" Cette fonction nous permet de dessiner une case puis d'insérer les images correspondantes aux coordonnées"""

def DessinerCaseVoiture(canvas, stationnement_voiture, ran, col):

    marge = 20
    TailleCell = 100

    Gauche = marge + col * TailleCell

    Droite = Gauche + TailleCell

    Haut = marge + ran * TailleCell

    Bas = Haut + TailleCell

    canvas.create_rectangle(Gauche, Haut, Droite, Bas, fill="white")

    if (stationnement_voiture[ran][col] ==2):

        canvas.create_image(Gauche, Haut, image = canvas.data["voiture_bleue"], anchor='nw')



    if (stationnement_voiture[ran][col] ==-1):

        canvas.create_image(Gauche, Haut, image = canvas.data["exit"], anchor='nw')



    if (stationnement_voiture[ran][col] ==1):

        canvas.create_image(Gauche, Haut, image = canvas.data["voiture_rouge"], anchor='nw')

def Instructions():

    print ("Sortez la voiture du parking!")

    print ("Utilisez les flèches pour déplacer la voiture.")

    print ("Evitez les autres voitures.")

    print ("Appuyez sur r pour recommencer.")



def init(canvas):

    Instructions()

    canvas.data["Perdu"] = False

    canvas.data["Gagné"] = False

    stationnement_voiture(canvas)

    ToutRedessinner(canvas)



def init2(canvas):

    Instructions()

    canvas.data["Perdu"] = False

    canvas.data["Gagné"] = False

    stationnement_voiture2(canvas)

    ToutRedessinner(canvas)





##########################################################################



def run():

    root = Tk()
    canvas = Canvas(root, bg="green", width=650, height=700)
    canvas.pack()
    root.canvas = canvas.canvas = canvas
    canvas.data = {}
    init(canvas)

    root.bind("<Key>", ToucheClavier)
    bouton_fermer = Button(root, text="fermer", command=root.quit)
    bouton_fermer.pack()



    root.mainloop()


run()