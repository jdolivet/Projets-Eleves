from tkinter import *
import Formule_essai
import os
import csv
import datetime

HAUTEUR= 2000
LARGEUR=2000

def open_csv():     # Fonctionne sur Windows
    os.startfile('Catalogue5.1.csv') 


class ecran():
    def __init__(self):
        self.hauteur=HAUTEUR
        self.Largeur=LARGEUR
        self.angle=45
        self.azimut=180
        self.ascencion=22


class date:
    def __Init__(self):
        self.today = datetime.datetime.now() 
        self.Annee = today.year
        self.Mois = today.month
        self.Jour = today.day
        self.Heure = today.hour
        self.Minute = today.minute



class lieu:
    def __init__(self):
        self.lat = -37.9
        self.longi = 89.2642


class programe(Frame):
    def __init__(self, root):
        root.title("Menu")
        root.geometry("800x560")
        root.config(background="#0B0B3B")
        #root.iconbitmap("favicon.ico") # Fonctionne sur Windows
        self.Image = PhotoImage(file='stars-964022_960_720.png')
        self.canvas = Canvas(root,width=800, height=337, bg="#FFFFFF", bd=0, highlightthickness=0)
        self.canvas.create_image(0, 0, image=self.Image, anchor= NW)
        self.canvas.grid()
        button_SP = Button(root, text="  São Paulo   ", font=("Arial", 10), bg= "#0B0B3B", fg ="#FFFFFF", command= self.open_window)
        button_SP.grid()
        button_russia = Button(root, text="    Moscou    ", font=("Arial", 10), bg="#0B0B3B", fg="#FFFFFF",command=self.open_Russia)
        button_russia.grid()
        button_Paris = Button(root, text="      Paris       ", font=("Arial", 10), bg="#0B0B3B", fg="#FFFFFF",command=self.open_Paris)
        button_Paris.grid()
        button_Tokyo = Button(root, text="     Tokyo      ", font=("Arial", 10), bg="#0B0B3B", fg="#FFFFFF",command=self.open_Tokyo)
        button_Tokyo.grid()
        button_NY = Button(root, text=" Nova Yorque", font=("Arial", 10), bg="#0B0B3B", fg="#FFFFFF",command=self.open_NY)
        button_NY.grid()
        button1 = Button(root, text="   Catalogue    ",font=("Arial", 10), bg= "#0B0B3B", fg ="#FFFFFF",command= open_csv)
        button1.grid()
        button3 = Button(root, text="    InfoStars    ", font=("Arial", 10), bg="#0B0B3B", fg="#FFFFFF", command=self.open_InfoStars)
        button3.grid()
        button2 = Button(root, text="     Close      ",font=("Arial", 10), bg= "#0B0B3B", fg ="#FFFFFF", command= root.destroy)
        button2.grid()
        self.Ecran=ecran()
        self.Lieu=lieu()
        self.Date=date()
        self.catalogue=self.charger_catalogue()
        print(self.catalogue[1])
        self.position_actuel=[]

    def open_InfoStars(self):
        self.info = Toplevel()
        self.info.title("Information Etoiles")
        #self.info.iconbitmap("favicon.ico")
        self.info.config(background="#0B0B3B")
        self.info.label = Label(self.info, text = "-Grande Ourse; Nom Latin: Ursa Major",bg="#0B0B3B", fg="#FFFFFF",bd=1,relief="solid",font="Arial")
        self.info.label.pack()
        self.info.label = Label(self.info, text="Composé de sept étoiles:Alpha Dubhe,Beta UMa, Phecda, Megrez, Alioth, zeta Ursae Majoris et Alkaid",bg="#0B0B3B", fg="#FFFFFF", bd=1, relief="solid",font="Arial")
        self.info.label.pack()




    def charger_catalogue(self):
        catalogue=[]
        with open("Catalogue5.1.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for lines in csv_reader:
                catalogue.append(lines)

        return(catalogue)

            
    def open_csv(self):
        os.startfile('Catalogue5.csv')

    def create_circle(self, x, y, r,**kwargs):
        return self.canvas.create_oval(x - r, y - r, x + r, y + r,**kwargs)

    def open_Tokyo(self):
        self.top = Toplevel()
        self.top.title("Space")
        #self.top.iconbitmap("favicon.ico")
        self.top.geometry("%dx%d+0+0" % (self.top.winfo_screenwidth(), self.top.winfo_screenheight()))
        self.canvas = Canvas(self.top, width=LARGEUR, height=HAUTEUR, bg="black")
        self.canvas.grid()
        today = datetime.datetime.now()
        Annee = today.year
        Mois = today.month
        Jour = today.day
        Heure = today.hour
        Minute = today.minute

        lat = 35.6894
        longi = 139.692

        # Execution des fonctions a realiser que quand on change la date

        today = datetime.datetime.now()

        JJ = Formule_essai.JourJulien(Annee, Mois, Jour)
        # print(JJ)

        HS = Formule_essai.HeureSideral(JJ)

        angle = Formule_essai.Angle(HS, Heure, Minute)

        with open("Catalogue5.1.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for lines in csv_reader:
                asc = lines[2]
                asc = float(asc)

                dec = lines[3]
                dec = float(dec)

                Vmag = lines[4]
                Vmag = float(Vmag)

                RVB = lines[5]

                # Execution des fonctions a realiser pour chaque etoile

                H = Formule_essai.Calcul_H(asc, angle, longi)

                hau = Formule_essai.Hauteur(dec, lat, H)

                az = Formule_essai.Azimut(dec, lat, hau, H)

                dist = Formule_essai.dista(hau)
                # Angle.(HS,Heure,Minute)
                # print(az)

                X = Formule_essai.X(dist, az)
                Y = Formule_essai.Y(dist, az)

                print(X, Y, Vmag, RVB)

                # tk.Canvas.create_circle = _create_circle

                self.create_circle(X, Y, Vmag, fill=RVB, outline="#DDD", width=0)
                # self.create_circle(X, Y, Vmag)

    def open_NY(self):
        self.top = Toplevel()
        self.top.title("Space")
        #self.top.iconbitmap("favicon.ico")
        self.top.geometry("%dx%d+0+0" % (self.top.winfo_screenwidth(), self.top.winfo_screenheight()))
        self.canvas = Canvas(self.top, width=LARGEUR, height=HAUTEUR, bg="black")
        self.canvas.grid()
        today = datetime.datetime.now()
        Annee = today.year
        Mois = today.month
        Jour = today.day
        Heure = today.hour
        Minute = today.minute

        lat = 40.6643
        longi =  -73.9385

        # Execution des fonctions a realiser que quand on change la date

        today = datetime.datetime.now()

        JJ = Formule_essai.JourJulien(Annee, Mois, Jour)
        # print(JJ)

        HS = Formule_essai.HeureSideral(JJ)

        angle = Formule_essai.Angle(HS, Heure, Minute)

        with open("Catalogue5.1.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for lines in csv_reader:
                asc = lines[2]
                asc = float(asc)

                dec = lines[3]
                dec = float(dec)

                Vmag = lines[4]
                Vmag = float(Vmag)

                RVB = lines[5]

                # Execution des fonctions a realiser pour chaque etoile

                H = Formule_essai.Calcul_H(asc, angle, longi)

                hau = Formule_essai.Hauteur(dec, lat, H)

                az = Formule_essai.Azimut(dec, lat, hau, H)

                dist = Formule_essai.dista(hau)
                # Angle.(HS,Heure,Minute)
                # print(az)

                X = Formule_essai.X(dist, az)
                Y = Formule_essai.Y(dist, az)

                print(X, Y, Vmag, RVB)

                # tk.Canvas.create_circle = _create_circle

                self.create_circle(X, Y, Vmag, fill=RVB, outline="#DDD", width=0)
                # self.create_circle(X, Y, Vmag)

    def open_Paris(self):
        self.top = Toplevel()
        self.top.title("Space")
        #self.top.iconbitmap("favicon.ico")
        self.top.geometry("%dx%d+0+0" % (self.top.winfo_screenwidth(), self.top.winfo_screenheight()))
        self.canvas = Canvas(self.top, width=LARGEUR, height=HAUTEUR, bg="black")
        self.canvas.grid()
        today = datetime.datetime.now()
        Annee = today.year
        Mois = today.month
        Jour = today.day
        Heure = today.hour
        Minute = today.minute

        lat = 48.8667
        longi = 2.33333

        # Execution des fonctions a realiser que quand on change la date

        today = datetime.datetime.now()

        JJ = Formule_essai.JourJulien(Annee, Mois, Jour)
        # print(JJ)

        HS = Formule_essai.HeureSideral(JJ)

        angle = Formule_essai.Angle(HS, Heure, Minute)

        with open("Catalogue5.1.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for lines in csv_reader:
                asc = lines[2]
                asc = float(asc)

                dec = lines[3]
                dec = float(dec)

                Vmag = lines[4]
                Vmag = float(Vmag)

                RVB = lines[5]

                # Execution des fonctions a realiser pour chaque etoile

                H = Formule_essai.Calcul_H(asc, angle, longi)

                hau = Formule_essai.Hauteur(dec, lat, H)

                az = Formule_essai.Azimut(dec, lat, hau, H)

                dist = Formule_essai.dista(hau)
                # Angle.(HS,Heure,Minute)
                # print(az)

                X = Formule_essai.X(dist, az)
                Y = Formule_essai.Y(dist, az)

                print(X, Y, Vmag, RVB)

                # tk.Canvas.create_circle = _create_circle

                self.create_circle(X, Y, Vmag, fill=RVB, outline="#DDD", width=0)
                # self.create_circle(X, Y, Vmag)

    def open_Russia(self):
        self.top = Toplevel()
        self.top.title("Space")
        #self.top.iconbitmap("favicon.ico")
        self.top.geometry("%dx%d+0+0" % (self.top.winfo_screenwidth(), self.top.winfo_screenheight()))
        self.canvas = Canvas(self.top, width=LARGEUR, height=HAUTEUR, bg="black")
        self.canvas.grid()
        today = datetime.datetime.now()
        Annee = today.year
        Mois = today.month
        Jour = today.day
        Heure = today.hour
        Minute = today.minute

        lat = 55.7508
        longi = 37.6172

        # Execution des fonctions a realiser que quand on change la date

        today = datetime.datetime.now()

        JJ = Formule_essai.JourJulien(Annee, Mois, Jour)
        # print(JJ)

        HS = Formule_essai.HeureSideral(JJ)

        angle = Formule_essai.Angle(HS, Heure, Minute)

        with open("Catalogue5.1.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for lines in csv_reader:
                asc = lines[2]
                asc = float(asc)

                dec = lines[3]
                dec = float(dec)

                Vmag = lines[4]
                Vmag = float(Vmag)

                RVB = lines[5]

                # Execution des fonctions a realiser pour chaque etoile

                H = Formule_essai.Calcul_H(asc, angle, longi)

                hau = Formule_essai.Hauteur(dec, lat, H)

                az = Formule_essai.Azimut(dec, lat, hau, H)

                dist = Formule_essai.dista(hau)
                # Angle.(HS,Heure,Minute)
                # print(az)

                X = Formule_essai.X(dist, az)
                Y = Formule_essai.Y(dist, az)

                print(X, Y, Vmag, RVB)

                # tk.Canvas.create_circle = _create_circle

                self.create_circle(X, Y, Vmag, fill=RVB, outline="#DDD", width=0)
                # self.create_circle(X, Y, Vmag)

    def open_window(self):
    
        self.top = Toplevel()
        self.top.title("Space")
        #self.top.iconbitmap("favicon.ico")
        self.top.geometry("%dx%d+0+0" % (self.top.winfo_screenwidth(),self.top.winfo_screenheight()))
        self.canvas = Canvas(self.top,width=LARGEUR, height=HAUTEUR, bg="black") 
        self.canvas.grid()
        today = datetime.datetime.now()
        Annee = today.year
        Mois = today.month
        Jour = today.day
        Heure = today.hour
        Minute = today.minute


        lat = -60
        longi = -90

        # Execution des fonctions a realiser que quand on change la date

        today = datetime.datetime.now()

        JJ = Formule_essai.JourJulien(Annee, Mois, Jour)
        # print(JJ)

        HS = Formule_essai.HeureSideral(JJ)

        angle = Formule_essai.Angle(HS, Heure, Minute)

        with open("Catalogue5.1.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for lines in csv_reader:
                asc = lines[2]
                asc = float(asc)

                dec = lines[3]
                dec = float(dec)

                Vmag = lines[4]
                Vmag = float(Vmag)

                RVB = lines[5]

                # Execution des fonctions a realiser pour chaque etoile

                H = Formule_essai.Calcul_H(asc, angle, longi)

                hau = Formule_essai.Hauteur(dec, lat, H)

                az = Formule_essai.Azimut(dec, lat, hau, H)

                dist = Formule_essai.dista(hau)
                # Angle.(HS,Heure,Minute)
                # print(az)

                X = Formule_essai.X(dist, az)
                Y = Formule_essai.Y(dist, az)

                print(X, Y, Vmag, RVB)

            #tk.Canvas.create_circle = _create_circle

                self.create_circle(X, Y, Vmag, fill=RVB, outline="#DDD", width=0)
                #self.create_circle(X, Y, Vmag)

    def create_Image(self, param, param1, image):
        pass


root=Tk()
app=programe(root)
root.mainloop()




