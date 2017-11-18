from tkinter import *
from random import randrange
import pandas as pd



class Fenetre(Frame):
  
    def __init__(self):

        super().__init__()     #prend toutes les proprietes de la classe Frame    
        self.initUI()
        
    
    def initUI(self):
        '''Initalisation de chaque objet de la classe'''

        self.master.title("Revise le BAC en jouant!") #Proprietes de la fenetre principale
        self.configure(bg="gray10")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow() 



        #creation des blocs d'informations de la fenetre
        fenetre_haut = LabelFrame(self, text="Le BACorévisateur", font=" Athelas 40 bold", relief= "ridge", padx=500, pady=20, bg="IndianRed4", labelanchor=N)
        self.frame_questions_et_des=Frame(self,borderwidth=5, bg="IndianRed4", relief=GROOVE)
        self.frame_exit=Frame(self,borderwidth=5, bg="grey", relief=GROOVE)
        self.frame_theme=Frame(self.frame_questions_et_des,borderwidth=5, bg="grey", relief=GROOVE)
        self.frame_theme_base=Frame(self.frame_questions_et_des,borderwidth=5, bg="grey", relief=GROOVE)
        self.frame_question=Frame(self.frame_questions_et_des,borderwidth=5, bg="grey", relief=GROOVE)
        self.canvas=Canvas(self, width=900, height=650, bg='white')
        self.boutton_theme=Button(self.frame_theme, text ='Choisir un theme', command = self.dedecouleur)
        des_couleur=Frame(self.frame_theme_base, borderwidth=5, bg="grey", relief=GROOVE)
        regles=Button(fenetre_haut, text ='RÉGLE DU JEU', command=self.afficherregle)
        self.action=Button(self.frame_questions_et_des, text="Vérifier", command=self.action)
        self.quitButton = Button(self.frame_exit, text="Quitter", command=self.quit)
        
        #importation de la photo
        self.photo=PhotoImage(file = './photo.gif')
        tableau_jeu=self.canvas.create_image(0, 0, image=self.photo)

        #classification des themes avec sa couleur respective
        self.liste_themes=[["Geographie","blue"],["Histoire","yellow"],["Philosophie","pink"],["SVT","green"],["Physique-Chimie","purple"],["Mathematiques","red"]]

        #positions carthesiennes (x,y) en pixel de chaque case du tableau de jeu
        self.liste_position=[[278,515],[351,515],[430,515],[498,515],[577,515],[662,509],[741,480],[804,440],[843,358],[838,283],[832,202],[792,139],[725,87],[640,70],[555,70],[470,70],[396,70],[312,70],[215,70],[142,87],[96,139],[68,202],[68,283],[96,358],[147,420],[232,430],[316,430],[390,430],[465,430],[535,430],[612,430],[686,430], [740,358], [750,280], [730,200], [660,170], [590,170], [520,170], [440,170],[360,170], [250,170],[210,170], [150,250], [150,300], [210,350], [280,350], [350,350], [430,350], [520,350]]
        self.fin_dujeu=len(self.liste_position)-1
        
        #dictionaire contenant des listes vides pour chaques themes. les questions deja repondus seront ajoutee au fur et a mesure.
        self.dictionaire_question_repondu_correctement={}
        for theme in self.liste_themes:
            self.dictionaire_question_repondu_correctement[theme[0]]=[]

        
        #Dessine tout les blocs d'informations sur l'ecran
        fenetre_haut.pack(expand="yes")
        self.canvas.pack(side=LEFT, padx=5, pady=5)
        self.frame_questions_et_des.pack(side=TOP, padx=5, pady=5)
        self.frame_theme.pack(side=TOP, padx=5, pady=5)
        self.frame_theme_base.pack(side=TOP, padx=5, pady=5)
        self.frame_question.pack(side=TOP, padx=5, pady=5)
        self.boutton_theme.pack(side=TOP, padx=5, pady=5) 
        des_couleur.pack(side=TOP, padx=5, pady=5)
        Label(des_couleur, bg="grey").pack(padx=50, pady=50)
        self.frame_exit.pack(side=BOTTOM, padx=5, pady=5, fill=X)
        regles.pack(side=BOTTOM, padx=5, pady=5)
        self.action.pack(side=RIGHT, padx=5, pady=5, anchor=S)
        self.action.config(state='disabled')
        self.quitButton.pack(side=RIGHT, padx=5, pady=5, anchor=S)
        self.ball_1=self.canvas.create_oval(-10,-10,10,10, outline='black', fill='gray40', tags=('ball1'))
       

        self.canvas.move(self.ball_1, self.liste_position[0][0], self.liste_position[0][1])#placer le pion sur la premiere case
        self.canvas.move(tableau_jeu, 450, 300) #placer l'image au centre des diagolanl du Canvas

        self.absolute_pos1=0 # position  absolue (par rapport a la liste des position) du pion au long de la partie 


    def shutdown(self):
        '''fonction qui permet de terminer le jeu, Il desactive tout les bouttons sauf "quit".
        De plus, il efface la derniere question posée de lecran'''
        self.boutton_theme.config(state='disabled')
        self.action.config(state='disabled')
        for each_slave in self.frame_question.pack_slaves():
                each_slave.destroy()
        slaves= self.frame_theme_base.pack_slaves()
        for slave in slaves:
            slave.destroy()
        #print (self.dictionaire_question_repondu_correctement)

    	
    def get_center(self, ball):
        '''prendre la position carthesienne de la balle dans un instant donne'''
        return (self.canvas.coords(ball)[0]+self.canvas.coords(ball)[2])/2, (self.canvas.coords(ball)[1]+self.canvas.coords(ball)[3])/2

    def action(self):
        '''Fait l'action du pion'''

        reponse1=int(self.var1.get()) #le 'self.var.get' me retourne 1 ou 0 si chaque checkButton est appuyer ou non
        reponse2=int(self.var2.get()) 
        reponse3=int(self.var3.get())
        
        if (reponse1 + reponse2 + reponse3) == 1: #L'action n'est faite que si un seul des CheckButton est appuyer.
            center= self.get_center(self.ball_1)
            if (reponse1 == self.reponse) or (2*reponse2 == self.reponse) or (3*reponse3 == self.reponse ):                                                                              #pour differencier  le checkButton 1, 2, 3 je multiplie les reponse par 1, 2 et 3. Les check button retourne une valeur de 1 ou de 0 dependant s'il est cocher ou non. Pour pouvoir verifier par rapport au tableau excel, on multiplie ces valeurs par l'indice de la variable.
                self.textrep = Text(self.frame_question, height=1, width=30)
                self.textrep.pack()
                self.textrep.insert(END, "Bonne réponse!")
                self.textrep
                self.absolute_pos1 = self.absolute_pos1 + 2 

                #si la reponse est juste, on aditionne la question au dictionnaire des question repondus
                self.dictionaire_question_repondu_correctement[self.theme[0]].append(self.df.iloc[self.numque][0])

                #On se questionne sur l'avancement du jeu, si le jeu est fini, le pion ne bougera pas. Sinon il avance
                if self.absolute_pos1 <= self.fin_dujeu :
                    self.canvas.move(self.ball_1, (self.liste_position[self.absolute_pos1][0] - center[0]), (self.liste_position[self.absolute_pos1][1] - center[1]))
            else:
                self.textrep = Text(self.frame_question, height=1, width=30)
                self.textrep.pack()
                self.textrep.insert(END, "Mauvaise réponse!")
                self.textrep

                self.absolute_pos1 = self.absolute_pos1 -1

                if self.absolute_pos1 < 0:
                    self.absolute_pos1 = 0

                else:
                    if self.absolute_pos1 < self.fin_dujeu :
                        self.canvas.move(self.ball_1, (self.liste_position[self.absolute_pos1][0] - center[0]), (self.liste_position[self.absolute_pos1][1] - center[1]))
            
            self.boutton_theme.config(state='normal')
            self.action.config(state='disabled')

        #determine quand le jeu est fini, lorsque la position absolue du pion est plus grand que le nombre de cases
        if self.absolute_pos1 > self.fin_dujeu :
            fim = Tk()
            fim.title("Le jeu est fini")
            frame4 = Frame(fim, borderwidth=5, relief=GROOVE)
            frame4.pack(padx=20, pady=20)

            Label(frame4, text="Felicitation! Vous avez fini le jeu et vous etes pret pour le bac",bg="green").pack(padx=20, pady=20)
            self.shutdown()


    def centerWindow(self):
        '''Definie l'affichage de la fenetre et sa taille, puis la centre dans lecran'''
      
        w = 1300
        h = 900

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
    
    def afficherregle(self):
        '''afiche les regles et permet qu'une seule fenetre ne soit ouverte meme quand le boutton est appuyer plusieurs fois'''
        try:
            self.fenetre_regle.destroy()
        except:
            pass
        self.fenetre_regle = Tk()
        self.fenetre_regle.title("Regles du jeux")
        self.configure(bg="black")
        self.Frame3 = Frame(self.fenetre_regle, borderwidth=5, relief=GROOVE)
        self.Frame3.pack(padx=20, pady=20)
        #self.quitButton_regles = Button(self.Frame3, text="Fermer", command=self.quit)

        Label(self.Frame3, text="Regles du jeu",bg="green").pack(padx=20, pady=20)
        Label(self.Frame3, text="1. Chaque joueur lance le dé pour choisir son thème. Chaque couleur du dé correspond a une matière. ",bg="light blue").pack(padx=20, pady=20)
        Label(self.Frame3, text="2. Il n'y a qu'une seule bonne réponse pour chaque question. Le pion n'avancera pas si le joueur coche plus d'une case.",bg="light blue").pack(padx=20, pady=20)
        Label(self.Frame3, text="3. Si la réponse cochée est la bonne, le pion avancera de 2 casses, sinon il reculera de 1 case.",bg="light blue").pack(padx=20, pady=20)
        Label(self.Frame3, text="4. Le joueur gagnera le jeu en arrivant sur la dernière case du plateau.",bg="light blue").pack(padx=20, pady=20)
    

    def dedecouleur(self):
        '''Tire au sors un theme ou les question deja repondu correctement ne se repete pas'''
        slaves= self.frame_theme_base.pack_slaves()# a chaque fois que l'on tire au sort un theme, on detruit tout les pack du frame_des_question
        for each_slave in self.frame_question.pack_slaves():
                each_slave.destroy()

        for slave in slaves:
            slave.destroy()

        #On reconstruit a partir  du tirage au sort du theme
        self.theme = self.liste_themes[randrange(1,6)]#tirage du theme
        self.des_couleur=Frame(self.frame_theme_base, borderwidth=5, bg=self.theme[1], relief=GROOVE)
        self.des_couleur.pack(side=TOP, padx=5, pady=5, fill=X)
        self.label_color=Label(self.des_couleur, text=self.theme[0],bg=self.theme[1]).pack(padx=20, pady=20)

        self.boutton_theme.config(state='disabled')
        self.action.config(state='normal')

        self.df=pd.read_excel(self.theme[0] +".xlsx") #ouvre le ficher excel dependant du theme, contenant les questions et l'insere dans un grid appele dataframe (df)
        taille=len(self.df["question"]) #se demande le nombres de questions dans le excel
        self.numque=randrange(1,taille) #choisit aleatoirement un entier entre 1 et le nombre total de question dans le fichier,  ce qui correspond a l'index de la question choisit

        while self.df.iloc[self.numque][0] in self.dictionaire_question_repondu_correctement[self.theme[0]]: #tant que la question a deja ete posee et bien repondu, on cherche une autre non repondu du meme theme
            self.numque=randrange(1,taille)
            if len(self.dictionaire_question_repondu_correctement[self.theme[0]]) == taille: # si toutes les questions on deja etet posee, on arrete le jeu
                #print ("stop")
                self.shutdown()
                break


        self.reponse=int(self.df.iloc[self.numque][4]) # acceder a la bonne reponse. Le iloc accede le dataframe par un grid
        self.text = Text(self.frame_question, height=4, width=50)#case de texte ou est inseree la question. cette case a 4lignes et 50px de grosseur
        self.text.pack()
        self.text.insert(END, self.df.iloc[self.numque][0])
        self.text

        #permet d'afficher les differents choix 
        self.var1 = IntVar()
        self.rep1=Checkbutton(self.frame_question, text=self.df.iloc[self.numque][1], variable=self.var1, height=2).pack(side=TOP, padx=5, pady=5)
        self.var2 = IntVar()
        self.rep2=Checkbutton(self.frame_question, text=self.df.iloc[self.numque][2], variable=self.var2, height=2).pack(side=TOP, padx=5, pady=5)
        self.var3 = IntVar()
        self.rep3=Checkbutton(self.frame_question, text=self.df.iloc[self.numque][3], variable=self.var3, height=2).pack(side=TOP, padx=5, pady=5)
            


def main():
  
    root=Tk() #initialiser le package tkinter
    app = Fenetre() #programme qui execute tout 
    root.mainloop() #loop du tkinter


if __name__ == '__main__': #lorsque le terminal recoit le nom du programme, il va executer le main
    main() 
