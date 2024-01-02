# Créer une classe nommée Point avec les attributs x et y correspondant aux
# coordonnées horizontales et verticales du point. Les deux attributs doivent être
# initialisés dans le constructeur.

# La classe Point doit posséder les méthodes suivantes :

# - afficherLesPoints qui affiche les coordonnées des points.
# - afficherX et afficherY qui affiche respectivement x et y.
# - changerX et changerY qui change la valeur des attributs x et y.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("Coordonnées du point :",self.x,", ",self.y)

    def afficheX(self):
        print ("x = ",self.x)

    def afficheY(self):
        print ("y = ",self.y)

    def changerX(self):
        self.x= input("Donnez une valeur pour x : ")

    def changerY(self):
        self.y= input("Donnez une valeur pour y : ")

point = Point(2, 3)

point.afficherLesPoints()
point.afficheX()
point.afficheY()

point.changerX()
point.changerY()

point.afficherLesPoints()
