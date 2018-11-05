class Application:
	
	def __init__(self,root):
		"""Constructeur de la fenetre principale"""

		root.title('Le Jeu du Takin')

		self.canvas = Canvas(root, width=700, height=500, background="purple")

		self.texte = self.canvas.create_text(350, 250, text="Le Jeu du Takin", font="Verdana 16 bold underline", fill="white")

		self.canvas.pack()
		
		self.Placement=[]

		bouton1=Button(root, text="jouer",command=self.Play).pack()

		bouton2=Button(root, text="instructions", command=self.Instruction).pack()

		bouton3=Button(root, text="Quitter", command=root.destroy).pack()
		
		Fichier_Image= ["numero1takin.gif", "numero2takin.gif", "numero3takin.gif" ,"numero4takin.gif","numero5takin.gif","numero6takin.gif","numero7takin.gif","numero8takin.gif"]
		
		self.Image =[]
		
		for fichier in Fichier_Image:
			self.Image.append(PhotoImage(file=fichier))

	


	def Play(self):
		
		"""Fonction activer quand on appuie sur le bouton jouer"""

		print("jouez")
		
		self.canvas.create_rectangle(150, 50, 550, 450, fill= 'black', outline= 'white', width= 1)
		
		self.Placement=self.tirage()

		self.afficher()
		
		self.canvas.focus_set()
		
		self.canvas.bind('<Key>', self.Evenements)



	

	def Instruction(self):

		"""Fonction activer quand on appuie sur le bouton Instruction"""
		
		print("instruction")





	def tirage(self):

		"""Tirage au sort de l'ordre des numeros"""
		
		Objets= [0, 1, 2, 3, 4, 5, 6, 7, 8]

		self.placement= []
		
		for i in range(0,3):
			
			self.placement.append([0 for j in range(0,3)])

		
		for i in range(0,3):
			
			for j in range(0,3):
				
				tirage= random.choice(Objets)
				
				Objets.remove(tirage)
				
				self.placement[i][j]=tirage
				
				if tirage == 0:
					
					self.Y0 = i
					
					self.X0 = j
		
		print('X0=', self.X0, 'Y0=', self.Y0)

		return self.placement 





	def afficher(self):

		"""Fonction permettant d'afficher dans un cadre les numeros tires au sort"""

		self.canvas.delete(ALL)

		self.canvas.create_rectangle(150, 50, 550, 450, fill= 'black', outline= 'white', width= 1)

		for i in range(0,3):
			
			for j in range(0,3):
				
				print(self.Placement[i][j])
				
				if self.Placement[i][j] != 0:

					self.canvas.create_image(217 + j*133 , 117 + i*133, image= self.Image[self.Placement[i][j]-1])

		self.Gagner()
			
	


	def Gagner(self):
		# Est ce que c'est gagne ?

		if self.Placement == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
			
			showinfo('Fini', 'Vous avez gagne !')




	def Evenements(self,event):
		
		"""Fonction permettant le mouvement des cases (grace aux fleches du clavier)"""

		touche = event.keysym
		
		print(touche)
		
		

		if touche == "Right":
		
			print(touche)
		
			if self.X0 >= 0 :
		
				self.a0 = self.Placement[self.Y0][self.X0-1]
		
				print ('a0',self.a0)
		
				self.b0 = self.Placement[self.Y0][self.X0]
		
				print ('b0',self.b0)
		
				self.Placement[self.Y0][self.X0] = self.a0 
		
				self.Placement[self.Y0][self.X0-1] = self.b0
				
				self.X0 = self.X0-1
		
				self.Y0 = self.Y0

			print (self.X0, self.Y0)
	

		
		if touche == "Left":

			print(touche)

			if self.X0 >= 0:

				self.a0 = self.Placement[self.Y0][self.X0+1]

				print('a0', self.a0)

				self.b0 = self.Placement[self.Y0][self.X0]

				print('b0', self.b0)

				self.Placement[self.Y0][self.X0] = self.a0 
		
				self.Placement[self.Y0][self.X0+1] = self.b0
				
				self.X0 = self.X0+1
		
				self.Y0 = self.Y0

			print (self.X0, self.Y0)
	


		if touche == "Up":

			print(touche)

			if self.Y0 >= 0:

				self.a0 = self.Placement[self.Y0+1][self.X0]

				print('a0', self.a0)

				self.b0 = self.Placement[self.Y0][self.X0]

				print('b0', self.b0)

				self.Placement[self.Y0][self.X0] = self.a0 
		
				self.Placement[self.Y0+1][self.X0] = self.b0
				
				self.X0 = self.X0
		
				self.Y0 = self.Y0+1

			print (self.X0, self.Y0)
	


		if touche == "Down":

			print(touche)

			if self.Y0 >= 0:

				self.a0 = self.Placement[self.Y0-1][self.X0]

				print('a0', self.a0)

				self.b0 = self.Placement[self.Y0][self.X0]

				print('b0', self.b0)

				self.Placement[self.Y0][self.X0] = self.a0 
		
				self.Placement[self.Y0-1][self.X0] = self.b0
				
				self.X0 = self.X0
		
				self.Y0 = self.Y0-1

			print (self.X0, self.Y0)
		

		self.afficher()





# Programme principal :
from tkinter import *

from tkinter.messagebox import *

import random 

root=Tk()

f = Application(root)    # instanciation de l'objet application

root.mainloop()
