# Créez une classe Personne avec les attributs nom et prenom.
# Ajoutez une méthode SePresenter qui retourne le nom et le prénom de la personne.
# Ajoutez aussi un constructeur prenant en paramètres de quoi donner des valeurs initiales aux attributs
# nom et prenom. Instanciez plusieurs personnes avec les valeurs de construction de
# votre choix et faites appel à la méthode SePresenter afin de vérifier que tout fonctionne
# correctement.

class Personne:
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("je suis ", self.prenom, self.nom)


Jean = Personne("Jean", "Dujardin")
Edouard = Personne("Edouard", "Dupont")
Kacem = Personne("Kacem", "Alwalid")

Jean.SePresenter()
Edouard.SePresenter()
Kacem.SePresenter()