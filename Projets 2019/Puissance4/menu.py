from tkinter import *
import finalProjectAi


fenetre = Tk()
fenetre.geometry("600x150+470+200")

# Creation des labels

fenetre.title("MENU")
fenetre["background"] = "blue"
photo = PhotoImage(file="connect4logo.png")


# Design et actions des boutons
def jvsj():
    cpu = False
    finalProjectAi.nouvelle_partie(cpu)


def jvscpu():
    cpu = True
    finalProjectAi.nouvelle_partie(cpu)


bouton3 = Button(fenetre, text="Quit", relief=RAISED, cursor="circle", command=fenetre.destroy, height=2, fg="red",\
                 bg="yellow", activebackground="red", activeforeground="yellow").pack(side= RIGHT, pady=5, padx=10)
bouton1 = Button(fenetre, text="J1 vs J2", relief=RAISED, cursor="circle", command=jvsj, height=2, fg="red", bg="yellow",\
                 activebackground="red", activeforeground="yellow").pack(side=RIGHT, pady=5, padx=5)
bouton2 = Button(fenetre, text="J1 vs IA", relief=RAISED, cursor="circle", command=jvscpu, height=2, fg="red",\
                 bg="yellow", activebackground="red", activeforeground="yellow").pack(side=RIGHT, pady=5, padx=5)

# Positionnement des widgets

canvas = Canvas(fenetre, width=500, height=200, bg="blue", highlightthickness=0)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack(side=LEFT, pady=5)

fenetre.mainloop();




