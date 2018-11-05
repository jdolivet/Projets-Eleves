from tkinter import *
from tkinter.messagebox import *
import random


global couleurs
couleurs = ["red","green","blue","yellow","orange","pink"]
global couleurs_fr
couleurs_fr = ["rouge"," vert","bleu","jaune","orange","rose"]
global initiales_couleurs
initiales_couleurs = [couleurs[i][0] for i in range(len(couleurs))]
global longueur_combinaison
longueur_combinaison = 5
global nbmaxtentatives
nbmaxtentatives = 10

global HAUTEUR
HAUTEUR= 1000 ########################################
global LARGEUR
LARGEUR= 1000########################################

global COLORS
COLORS = ["red","green","blue","yellow","orange","pink"]

              
global NB_EMPLACEMENTS
NB_EMPLACEMENTS = 4


class Fenetre(Tk):
 

        def __init__(self, *args, **kwargs): 

            Tk.__init__(self, *args, **kwargs) 
            row_offset = 1
            self.title("Mastermind Game")
            # Création du canvas
            self.canvas = Canvas(width=LARGEUR, height=HAUTEUR, background="#FFFFCC")
            self.canvas.pack(fill="both", expand=True)
            self.Creation_Interface()
            self.line_doing =0
            self.compteur =[]
            self.init_compteur()
            self.list_lab =[]
            self.has_ended= False


           
            

        def Creation_Interface(self): ## Creation de l'interface du menu.


            			##Creation des boutons pour choisir le mode de jeu (instructions, jouer, quitter).
            self.canvas.create_rectangle(0,0,10000, 10000, fill="black")
            
            self.bouton_jouer = Button(self.canvas, text="Je devine", bg="yellow", fg="#66A7CC", relief=FLAT, font=("cambria", 14, 'bold'), command= self.initUI)
            self.bouton_jouer.place(x="100", y="750", anchor=CENTER)
            
            self.bouton_jouerO = Button(self.canvas, text="L'ordinateur devine", bg="yellow", fg="#66A7CC", relief=FLAT, font=("cambria", 14, 'bold'), command= self.ordi)
            self.bouton_jouerO.place(x="310", y="750", anchor=CENTER)

            self.bouton_instructions = Button(self.canvas, text="Instructions", bg="yellow", fg="#66A7CC", relief=FLAT, font=("cambria", 14, 'bold'),command=self.Instructions)
            self.bouton_instructions.place(x="530", y="750", anchor=CENTER)

            self.bouton_quitter = Button(self.canvas, text="Quitter",bg="yellow", fg="#66A7CC", relief=FLAT, font=("cambria", 14, 'bold'), command=self.Quitter)
            self.bouton_quitter.place(x="700", y="750", anchor=CENTER)
                
            self.photo = PhotoImage(file ="PHOTO.ppm") ## ouverture de la photo du MASTERMIND
            self.canvas.create_image(420, 350, image =self.photo)
            self.canvas.pack()

        def initUI(self):       #actions lorsqu'on clique sur 'jouer' 

            
            self.bouton_jouer.destroy()
            self.bouton_instructions.destroy()
            self.bouton_jouerO.destroy()
            self.bouton_quitter.destroy()
            self.canvas.delete("all")
            self._create_token()
            self.creer_combinaison_secrete()
            self.line_doing =0
            self.compteur =[]
            self.init_compteur()
            self.has_ended= False

            
        def initUI_2(self):
                #remise à zéro de toutes les variables pour commencer une nouvelle partie
        
            self.line_doing =0
            for lab in self.list_lab:
                 lab.destroy()
            #compteur represente le tableau de jeu
            self.compteur =[]
            self.init_compteur()
            self.bouton_rejouer.destroy()
            self.canvas.delete("all")
            self.bouton_1.destroy()
            self.bouton_2.destroy()
            self.bouton_3.destroy()
            self.bouton_4.destroy()
            self.bouton_5.destroy()
            self.bouton_validation.destroy()
            self._create_token()
            self.creer_combinaison_secrete()
            self.has_ended= False


        def _create_token(self):
 
                for x in range(5):
                        for y in range(10):
                               self.canvas.create_oval(int(LARGEUR*(1+x)/10)
                                        , int(HAUTEUR*(1+y)/16)
                                        , int(LARGEUR*(1+x)/10 + (LARGEUR/10)*(1/2))
                                        , int(HAUTEUR*(1+y)/16 + (LARGEUR/10)*(1/2))
                                        , outline="black"
                                        , fill="gray"
                                        , width=5)


                
                y=10.5
                self.bouton_1 = Button(self.canvas, command = lambda: self.change_color(0))
                self.bouton_1.place(x="125", y=int(HAUTEUR*(1+y)/16), anchor=CENTER)
                self.bouton_2 = Button(self.canvas, command = lambda: self.change_color(1))
                self.bouton_2.place(x="225", y=int(HAUTEUR*(1+y)/16), anchor=CENTER)
                self.bouton_3 = Button(self.canvas, command = lambda: self.change_color(2))
                self.bouton_3.place(x="325", y=int(HAUTEUR*(1+y)/16), anchor=CENTER)
                self.bouton_4 = Button(self.canvas, command = lambda: self.change_color(3))
                self.bouton_4.place(x="425", y=int(HAUTEUR*(1+y)/16), anchor=CENTER)
                self.bouton_5 = Button(self.canvas, command = lambda: self.change_color(4))
                self.bouton_5.place(x="525", y=int(HAUTEUR*(1+y)/16), anchor=CENTER)
                self.bouton_validation = Button(self.canvas, text="Valider", bg="yellow", fg="#66A7CC", relief=FLAT, font=("cambria", 14, 'bold'), command=self.Validation)
                self.bouton_validation.place(x="650", y=int(HAUTEUR*(1+y)/16), anchor=CENTER)
                self.bouton_menu = Button(self.canvas, text="Menu", bg="yellow", fg="#66A7CC", relief=FLAT, font=("cambria", 14, 'bold'), command=self._retour_menu)
                self.bouton_menu.place(x="50", y="40", anchor=CENTER)
        
        def init_compteur(self):
            for i in range(10):
                    self.compteur.append([-1]*5)


        def _retour_menu(self):
                
                for lab in self.list_lab:
                        lab.destroy()

                if self.has_ended:
                        self.bouton_rejouer.destroy()
                self.line_doing=0
                self.init_compteur()
                self.canvas.delete("all")
                self.bouton_1.destroy()
                self.bouton_2.destroy()
                self.bouton_3.destroy()
                self.bouton_4.destroy()
                self.bouton_5.destroy()
                self.bouton_validation.destroy()
                self.bouton_menu.destroy()
                self.Creation_Interface()
        

        def Instructions(self):
                #Creation de la fenetre d'instructions

            f=Toplevel(background='ivory' )
            f.transient()           #reste au premier plan
            f.grab_set()                        #inactive la fenêtre parent
            f.geometry("1100x700") 
            file = open('instructions.txt','r')      
                                            # lecture dans le fichier avec la méthode read()
            texte=file.read()
            file.close()
            Label(f,text =texte, justify= CENTER,background='ivory',padx=10, pady=10).pack()
            

            Button(f, text=" Quitter",background='light blue', command=f.destroy).pack(side=RIGHT, padx=10, pady=10)


         

                            
        def change_color(self, column):       #Change la couleur du rond de la première colonne
                line = self.line_doing
                self.compteur[line][column] = (self.compteur[line][column] + 1) % len(COLORS)
                self.canvas.create_oval(int(LARGEUR*(1+column)/10)
                                        , int(HAUTEUR*(1+line)/16)
                                        , int(LARGEUR*(1+column)/10 + (LARGEUR/10)*(1/2))
                                        , int(HAUTEUR*(1+line)/16 + (LARGEUR/10)*(1/2))
                                        , outline="black"
                                        , fill=COLORS[self.compteur[line][column]]
                                        , width=5)
                                

                
        def creer_combinaison_secrete(self) : #crée une chaine de caractères avec un certains nombre de couleurs

                self.combinaison_secrete = []
                for i in range (0, longueur_combinaison) :
                        self.combinaison_secrete.append(random.randint(0, len(initiales_couleurs)-1))


        def comparer_combinaison(self):
                nb_couleurs_bien_placees = 0
                nb_couleurs_mal_placees = 0
                initiales_couleurs_entrees =self.compteur[self.line_doing].copy()
                initiales_couleurs_secretes = self.combinaison_secrete.copy()
        
                for i in range(len(initiales_couleurs_entrees)): 
                        if initiales_couleurs_entrees[i] == initiales_couleurs_secretes[i] :
                                nb_couleurs_bien_placees+=1
                                initiales_couleurs_entrees[i]='x' 

                for i in range(0,len(initiales_couleurs_entrees)) : 
                        if initiales_couleurs_entrees[i] in initiales_couleurs_secretes : 
                                if initiales_couleurs_entrees[i] != 'x' : 

                                        nb_couleurs_mal_placees+=1
                                        couleur_actuelle=initiales_couleurs_entrees[i]
                                        j=initiales_couleurs_secretes.index(couleur_actuelle)
                                        initiales_couleurs_secretes[j]='x'

                                        
                 #Création de variables qui peuvent s'actualiser (avec le bouton valider)
                self.a=StringVar()
                self.a.set(nb_couleurs_bien_placees)
                self.b=StringVar()
                self.b.set(nb_couleurs_mal_placees)
                self.c=StringVar()
                self.c.set(' - '.join([couleurs_fr[color] for color in self.combinaison_secrete]))

                # label des biens places 
                lLab = Label(self.canvas, text=str(nb_couleurs_bien_placees), bg="#FFFFCC")
                lLab.config(font=("Courier", 23))
                lLab.place(x= int(LARGEUR*6/10) #pour mettre a la fin de la ligne
                           , y= (int(HAUTEUR*(1+self.line_doing)/16)+int(HAUTEUR*(1+self.line_doing+1)/16))/2-5, anchor=CENTER) # pour mettre (au mileu de la line doing et line doing+1 )- 5 pixels
                self.list_lab.append(lLab)

                
                 # label des mals places 
                lLab = Label(self.canvas, text=str(nb_couleurs_mal_placees), bg="#FFFFCC")
                lLab.config(font=("Courier", 23))
                lLab.place(x= int(LARGEUR*6/10)+50 #pour mettre a la fin de la ligne
                           , y= (int(HAUTEUR*(1+self.line_doing)/16)+int(HAUTEUR*(1+self.line_doing+1)/16))/2-5, anchor=CENTER) # pour mettre (au mileu de la line doing et line doing+1 )- 5 pixels
                self.list_lab.append(lLab)
 

                # labels

                lLab = Label(self.canvas, text="Nombre de couleurs bien placees : ", bg="#FFFFCC")
                lLab.place(x=int(LARGEUR*8/10), y="385", anchor=CENTER)
                self.list_lab.append(lLab)
                lLab = Label(self.canvas, text="Nombre de couleurs mal placees : ", bg="#FFFFCC")
                lLab.place(x=int(LARGEUR*8/10), y="415", anchor=CENTER)
                self.list_lab.append(lLab)
                
                lLab = Label(self.canvas, textvariable=self.a, bg="#FFFFCC")
                lLab.place(x="920", y="385", anchor=CENTER)
                self.list_lab.append(lLab)
                
                lLab = Label(self.canvas, textvariable=self.b, bg="#FFFFCC")
                lLab.place(x="920", y="415", anchor=CENTER)
                self.list_lab.append(lLab)
                
               
                # A rajouter si on veut afficher la combinaison en haut a droite

                #lLab =Label(self.canvas, text="La combinaison secrete est : ", bg="#FFFFCC")
                #lLab.place(x="700", y="30", anchor=CENTER)
                #self.list_lab.append(lLab)
                
                #lLab = Label(self.canvas, textvariable=self.c)
                #lLab.place(x="812", y="30", anchor=CENTER)
                #self.list_lab.append(lLab)

                # En cas de victoire ou perte
                if nb_couleurs_bien_placees == 5 or self.line_doing == 9:
                        self.has_ended = True
                        self.bouton_rejouer = Button(self.canvas, text = "Rejouer" , bg="gray", fg = "#66A7CC", relief=FLAT, font=("cambria", 14, 'bold'), command = self.initUI_2)
                        self.bouton_rejouer.place(x="50", y="70", anchor=CENTER)
                        lLab = Label(self.canvas
                                     , text="Vous avez gagné !" if nb_couleurs_bien_placees == 5 else "Vous avez perdu... Retentez ! "
                                     , bg="white")
                        lLab.place(x="500", y="350", anchor=CENTER)
                        lLab.config(font=("Courier", 25))
                        self.list_lab.append(lLab)
                
                # Affichage de la combinaison en cas de perte
                if self.line_doing == 9:
                        lLab =Label(self.canvas, text="La combinaison secrète était : ", bg="white")
                        lLab.place(x="500", y="380", anchor=CENTER)
                        lLab.config(font=("Courier", 25))
                        self.list_lab.append(lLab)
                        
                        lLab = Label(self.canvas, textvariable=self.c , bg="white")
                        lLab.place(x="490", y="410", anchor=CENTER)
                        lLab.config(font=("Courier", 25))
                        self.list_lab.append(lLab)

      
                                                                                                                                                                                                                                                                                                                                                                    
        def Validation(self):     
                self.comparer_combinaison()           
                self.line_doing +=1

        def Quitter(self):

                f = Toplevel(self.canvas,background='ivory' )
             
                f.transient(self.canvas)  
                f.grab_set()            

                f.geometry("+%d+%d" % (self.canvas.winfo_rootx()+100, self.canvas.winfo_rooty()+100))
                Label(f,text ="VOULEZ VOUS QUITTER ?",justify= CENTER,background='ivory',padx=10, pady=10).pack()
                Button(f, text=" OUI",background='green', command=self.canvas.destroy).pack(side=RIGHT, padx=20, pady=10)
                Button(f, text=" NON",background='red', command=f.destroy).pack(side=RIGHT, padx=0, pady=10)                       


        def ordi(self):
            ORDI=Ordi_devine()

