# Créer la classe “Cercle” recevant en argument son rayon initialisé dans le constructeur.

# Ajouter les méthodes suivantes :
# - changerRayon qui permet de modifier le rayon.
# - afficherInfos qui permet d’afficher toutes les informations du cercle.
# - circonférence qui permet de retourner la circonférence.
# - aire qui permet de retourner l’aire du cercle.
# - diametre qui permet de retourner le diamètre du cercle.

import math

class Cercle:
    def __init__(self, rayon=0):
        self.rayon = rayon
    
    def changerRayon(self, rayon):
        self.rayon = rayon

    def circonference(self):
        circonference = 2 * math.pi * self.rayon
        return round(circonference,1)


    def afficherInfos(self):
        print(f"rayon du cercle : {self.rayon}")
        print(f"circonférence du cercle : {self.circonference()}")
        print(f"aire du cercle : {self.aire()}")
        print(f"diamètre du cercle : {self.diametre()}")


    def aire(self):
        aire = math.pi * self.rayon ** 2
        return round(aire,1)
    
    def diametre(self):
        diametre = 2 * self.rayon
        return round(diametre,1)

# Créer deux cercles avec comme rayon 4 et 7. Pour chaque cercle.
# afficher ses informations, afficher sa circonférence, son diamètre et son aire.  
    
cercle_4=Cercle(4)
cercle_7=Cercle(7)

cercle_4.afficherInfos()
cercle_4.circonference()
cercle_4.diametre()
cercle_4.aire()

cercle_7.afficherInfos()
cercle_7.circonference()
cercle_7.diametre()
cercle_7.aire()
