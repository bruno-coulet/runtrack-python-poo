# Créer une classe Commande avec les attributs privés, numéro de commande, liste de plats commandés et statut de la commande (en cours, terminée ou annulée).
class Commande:
    def __init__(self, numéro, plats, statut, addition):
        self.__number = numéro
        self.__dishes = plats
        self.__status = statut
        self.__total = 0
        self.__TVA = 0

# Ajouter un plat à la commande
    def add_dish(self, dish, prix):
        self.__dishes[dish] = {"prix": prix, "status": "en cours"}

# Annuler une commande
    def cancel(self):
        self.__dishes = {}
        self.__total = 0
        self.__TVA = 0  

# calculer le total d’une commande qui doit être en privé
    def __set_addition(self):
        self.__total = sum(plat["prix"] for plat in self.__dishes.values())

# et afficher une commande avec son total à payer.
    def __get_addition(self):
        self.__set_addition()
        return self.__number, self.__total

# ainsi qu’une méthode permettant de calculer la TVA.
    def set_TVA(self):
        self.__set_addition()
        self.__TVA = self.__total * 0.2
        return self.__TVA

# Utiliser l’encapsulation et l’abstraction pour créer cette classe de manière que les attributs ne puissent pas être modifiés de l’extérieur.
# La liste des plats commandés doit être représentée sous forme de dictionnaire avec les noms des plats, le prix, le statut de la commande.
salade = "Salade"
steack = "Steack"
tarte = "Tarte"

table_12 = Commande(5, {salade: 10, steack: 15, tarte: 5}, "En cours", "addition")

print(table_12.__get_addition())