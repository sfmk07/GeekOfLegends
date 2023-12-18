import random

class Personnage:
    def __init__(self, nom, pv, attaque):
        self.nom = nom
        self.pv = pv
        self.attaque = attaque
        self.pv_initial = pv  # Ajout de l'attribut pv_initial

    def est_vivant(self):
        return self.pv > 0
