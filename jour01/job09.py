class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC (self):
        prixTTC = self.prixHT * (self.TVA+100) /100
        return round(prixTTC, 2)
    
    def afficher (self):
        return f"Le prix HT est de : {self.prixHT} £\nLa TVA est de : {self.TVA} %\nLe prix TTC est de : {self.CalculerPrixTTC()} £"
    
# Ajouter des méthodes permettant de modifier le nom du produit et son prix.

    def nouveau_nom(self, nom):
        self.nom = nom

    def nouveau_prix(self, prix):
        self.prix = prix
 
# Ainsi que des méthodes permettant de retourner chaque information du produit.
    def nom_produit(self):
        return f"le nom du produit est : {self.nom}"
        
    def prixHT_produit(self):
        return f"le prix HT du produit est :{self.prixHT}"

    def TVA_produit(self):
        return self.prixHT * self.TVA /100 
    
    def prixTTC_produit(self):
        return f"le prix TTC du produit est : {self.CalculerPrixTTC()}"
    


# Créer plusieurs produits et calculer leurs TVA.      
ustensile = Produit("casserole", 50, 20)
feculent = Produit("patate", 5, 5)
vehicule = Produit("grosse_voiture", 50000, 20)


# Modifier le nom et le prix de chaque produit 
ustensile.nouveau_nom("cocotte")
ustensile.nouveau_prix(100)

feculent.nouveau_nom("riz")
feculent.nouveau_prix(4)

vehicule.nouveau_nom("citadine")
vehicule.nouveau_prix(20000)


# et afficher en console le nouveau prix des produits.
print(ustensile.prixTTC_produit())
print(feculent.prixTTC_produit())
print(vehicule.prixTTC_produit())