#############################     2e mode de jeu      ##########################################################


class Ordi_devine():
        
          
        def __init__(self): 

                #Creation de la fenetre de l'ordinateur devine

            self.f=Toplevel(background='#FFFFCC' )
            self.f.transient()           #reste au premier plan
            self.f.grab_set()            #inactive la fenêtre parent                                           

            self.f.geometry("900x600") 

            row_offset = 1
            entryLabel = Label(self.f, bg="#FFFFCC")
            entryLabel["text"] = "Bien placées:"
            entryLabel.grid(row=row_offset, sticky=E, padx=5, column=NB_EMPLACEMENTS + 4)
            self.entryWidget_both = Entry(self.f)
            self.entryWidget_both["width"] = 5
            self.entryWidget_both.grid(row=row_offset, column=NB_EMPLACEMENTS + 5)
            self.entries = {'bien_place':self.entryWidget_both}


            entryLabel = Label(self.f, bg="#FFFFCC")
            entryLabel["text"] = "Mal placées:"
            entryLabel.grid(row=row_offset+1, sticky=E, padx=5,column= NB_EMPLACEMENTS + 4)
            self.entryWidget_only_colours = Entry(self.f)
            self.entryWidget_only_colours["width"] = 5
            self.entryWidget_only_colours.grid(row=row_offset+1, column=NB_EMPLACEMENTS + 5)
            self.entries['mal_place'] = self.entryWidget_only_colours

            bouton_valider = Button(self.f, text="Valider", bg="#FFFFCC", command=self.nvlle_proposition_tk)
            bouton_valider.grid(row=4,column=NB_EMPLACEMENTS + 4)

            bouton_quitter = Button(self.f, text="Quitter", bg="#FFFFCC", command=self.f.quit)
            bouton_quitter.grid(row=4,column=NB_EMPLACEMENTS + 5)
            


            self.list_poss = self.create_list() # fait la liste de toutes les possibilités de combinaison
            self.last_guess = self.list_poss[random.randrange(0, len(self.list_poss))] # choisi une des combinaisons possibles au hasard

 
            self.montre_proposition_actuelle(self.last_guess)
            self.propositions = []

           
        def first_guess(self):
                return self.last_guess

        def nvlle_proposition_tk(self):
                mal = self.entries['mal_place'].get() if len(self.entries['mal_place'].get())>0 else 0
                bien = self.entries['bien_place'].get() if len(self.entries['bien_place'].get())>0 else 0
                try:
                        mal = int(mal)
                        bien = int(bien)
                except Exception:
                        showinfo("Erreur"," Vos entrées sont non numériques !")
                        return -1
                self.propositions.append([self.last_guess, [bien, mal]])
                self.last_guess = self.make_guess(mal, bien)
                self.montre_proposition_actuelle(self.last_guess)
                self.affiche_propositions()

        def montre_proposition_actuelle(self, last_guess):
            #creation de l'interface avec les carrés de couleurs des combinaisons
            row = 1 
            Label(self.f, text="   Nouvelle proposition:   ", bg="#FFFFCC").grid(row=row, column=0, columnspan=4)
            row +=1
            col_count = 0
            for index_cor in last_guess:
                 l = Label(self.f, text="    ", bg=couleurs[index_cor])
                 l.grid(row=row,column=col_count,  sticky=W, padx=2)
                 col_count += 1

                 

        def affiche_propositions(self):
            row = 3
            Label(self.f, text="Anciennes propositions", bg="#FFFFCC").grid(row=row,column=0, columnspan=4)
            Label(self.f, text="Bien placées", bg="#FFFFCC").grid(row=row, padx=5, column=NB_EMPLACEMENTS + 1)
            Label(self.f, text="Mal placées", bg="#FFFFCC").grid(row=row,padx=5, column=NB_EMPLACEMENTS + 2)


            for proposition in self.propositions:
              guessed_colours = proposition[0]
              col_count = 0
              row += 1
            for index_cor in guessed_colours:
                 l = Label(self.f, text="    ", bg=couleurs[index_cor])
                 l.grid(row=row,column=col_count,  sticky=W, padx=2)
                 col_count +=1
              # evaluation:
            for i in (0,1):
                l = Label(self.f, text=str(proposition[1][i]), bg="#FFFFCC")
                l.grid(row=row,column=col_count + i, padx=2)


 
