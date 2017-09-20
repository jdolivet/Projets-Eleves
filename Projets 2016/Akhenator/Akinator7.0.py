

# -*- coding: utf-8 -*-
from tkinter import * 
import csv
import random
class Fenetre:


        def __init__(self,master): 

            self.Creation_Interface()                
           ### self.TABLEAUself.compteur=0

        def Creation_Interface(self): ## Creation de l'interface du menu.
            root.title('Akinator')
            root.resizable(width=False, height=False)
            self.compteur=0


            self.canvas1 = Canvas(root,width=500, height=500)
            self.photo = PhotoImage(file ="Files/Salut2.png") ## ouverture de la photo du genie Akinator.
            self.canvas1.create_image(250, 250, image =self.photo)
            self.canvas1.pack()
            						##Creation des boutons pour choisir le mode de jeu (Term S ou Pays de l'Euro).

            self.bouton_Terms = Button(root, text="Jouer Terminales S", width=20,height=2, bg="green", command=lambda: self.Play("Term"))
            self.bouton_Terms.pack(side= RIGHT, padx=30, pady=5)

            self.bouton_Europe = Button(root, text="Jouer Pays de l'UE",width=20, height=2, bg="blue",command=lambda: self.Play("Euro"))
            self.bouton_Europe.pack(side= LEFT, padx=30, pady=5)

            self.bouton_quitter = Button(root, text="Quitter",width=20, height=2, bg="red", command=self.Quitter)
            self.bouton_quitter.pack(side= BOTTOM, padx=30, pady=5)

             
        def Play(self,choix):
        					##Creation de la fenetre de jeu avec l'utilisateur.
            
            self.Questions = Toplevel(root)
            self.Questions.transient(root)
            self.Questions.resizable(width=False, height=False)
            
            self.canvas2 = Canvas(self.Questions, width=800, height=200, bg='ivory')
            self.canvas2.pack(side=TOP, padx=5, pady=5)
            				##Creation des boutons "Oui","Non" et "Je ne sais pas", pour interagir avec l'utilisateur.
            
            self.bouton1 = Button(self.Questions, text ="Oui", width=7, height=1, bg="green")
            self.bouton2 = Button(self.Questions, text ="Non", width=7, height=1, bg="red", command =lambda: self.Interpreterreponse(question, "non"))
            self.bouton3 = Button(self.Questions, text ="Je sais pas", width=7, height=1, bg="blue", command =lambda: self.Interpreterreponse(question, "nsp"))
  
            self.bouton1.pack(side=LEFT, padx=10, pady=7)
            self.bouton2.pack(side=RIGHT, padx=10, pady=7)
            self.bouton3.pack(side=BOTTOM, padx=10, pady=7)
            
            self.Chargertableau(choix)
            self.PlayGame()                 
                
            
        def Chargertableau(self,choix) :
        

            if choix=="Term":
                tableau = "Files/Tableau_Akinator.csv"
            if choix=="Euro":
                tableau = "Files/Tableau_UE.csv"
            fichier = open(tableau,"r")
            reader = csv.reader(fichier, delimiter=",")
            self.TABLEAU = list(reader)
            self.taille_ligne= len(self.TABLEAU[1])
            self.taille_colonne= len(self.TABLEAU)
            self.NombreJsp= 0
            self.compteur=0

        def PlayGame(self):                 ##Fonction intermediaire pour eviter de charger plusieur fois le tableau.
            self.Choisirquestion()
            

        def Choisirquestion(self) :
      
            personnespossibles=0     ###colonne droite du tableau, question: "Votre personne n'a pas été eliminée?"
            for row in self.TABLEAU:
                if row[self.taille_ligne-1]=='1':  
                    personnespossibles+=1
      
            totaux=[]    ##liste totaux de reponse oui par question
            for j in range (1,self.taille_ligne-1):
                TtParQuest=0  
                for row in self.TABLEAU:
                    if row[self.taille_ligne-1]=='1' and row[j]=='1': ##pour une question, si la reponse est Oui
                    												  ##et que la personne n'a pas ete eliminee, aditionner 1 au totaux
                        TtParQuest+=1
                totaux.append(TtParQuest)  ##definir totaux par question

            for i in range(1,len(totaux)):  
                if self.TABLEAU[self.taille_colonne-1][i]=='1':
                    totaux[i-1]=0   ### pour que des questions deja posees soient evites (derniere ligne pour les questions deja posees)
            
            index_a_choisir=[]		##liste de questions considerees optimales de la quelle va se prendre une au hazard
            compt=1
            for i in totaux:
                if i>0.3*personnespossibles and i<0.7*personnespossibles:  ##afin de choisir des questions qui eliminent une bonne part
                    index_a_choisir.append(compt)						## des personnes encore possibles
                compt+=1
            

            if index_a_choisir==[]: 	### si il n' ya pas de questions optimales, nous voulons au moins une question qui élimine quelqu'un						
                valeur=0
                while valeur==0 or valeur==personnespossibles: ## questions où tout le monde repond Oui ou NOn
                        valeur=(random.choice(totaux))
                        indicequestion=totaux.index(valeur)  ##indice de la question sur le tableau
            else:
                indicequestion=(random.choice(index_a_choisir)) ##choix aleatoire dans liste des optimales 

            self.TABLEAU[self.taille_colonne-1][indicequestion]='1'  ##garder en memoire que la question a ete posee

            self.afficherQuestion(indicequestion)  

        def afficherQuestion(self, question):
            

            if self.NombreJsp<3: 
                self.compteur+=1
            
                self.canvas2.delete("all")         ## Vider entierement le tableau, pour ne pas rajouter plusieur fois la même chose.
            
                txt2= self.canvas2.create_text(400, 25, text='Question nº', font="Arial 16 italic",fill="blue")
                txt2= self.canvas2.create_text(465, 25, text=self.compteur, font="Arial 16 italic",fill="blue")     
                txt = self.canvas2.create_text(400, 100, text=self.TABLEAU[0][question], font="Arial 16 italic",fill="blue")
                self.bouton1.config(command=lambda: self.Interpreterreponse(question, "oui"))
                self.bouton2.config(command=lambda: self.Interpreterreponse(question, "non"))
                self.bouton3.config(command=lambda: self.Interpreterreponse(question, "nsp"))
            else:
                
                self.fin_du_jeu("Tropdejsaispas")
                
    		
        def Interpreterreponse(self, question, reponse) :

            
            if reponse == "oui" :									##SI reponse de la personne est oui 
                    for row in self.TABLEAU :						#déconsidère tout ceux repondant non dans le tableau
                            if row[question] == "0":
                                row[self.taille_ligne-1] = "0"

            if reponse == "non" :
                    for row in self.TABLEAU:
                            if row[question] == "1" :
                                row[self.taille_ligne-1] = "0"
            if reponse== "nsp":										##Compteur pour fin alternative, 
                self.NombreJsp+=1									## si utilisateur est un mauvais joueur

            personnespossibles=0
            for row in self.TABLEAU:
                if row[self.taille_ligne-1]=='1':
                    personnespossibles+=1						##recompte le nombre de personnes qui peuvent etre 
                        											## l'inconnu que le programme doit deviner
            if personnespossibles==1:
                for i in range (1,self.taille_colonne-1):			##si il reste qu'une seule option, inconnu trouvé
                    if self.TABLEAU[i][self.taille_ligne-1]=='1':
                        indicepersonne=i
                self.fin_du_jeu(indicepersonne)						##donc, appel de ça fonctiond de fin du jeu

            else:
                self.PlayGame()


        def fin_du_jeu(self,indicepersonne) :  ## Creation de la fenetre de fin de jeu.
            self.Questions.destroy()

            self.Fin = Toplevel(root)
            self.Fin.transient(root)
            self.Fin.resizable(width=False, height=False)
            
            self.canvas3 = Canvas(self.Fin, width=626, height=352, bg='ivory')
            self.canvas3.pack(side=TOP, padx=5, pady=5)

            if indicepersonne=="Tropdejsaispas":

            	self.photo2 = PhotoImage(file ="Files/JonSnow.png") 
            	self.canvas3.create_image(313,176, image =self.photo2)

            else:
                txt1 = self.canvas3.create_text(300, 50, text="Vous pensez a :",font="Arial 16 italic", fill="blue")
                txt2 = self.canvas3.create_text(300, 100, text=self.TABLEAU[indicepersonne][0], font="Arial 16 italic", fill="blue")
                txt3 = self.canvas3.create_text(300, 200, text="Nombre de questions posees :",font="Arial 16 italic", fill="blue")
                txt4 = self.canvas3.create_text(300, 250, text=self.compteur, font="Arial 16 italic", fill="blue")
            self.bouton_quitter = Button(self.Fin, text="Quitter",width=20, height=2, bg="red", command=self.Quitter)
            self.bouton_quitter.pack(side= LEFT, padx=30, pady=5)
            self.bouton_rejouer = Button(self.Fin, text="Rejouer",width=20, height=2, bg="green", command=self.rejouer)
            self.bouton_rejouer.pack(side=RIGHT , padx=30, pady=5)


            


            

        def rejouer(self):
            self.Fin.destroy()
            self.compteur=0

            
            
            
        def Quitter(self):

            f = Toplevel(root,background='ivory' )
             
            f.transient(root)  
            f.grab_set()            

            f.geometry("+%d+%d" % (root.winfo_rootx()+100, root.winfo_rooty()+100))
            Label(f,text ="VOULEZ VOUS QUITTER ?",justify= CENTER,background='ivory',padx=10, pady=10).pack()
            Button(f, text=" OUI",background='green', command=root.destroy).pack(side=RIGHT, padx=20, pady=10)
            Button(f, text=" NON",background='red', command=f.destroy).pack(side=RIGHT, padx=0, pady=10)
            


global root
root =Tk()



FENETRE=Fenetre(root)




root.mainloop()
