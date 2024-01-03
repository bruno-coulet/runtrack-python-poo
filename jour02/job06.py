# Créer une classe Commande avec les attributs privés, numéro de commande, liste de plats commandés et statut de la commande (en cours, terminée ou annulée).
class Commande:
    def __init__(self, numéro):
        self.__number = numéro
        self.__dishes = {}
        self.__status = "en cours"
  

# Ajouter un plat à la commande
    def add_dish(self, dish, prix):
        if self.__status == "en cours":
            self.__dishes[dish] = {"prix": prix, "status": "en cours"}
            print("le plat ajouré est : ",dish)

# Annuler une commande
    def cancel(self):
        self.__status = "annulée"
        print("La commande est annulée")

# _________________________________________________________________
    def afficher_commande(self):
        print le prix et les plats commandé
        print("Le numéro de la commande est", self.__number)
# __________________________________________________________________
        


# calculer le total d’une commande qui doit être en privé
    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__dishes.values()if plat["status"]=='en cours')
        return total

# et afficher une commande avec son total à payer.
    def __get_addition(self):
        self.__set_addition()
        return self.__number, self.__total

# ainsi qu’une méthode permettant de calculer la TVA.
    def set_TVA(self):
        self.__calculer_total()
        self.__TVA = self.__total * 0.2
        return self.__TVA

# Utiliser l’encapsulation et l’abstraction pour créer cette classe de manière que les attributs ne puissent pas être modifiés de l’extérieur.
# La liste des plats commandés doit être représentée sous forme de dictionnaire avec les noms des plats, le prix, le statut de la commande.
salade = "Salade"
steack = "Steack"
tarte = "Tarte"



table_12 = Commande(1)
table_12.add_dish(salade,10)

table_12.cancel()
table_12.afficher_commande()

# print(table_12.__calculer_total())