### 3 méthodes pour faire liste de toutes les possibles combinaisons 
######## Methode recursive - plus efficace et avantageuse - celle que l'on va utiliser                                                                                                                        
        def create_list(self):
                # creer la liste de toutes les possibilites recursivement temps d'un appel: 0.006023782253265381 s
                return self.rec_create_list([], 0) 

            
        def rec_create_list(self, initial, length): 
            if(length > NB_EMPLACEMENTS):
                return [initial]
            to_return =[]
            for i in range(len(couleurs)):
                    to_return = to_return+ self.rec_create_list(initial+[i], length+1)
            return to_return

########### Methodes alternatives:mais finalement non utilisees dans programme

                #return self.faire_list_poss()
                #return self.boucles_list()

        def faire_list_poss(self): # temps d'un appel: 0.020677037239074707 s
                to_return = list()
                for i in range(pow(10, NB_EMPLACEMENTS)): # #creer la liste de toutes les possibilites en partant de la liste des entiers entre 0 et pow(10,nb_emplacement) 
                        if(True not in [int(i)>=len(couleurs) for i in list(str(i))]): # elemine tous les nombres qui ont au moins numero > nb_couleurs
                                to_list = list(str(i))
                                to_list = ['0']*(NB_EMPLACEMENTS - len(to_list)) + to_list
                                to_return.append([int(x) for x in to_list]) #sinon on les met dans la liste des combinaisons possibles
                return to_return 


        def boucles_list(self): # temps d'un appel : 0.00250466609001 s 
                to_return = []
                for i in range(len(couleurs)):
                        for j in range(len(couleurs)):
                                for k in range(len(couleurs)):
                                        for l in range(len(couleurs)):
                                                for m in range(len(couleurs)):
                                                        to_return.append([i,j,k,l,m])
                return to_return

