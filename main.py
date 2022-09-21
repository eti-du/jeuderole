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
    def monterExperience(self):
        #ajoute 2 points d’expérience
        #Augmente d’un niveau tous les 10 xp
        #Exemple 30xp = niveau 3
        self.xp += 2
        if self.xp%10 == 0 or (self.xp-1)%10 == 0:
            self.niveau += 1
    def estVivant(self):
        #retourne vrai si le personnage est vivant
        return self.vie>0
    def estMort(self):
        #retourne vrai si le personnage est mort
        return self.vie<=0

