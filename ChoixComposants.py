# -*- coding: utf-8 -*-
# Python v3

def combinaisons():
    #On utilise le format [nom,poids,puissance,durée proto,durée présérie,qualité,prix proto,prix présérie]]
    ecran = [["VisionPlus",200,400,1,3,18,310,210],["MagicScreen",300,450,4,2,24,390,285],["BildPix",150,370,2,0,20,250,180]]
    carte = [["NeutronB6",130,200,2,6,24,158,102],["Tigra3",110,180,0,9,19,119,54],["NeuronA9X",85,220,0,8,21,176,93]]
    memoire = [["Acces16Go",20,80,1,0,19,25,10],["Freedom",50,95,3,2,25,55,30],["StarMemory",40,120,0,3,22,40,20]]
    connexion = [["Wifi+BT",17,45,1,0,19,12,5],["Wifi+BT+3G",28,57,0,3,22,19,8],["Wifi+BT+4G",31,68,3,4,25,34,18],["Wifi+BT+3G+Lifi",46,90,8,7,35,60,41]]
    batterie = [["li-po",210,1200,2,3,25,80,50],["li-ion",250,1500,0,5,21,55,30]]
    camera = [["ColorMedia",60,70,2,4,23,20,8],["Oeil2lynx",45,95,1,0,21,15,6]]
    webcam = [["Spycam",28,58,2,1,16,12,4],["Facemathon",34,63,1,1,14,16,7]]
    gps = [["GPSGalactic",75,200,0,3,15,16,10],["GPSUniverse",50,220,3,7,21,25,14],["GPSWorld",45,175,1,0,11,11,6]]
    boitier = ["Boitier",105,0,0,0,18,158,36]
    
    #ex ecran[numéro de composant][caractéristique] : ecran[1][0] = "MagicScreen"
    
    cptEcran = 0
    cptCarte = 0
    cptMem = 0
    cptConn = 0
    cptBatt = 0
    cptCam = 0
    cptWebcam = 0
    cptGps = 0
    solutions = []
    
    while (cptEcran < 3):
        cptCarte = 0
        while (cptCarte < 3):
            cptMem = 0
            while (cptMem < 3):
                cptConn = 0
                while (cptConn < 4):
                    cptBatt = 0
                    while (cptBatt < 2):
                        cptCam = 0
                        while (cptCam < 2):
                            cptWebcam = 0
                            while (cptWebcam < 2):
                                cptGps = 0
                                while (cptGps < 3):
                                    #ne pas oublier boitier unique
                                    #ici qu'on réalise le calcul au final :)
                                    nom = ecran[cptEcran][0] + "_" + carte[cptCarte][0] + "_" + memoire[cptMem][0] + "_" + connexion[cptConn][0] + "_" + batterie[cptBatt][0] + "_" + camera[cptCam][0] + "_" + webcam[cptWebcam][0] + "_" + gps[cptGps][0] + "_" + boitier[0]
                                    poids = ecran[cptEcran][1] + carte[cptCarte][1] + memoire[cptMem][1] + connexion[cptConn][1] + batterie[cptBatt][1] + camera[cptCam][1] + webcam[cptWebcam][1] + gps[cptGps][1] + boitier[1]
                                    deltaP = batterie[cptBatt][2] - (ecran[cptEcran][2] + carte[cptCarte][2] + memoire[cptMem][2] + connexion[cptConn][2] + camera[cptCam][2] + webcam[cptWebcam][2] + gps[cptGps][2] + boitier[2])
                                    duréeP = ecran[cptEcran][3] + carte[cptCarte][3] + memoire[cptMem][3] + connexion[cptConn][3] + batterie[cptBatt][3] + camera[cptCam][3] + webcam[cptWebcam][3] + gps[cptGps][3] + boitier[3]
                                    duréeF = ecran[cptEcran][4] + carte[cptCarte][4] + memoire[cptMem][4] + connexion[cptConn][4] + batterie[cptBatt][4] + camera[cptCam][4] + webcam[cptWebcam][4] + gps[cptGps][4] + boitier[4]
                                    qual = ecran[cptEcran][5] + carte[cptCarte][5] + memoire[cptMem][5] + connexion[cptConn][5] + batterie[cptBatt][5] + camera[cptCam][5] + webcam[cptWebcam][5] + gps[cptGps][5] + boitier[5]
                                    prixP = ecran[cptEcran][6] + carte[cptCarte][6] + memoire[cptMem][6] + connexion[cptConn][6] + batterie[cptBatt][6] + camera[cptCam][6] + webcam[cptWebcam][6] + gps[cptGps][6] + boitier[6]
                                    prixF = ecran[cptEcran][7] + carte[cptCarte][7] + memoire[cptMem][7] + connexion[cptConn][7] + batterie[cptBatt][7] + camera[cptCam][7] + webcam[cptWebcam][7] + gps[cptGps][7] + boitier[7]
                                    solutions[len(solutions):len(solutions)] = [[nom,poids,deltaP,duréeP,duréeF,qual,prixP,prixF]]
                                    cptGps+=1
                                cptWebcam+=1
                            cptCam+=1
                        cptBatt+=1
                    cptConn+=1
                cptMem+=1
            cptCarte+=1
        cptEcran+=1
    
    print (str(len(solutions)) + " combinaisons réalisées.")
    return solutions
    
def tri(liste,ctPoids,ctPuissance,ctQualité):
    retenus = []
    i = 0
    while (i < len(liste)):
        if (liste[i][1] <= ctPoids and liste[i][2] >= ctPuissance and liste[i][5] >= ctQualité):
            retenus[len(retenus):len(retenus)] = [liste[i]]
        i+=1    
    print (str(len(retenus)) + " combinaisons retenues.")
    return retenus
    
    
listePossibles = combinaisons()
listeRetenues = tri(listePossibles,825,0,200)
i = 0

fichier = open("résultats.csv","w")
while (i<len(listeRetenues)):
    fichier.write(str(listeRetenues[i])+"\n")
    i+=1
fichier.close()
