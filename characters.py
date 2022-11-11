"""
class Personnage:
    def __init__(self,nom,hp,atk):
        self.nom,self.hp,self.atk = nom,hp,atk

    def estVivant(self):
        if self.hp>0:
            return True
        else:
            return False

    def __repr__(self):
        return self.nom+" a "+str(self.hp)+" points de vie et a "+str(self.atk)+" points d'attaque"

    def attaquer(self,p):
        p.hp -= self.atk
        if p.hp <0:
            p.hp = 0

    def info(self):
        return self.__class__.__name__

class Magicien(Personnage):
    def __init__(self,nom,hp,atk):
        super().__init__(nom,hp,atk)

    def attaquer(self,p):
        if p.info() == "Guerrier":
            coeff = 2
            print(p.info())
        elif p.info() == "Magicien" or p.info() == "Druide":
            coeff = 0.5
        else:
            coeff = 1
        p.hp -= self.atk*coeff
        if p.hp <0:
            p.hp = 0

class Guerrier(Personnage):
    def __init__(self,nom,hp,atk):
        super().__init__(nom,hp,atk)

    def attaquer(self,p):
        if p.info() == "Druide":
            coeff = 2
        elif p.info() == "Magicien" or p.info() == "Guerrier":
            coeff = 0.5
        else:
            coeff = 1
        p.hp -= self.atk*coeff
        if p.hp <0:
            p.hp = 0
class Druide(Personnage):
    def __init__(self,nom,hp,atk):
        super().__init__(nom,hp,atk)

    def attaquer(self,p):
        if p.info() == "Magicien":
            coeff = 2
        elif p.info() == "Guerrier" or p.info() == "Druide":
            coeff = 0.5
        else:
            coeff = 1
        p.hp -= self.atk*coeff
        if p.hp <0:
            p.hp = 0
#personnage simple
p1=Personnage('Frodon',40,12)
print(p1)
p2=Personnage('Faramir',30,10)
print(p2)
p1.attaquer(p2)
print(p2)
print("p2 est-t-il vivant?",p2.estVivant())
print(p2)
print("classe :",p2.info())
print("---------------------------------")
#personnage spécifique
p3=Magicien('Gandalf',39,16)
p4=Druide('Panoramix',44,14)
p5=Guerrier('Leonidas',45,15)
print("Avant attaque ->",p3)
print("Avant attaque ->",p4)
print("Avant attaque ->",p5)
p3.attaquer(p4)
print("Après attaque ->",p4)
p3.attaquer(p5)
print("Après attaque ->",p5)
print("--------------------")
#combat final
def combat(pers1,pers2):
    print("Avant attaque ->",pers1)
    print("Avant attaque ->",pers2)
    while pers1.estVivant() and pers2.estVivant():
        pers1.attaquer(pers2)
        pers2.attaquer(pers1)
    if pers1.estVivant():
        print(pers1.nom,"a gagné")
    else:
        print(pers2.nom,"a gagné")
    print("Après attaque ->",pers1)
    print("Après attaque ->",pers2)

combat(p1,p2)"""