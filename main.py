from random import randint,choice
class Personnage:
    def __init__(self,nom,vie,xp,niveau):
        self.nom=nom
        self.vie=vie
        self.maxVie=vie
        self.xp=xp
        self.niveau=niveau
    def ajouterVie(self,vie):
        #ajoute de la vie dans self.vie sans dépasser self.maxVie
        if self.vie+vie >= self.maxVie:
            self.vie = self.maxVie
        else:
            self.vie += vie
    def retirerVie(self,vie):
        #retire de la vie dans self.vie sans être inférieur à 0
        if self.vie-vie <= 0:
            self.vie = 0
        else:
            self.vie -= vie
    def monterExperience(self,xp):
        #ajoute 2 points d’expérience
        #Augmente d’un niveau tous les 10 xp
        #Exemple 30xp = niveau 3
        self.xp += xp
        self.niveau = xp//10
    def estVivant(self):
        #retourne vrai si le personnage est vivant
        return self.vie>0
    def estMort(self):
        #retourne vrai si le personnage est mort
        return self.vie<=0

class Guerrier(Personnage):
    def __init__(self,nom,force,vie,xp,niveau):
        super().__init__(nom,vie,xp,niveau)
        self.force=force
    def augmenterForce(self):
        self.force += 1
    def combat(self,adversaire):
        #inflige des dégats au mechant si celui-ci est vivant
        #incrémente le nombre de points d’expérience correspondant aux dégâts infligés
        #Monte si nécessaire en niveau en fonction du nombre de points xp
        #retire de la vie au méchant
        #si le méchant est mort augmenter la force de 1 du guerrier
        attaque=randint(1, 4)
        degats=attaque*self.niveau*self.force-adversaire.niveau
        if adversaire.estVivant():
            adversaire.retirerVie(degats)
        self.monterExperience(degats)
        if adversaire.estMort():
            self.augmenterForce()
        print("degat sur le mechant",degats)

p = Guerrier("ehoh",1,100,3,0)
adv = Personnage("Gentil",2,20,3)
p.monterExperience(1)
p.ajouterVie(1)
print(p.vie,p.xp,p.estVivant(),p.estMort())
for i in range(10):
    p.combat(adv)
print(p.vie,p.xp,p.niveau,p.estVivant(),p.estMort())
"""
p.retirerVie(151)
p.monterExperience()
p.monterExperience()
p.monterExperience()
p.monterExperience()
"""