############

        def check_guess(self, nb_mal_place, nb_bien_place): 
                new_list = [] 
                for poss in self.list_poss: 
                        if(self.check_poss(poss.copy(), nb_mal_place, nb_bien_place)): 
                                new_list.append(poss) # si check_poss retourne True on la rajoute à la nouvelle liste
                if(len(new_list)==0):
                        return -1
                else:
                        self.list_poss = new_list.copy()

                                

        def check_poss(self, poss, nb_mal_place, nb_bien_place):  
                me_mal_place = 0
                me_bien_place = 0
                me_poss = poss.copy()
                guess= self.last_guess.copy()
                for i in range(NB_EMPLACEMENTS):
                        if(me_poss[i] == guess[i]):
                                me_bien_place +=1
                                guess[i] = -1
                                me_poss[i] = -1

                                
                for i in range(len(guess)):
                        for j in range(len(guess)):
                                if(me_poss[j] == guess[i] and guess[i] != -1 and me_poss[j] != -1): 
                                        me_mal_place +=1
                                        guess[i] = -1
                                        me_poss[j] = -1
                                        
                if(nb_mal_place != me_mal_place):
                        return False
                if(nb_bien_place != me_bien_place):
                        return False
                return True

        def make_guess(self, nb_mal_place, nb_bien_place):
                if(self.check_guess(nb_mal_place, nb_bien_place) == -1):
                        showinfo("Erreur"," Vos propositions sont incohérentes!")
                self.last_guess = self.list_poss[random.randrange(0, len(self.list_poss))]
                print(len(self.list_poss))
                return self.last_guess

    ########### en ce qui concerne l'interface :
           
       
           
if __name__ == "__main__":
    app = Fenetre()
    app.mainloop()
