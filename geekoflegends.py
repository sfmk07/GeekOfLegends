import random

class Boss:
    def __init__(self, nom):
        self.nom = nom
        self.sante_max = random.randint(100, 200)
        self.sante = self.sante_max
        self.attaque = random.randint(10, 20)

    def attaquer_joueur(self):
        return self.attaque

    def subir_degats(self, degats):
        self.sante -= degats

    def est_en_vie(self):
        return self.sante > 0

class Hero:
    def __init__(self, nom, points_de_vie, points_d_attaque):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.points_d_attaque = points_d_attaque

    def defendre(self):
        self.points_d_attaque /= 2

    def subir_degats(self, degats):
        self.points_de_vie -= degats

    def est_en_vie(self):
        return self.points_de_vie > 0

cimetiere_heroes = []

def obtenir_details_heroes():
    nom_guerrier = input("Entrez le nom du Guerrier : ")
    nom_mage = input("Entrez le nom du Mage : ")
    nom_archer = input("Entrez le nom de l'Archer : ")

    total_points_vie = int(input("Entrez le total de points de vie à distribuer entre les héros : "))
    total_points_attaque = int(input("Entrez le total de points d'attaque à distribuer entre les héros : "))

    return nom_guerrier, nom_mage, nom_archer, total_points_vie, total_points_attaque

def poser_enigme():
    enigmes = [
        {"question": "Je suis plus grand que l'Empire State Building, mais je pèse moins que les plumes. Qui suis-je?", "reponse": "ombre"},
        {"question": "Je parle toutes les langues, mais je reste toujours silencieux. Qui suis-je?", "reponse": "echo"},
        {"question": "Je cours tout autour du pré sans jamais bouger. Qui suis-je?", "reponse": "cloture"}
    ]

    for enigme in enigmes:
        while True:
            reponse_joueur = input(enigme["question"] + "\nVotre réponse : ")
            if reponse_joueur.lower() != enigme["reponse"]:
                print("Réponse incorrecte. Veuillez réessayer.")
            else:
                print("Bonne réponse !")
                break

    print("Fin des énigmes.")

nom_heroes = obtenir_details_heroes()

points_vie_restants = nom_heroes[3]
points_attaque_restants = nom_heroes[4]

guerrier = Hero(nom_heroes[0], random.randint(10, points_vie_restants // 3), random.randint(5, points_attaque_restants))
points_vie_restants -= guerrier.points_de_vie
points_attaque_restants -= guerrier.points_d_attaque

mage = Hero(nom_heroes[1], random.randint(10, points_vie_restants // 2), random.randint(5, points_attaque_restants))
points_vie_restants -= mage.points_de_vie
points_attaque_restants -= mage.points_d_attaque

archer = Hero(nom_heroes[2], points_vie_restants, points_attaque_restants)

def gestion_combat_et_cimetiere():
    sauron = Boss("Sauron")
    chronos = Boss("Chronos")
    lilith = Boss("Lilith")

    bosses = [sauron, chronos, lilith]
    heroes = [guerrier, mage, archer]

    for boss in bosses:
        print(f"{boss.nom} a {boss.sante} points de vie et {boss.attaque} points d'attaque.")

        while boss.est_en_vie() and any(hero.est_en_vie() for hero in heroes):
            for hero in heroes:
                if hero.est_en_vie():
                    degats_hero = random.randint(5, 15)
                    boss.subir_degats(degats_hero)
                    print(f"{hero.nom} a infligé {degats_hero * 1.4} points de dégâts à {boss.nom}.")
                    if not boss.est_en_vie():
                        print(f"Bravo! Vous avez vaincu {boss.nom}!")
                        break
                    attaque_boss = boss.attaquer_joueur()
                    hero.subir_degats(attaque_boss / 2)
                    if not hero.est_en_vie():
                        print(f"{hero.nom} a été vaincu!")
                        cimetiere_heroes.append(hero.nom)

            if not boss.est_en_vie():
                continue
            else:
                break

    poser_enigme()

gestion_combat_et_cimetiere()

print(f"{guerrier.nom} a {guerrier.points_de_vie} points de vie et {guerrier.points_d_attaque} points d'attaque.")
print(f"{mage.nom} a {mage.points_de_vie} points de vie et {mage.points_d_attaque} points d'attaque.")
print(f"{archer.nom} a {archer.points_de_vie} points de vie et {archer.points_d_attaque} points d'attaque.")

print("Héros au cimetière :")
for hero in cimetiere_heroes:
    print(f"{hero} est au cimetière.")
