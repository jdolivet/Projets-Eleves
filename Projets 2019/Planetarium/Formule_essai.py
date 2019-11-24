import math

#    'Déclinaison' = dec            dans le catalogue
#    'Ascension droite' = asc

#    'Azimut '=az                   Position de l'étoile à calculer
#    'Hauteur '= hau

#    'Angle Horaire de l étoile '= H = angle - asc + longi
#    'angleH' = angleH
#    'angleT' = angleT

def Calcul_H(asc,angle,longi):
       
    H=angle-asc+longi
    return H

    #Calcul de la Hauteur a faire pour chaque etoile:
    
def Hauteur(dec,lat,H):
        sinushauteur = math.sin(dec) * math.sin(lat) - math.cos(dec) * math.cos(lat) * math.cos(H)
        #La hauteur est un angle compris entre -90° et +90°, la hauteur s obtient donc simplement par :
        hau = math.asin (sinushauteur)
        return hau

    
        #Calcul de l Azimut :

    #Calcul de la Azimut a faire pour chaque etoile:
def Azimut(dec,lat,hau,H):
        cosazimuth = ( math.sin(dec) - math.sin(lat) * math.sin(hau) ) / ( math.cos(lat) * math.cos(hau) )
        #L azimut est un angle compris entre 0 et 360°, nous avons donc besoin d un calcul intermédiaire :
        sinazimuth = ( math.cos(dec) * math.sin (H) ) / math.cos(hau)
        if sinazimuth > 0 :
            az = + math.acos(cosazimuth)
        else :
            az = - math.acos(cosazimuth)

        return az




    # JJ Que si on change la date
def JourJulien(Annee,Mois,Jour):
        if Mois <3 :
            Mois = Mois + 12
            Annee = Annee -1
        A = int( Annee / 100 )
        B = 2 - A + ( A // 4 )
        C = int( 365.25 * Annee )
        D = int( 30.6001 * ( Mois + 1 ) )
        JJ = B + C + D + Jour + 1720994.5
        return JJ


    # Heur Que si on change la date 
def HeureSideral(JJ):
        T = int( JJ - 2451545 ) / 36525
        H1 = 24110.54841 + ( 8640184.812866 * T) + ( 0.093104 * ( T*T ) ) - (0.0000062 * ( T*T*T ) )
        HSH = H1 / 3600
        HS = (( HSH / 24 ) - ( HSH // 24 ))*24
        return HS

def Angle(HS,Heure,Minute) :
        angleH = 2 * math.pi * HS
        angleT = (Heure - 12 + Minute/60 - 4) * 2 * math.pi
        angle = angleH + angleT
        return angle

print(HeureSideral (15521596))

def dista(hau):
    dist = -1000 * ((-2 / math.pi) * hau + 1)
    return dist


def X(dist, az):
    # ne pas oublier de mettre um coeff
    X = dist * math.cos(az)
    return X


def Y(dist, az):
    # ne pas oublier de mettre um coeff
    Y = dist * math.sin(az)
    return Y