from random import randint,choice
class Personnage:
    def __init__(self,nom,vie,xp,niveau):
        self.nom=nom
        self.vie=vie
        self.maxVie=vie
        self.xp=xp
        self.niveau=niveau
    def ajouterVie(self,vie): #ajoute de la vie dans self.vie sans dépasser self.maxVie
        if self.vie+vie >= self.maxVie:
            self.vie = self.maxVie
        else:
            self.vie += vie
    def retirerVie(self,vie): #retire de la vie dans self.vie sans être inférieur à 0
        if self.vie-vie <= 0:
            self.vie = 0
        else:
            self.vie -= vie
    def monterExperience(self,xp): #ajoute des points d’expérience
        #Augmente d’un niveau tous les 10 xp
        #Exemple 30xp = niveau 3
        self.xp += xp
        self.niveau = self.xp//10+1# ???
    def estVivant(self): #retourne vrai si le personnage est vivant
        return self.vie>0
    def estMort(self): #retourne vrai si le personnage est mort
        return self.vie<=0
    def __repr__(self):
        return "("+str(self.niveau)+") "+self.nom+" à "+str(self.vie)+" points de vie, soit est à "+str(100*self.vie//self.maxVie)+"% vivant et à "+str(self.xp)+" points d'expériences"

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
        print("degat sur "+adversaire.nom,degats)
class Magicien(Personnage):
    def __init__(self,nom,mana,vie,xp,niveau):
        super().__init__(nom,vie,xp,niveau)
        self.maxMana=mana
        self.mana=mana
    def augmenterMana(self):#augmente de 10 self.maxMana
        self.maxMana += 10
    def ajouterMana(self):#ajoute 1 en self.mana sans dépasser self.maxMana
        if self.mana + 1 <= self.maxMana:
            self.mana += 1
    def retirerMana(self,mana):
        #retire mana à self.mana sans descendre en dessous de 0
        #retourne vrai si le magicien à lancé un sort
        #retourne faux si le magicien nen peut plus lancer de sort.
        if self.mana -1 >= 0:
            self.mana -= 1
            return True
        else:
            return False
    def combat(self,adversaire):
        attaque=randint(1, 4)
        degats=attaque*self.niveau*2-adversaire.niveau
        print("degat du magicien sur "+adversaire.nom,degats)
        #inflige des dégats au mechant si celui-ci est vivant
        # et que le magicien dispose de nana
        #incrémente le nombre de points d’expérience correspondant aux dégâts infligés
        #Monte si nécessaire en niveau en fonction du nombre de points xp
        #retire de la vie au méchant et diminue de 1 self.mana (consommation de magie)
        #si le méchant est mort augmenter self.maxMana de 10 du magicien.
        if adversaire.estVivant() and self.mana>0:
            adversaire.retirerVie(degats)
            self.monterExperience(degats)
            self.mana -= 1
        if adversaire.estMort():
            self.augmenterMana()

"""
p = Guerrier("ehoh",1,100,13,1)
maj = Magicien("gandalfe",10,100,10,1)
adv = Personnage("Gentil",2,20,3)
adv2 = Personnage("Gentil",2,20,3)
p.monterExperience(10)
p.ajouterVie(1)
while adv.estVivant():
    p.combat(adv)
print(adv.estMort(),adv.vie)
print(p.vie,p.xp,p.niveau,p.estVivant(),p.estMort())

p.retirerVie(151)
p.monterExperience(1)
p.monterExperience(1)
p.monterExperience(1)
p.monterExperience(1)
while adv2.estVivant():
    maj.combat(adv2)
print(maj.vie,maj.xp,maj.niveau,maj.estVivant(),maj.estMort())
"""
combattant=Guerrier("Linflas",2,20,0,1)
mechant=Guerrier("Chaos",2,30,0,2)
magot=Magicien("Chani",30,30,0,2)
def duel(combattant,mechant):
    while mechant.estVivant() and combattant.estVivant():
        combattant.combat(mechant)
        mechant.combat(combattant)
    if mechant.estMort():
        return "Vous avez perdu le combat"
    elif combattant.estMort():
        return "Vous avez gagné le combat"
    else:
        return "erreur"
duel(magot,mechant)
print(combattant)
print(magot)
print(mechant)






















