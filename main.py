"""
Programme d'un jeu de role réalisé par moi
"""
import pygame
from os.path import join,dirname
from random import randint,choice

#variables
NB_TILES = 666   #nombre de tuiles a charger (ici de 00.png à 666.png) 667 au total !
TILE_SIZE = 64   #definition du dessin (carré)
tiles=[]         #liste des images des tuiles
clock = pygame.time.Clock()
#La taille de la fenetre ne dépend pas de la longueur et de la hauteur du niveau
#On rajoute une rangée de quelques pixels en bas de la fentre pour afficher le score
pygame.init()
window = pygame.display.set_mode((0,0),flags=pygame.FULLSCREEN) #window = pygame.display.set_mode((tiles_xmax*TILE_SIZE, (tiles_ymax+1)*TILE_SIZE))
pygame.display.set_caption("Role Playing Game | The Mysterious Hill")
font = pygame.font.Font(join(dirname(__file__),'assets\\font\\CourierNew.ttf'), 40)
fontmn = pygame.font.Font(None, 18)
fontG = pygame.font.Font(None, 120)
window_x,window_y = pygame.display.Info().current_w,pygame.display.Info().current_h
window.blit(fontG.render("CHARGEMENT …", True, (113,52,134)),(window_x//4,window_y//2-50))
pygame.display.update()

tiles_xmax = min(20,window_x//TILE_SIZE-5) #hauteur du niveau
tiles_ymax = min(14,window_y//TILE_SIZE-3) #longueur du niveau

offset_x = tiles_xmax//2
offset_y = tiles_ymax//2

from assets.map import niveau,collisions,decor

class Moveable_element(pygame.sprite.Sprite):
    def __init__(self,name,position,size,img,collisions):
        super().__init__()
        self.name = name
        self.image = pygame.transform.scale(pygame.image.load(img),(64,64))
        self.image.blit(fontmn.render(self.name[:9], True, (20, 23, 34)),(0,0))
        self.rect = self.image.get_rect()
        self.size=size
        self.collisions=collisions
        self.x,self.y=position
        self.rect.x=self.x*size
        self.rect.y=self.y*size
        self.rightdirection = True
        self.offset_x,self.offset_y = 0,0

    def collision(self,x,y):
        if (self.collisions[int(self.offset_y+self.y+y)][int(self.offset_x+self.x+x)]==0):
            return False
        return True

    def droite(self):
        if not self.collision(1,0):
            if self.offset_x > len(niveau[0]) - tiles_xmax:
                self.x+=0.2
                self.rect.x=self.x*self.size
            else:
                self.offset_x += 1

        if not self.rightdirection:
            self.image = pygame.transform.flip(self.image,True,False)
            self.rightdirection = True

    def gauche(self):
        if not self.collision(-1,0):
            if self.x*2 > tiles_xmax:
                self.x-=0.2
                self.rect.x=self.x*self.size
            else:
                self.offset_x -= 1
        if self.rightdirection:
            self.image = pygame.transform.flip(self.image,True,False)
            self.rightdirection = False

    def haut(self):
        if not self.collision(0,-1):
            if self.y*2 > tiles_ymax:
                self.y-=0.2
                self.rect.y=self.y*self.size
            else:
                self.offset_y -= 1

    def bas(self):
        if not self.collision(0,1):
            if self.offset_y > len(niveau) - tiles_ymax:
                self.y+=0.2
                self.rect.y=self.y*self.size
            else:
                self.offset_y += 1

    
"""
    def droite(self):
        self.testCollisionsDecor(1,0)
        self.rect.x=self.x*self.size
        if not self.rightdirection:
            self.image = pygame.transform.flip(self.image,True,False)
            self.rightdirection = True

    def gauche(self):
        self.testCollisionsDecor(-1,0)
        self.rect.x=self.x*self.size
        if self.rightdirection:
            self.image = pygame.transform.flip(self.image,True,False)
            self.rightdirection = False

    def haut(self):
        self.testCollisionsDecor(0,-1)
        self.rect.y=self.y*self.size

    def bas(self):
        self.testCollisionsDecor(0,1)
        self.rect.y=self.y*self.size
    
    """

def load_tiles():
    """
    fonction permettant de charger les images de tuiles dans la matrice tiles
    """
    global TILE_SIZE
    tile_size = 32
    file = join(dirname(__file__),"data/base.png")
    image = pygame.image.load(file).convert_alpha()
    size = image.get_size()
    tiles = []
    for y in range(0, size[1]//tile_size):
        ligne = []
        for x in range(0, size[0]//tile_size):
            ligne.append(pygame.transform.scale(image.subsurface(x*tile_size, y*tile_size, tile_size, tile_size),(TILE_SIZE,TILE_SIZE)))
        tiles.append(ligne)
    return tiles

def draw_tiles(niveau):
    """
    affiche le terrain à partir de la matrice "niveau"

    a = player.offset_y (début de la boucle pour)
    si la longueur du niveau est inférieur à a plus la longueur maximale de tuiles placable
    (si le joueur arrive à la fin du monde)
    alors a = longueur du niveau moins longueur maximale de tuiles
    si a >= 0
    alors a = player.offset_y
    si a < 0 (si le joueur est au début du monde)
    alors a = 0
    b = a + tiles_ymax (fin de la boucle pour)
    """
    window.fill((0,0,0))
    for_1 = max(min(player.offset_y,len(niveau) - tiles_ymax),-3)
    for_2 = max(min(player.offset_x,len(niveau[0]) - tiles_xmax),-5)
    for y in range(for_1,for_1+tiles_ymax):
        for x in range(for_2,for_2+tiles_xmax):
            window.blit(tiles[niveau[y][x]//23][niveau[y][x]%23],((x-for_2)*TILE_SIZE,(y-for_1)*TILE_SIZE))
            if (decor[y][x]>0):
                window.blit(tiles[decor[y][x]//23][decor[y][x]%23],((x-for_2)*TILE_SIZE,(y-for_1)*TILE_SIZE))
    pygame.draw.rect(window,(231,231,231),(tiles_xmax*64,0,15,window_y))
    pygame.draw.rect(window,(231,231,231),(0,tiles_ymax*64,window_x,15))
    pygame.draw.rect(window,(0,0,0),(tiles_xmax*64+7,0,3,window_y+8))
    pygame.draw.rect(window,(0,0,0),(0,tiles_ymax*64+7,window_x,3))

def afficheScore(score):
    """
    affiche le score
    """
    scoreAafficher = font.render(str(score), True, (20, 235, 134))
    window.blit(scoreAafficher,(tiles_xmax*TILE_SIZE+20,20))
    window.blit(font.render(str(player.collision(0,0)), True, (20, 235, 134)),(tiles_xmax*TILE_SIZE+20,60))
#==Personnages==
class Personnage(Moveable_element):
    def __init__(self,nom,vie,xp,niveau,position,size,img,collisions):
        if position == False:
            position = (tiles_xmax//2,tiles_ymax//2)
            Moveable_element.__init__(self,nom,position,size,img,collisions)
        else:
            Moveable_element.__init__(self,nom,position,size,img,collisions)
        self.nom=nom
        self.vie=vie
        self.maxVie=vie
        self.xp=xp
        self.niveau=niveau
    def ajouterVie(self,vie):#ajoute de la vie à vie sans dépasser maxVie
        if self.vie+vie >= self.maxVie:
            self.vie = self.maxVie
        else:
            self.vie += vie
    def retirerVie(self,vie):#retire de la vie mais reste supérieur à 0
        if self.vie-vie <= 0:
            self.vie = 0
        else:
            self.vie -= vie
    def monterExperience(self,xp):#ajoute 2 points d’expérience, Augmente d’un niveau tous les 10 xp
        self.xp += xp
        self.niveau = self.xp//10+1
    def estVivant(self):
        return self.vie>0
    def estMort(self):
        return self.vie<=0

class Guerrier(Personnage):
    def __init__(self,nom,force,vie,xp,niveau,position,size,img,collisions):
        super().__init__(nom,vie,xp,niveau,position,size,img,collisions)
        self.force=force
    def augmenterForce(self):
        self.force += 1
    def combat(self,adversaire):
        """
        inflige des dégats à l'adversiare, 
        incrémente le nombre de points d’expérience correspondant aux dégâts infligés, 
        Monte si nécessaire en niveau en fonction du nombre de points xp retire de la vie au méchant
        """
        attaque=randint(1, 4)
        degats=attaque*self.niveau*self.force
        if adversaire.estVivant():
            adversaire.retirerVie(degats)
        self.monterExperience(degats)
        if adversaire.estMort():
            self.augmenterForce()
        afficheScore(str(degats)+" dégats infligés à "+adversaire.nom)
class Magicien(Personnage):
    def __init__(self,nom,mana,vie,xp,niveau,position,size,img,collisions):
        super().__init__(nom,vie,xp,niveau,position,size,img,collisions)
        self.maxMana=mana
        self.mana=mana
    def augmenterMana(self):#augmente maxMana de 10 
        self.maxMana += 10
    def ajouterMana(self):#ajoute 1 de mana sans dépasser maxMana
        if self.mana + 1 <= self.maxMana:
            self.mana += 1
    def retirerMana(self,mana):#retire du mana retourne vrai si le magicien à assez de mana
        if self.mana -1 >= 0:
            self.mana -= 1
            return True
        else:
            return False
    def combat(self,adversaire):
        """
        inflige des dégats à l'adversaire s'il est vivant et si le magicien dispose assez de mana, 
        incrémente le nombre de points d’expérience correspondant aux dégâts infligés, 
        retire de la vie au méchant et diminue le mana
        """
        attaque=randint(1,4)
        degats=attaque*self.niveau*2
        afficheScore(str(degats) + " dégats infligés du magicien sur le méchant")
        if adversaire.estVivant() and self.mana>0:
            adversaire.vie -= degats
            self.monterExperience(degats)
            self.mana -= 1
        if adversaire.estMort():
            self.augmenterMana()

def duel(combattant,mechant):
    #combat entre deux personnages
    i = 0
    while mechant.estVivant() and combattant.estVivant() or i>200:
        combattant.combat(mechant)
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.draw.rect(window,(90,0,0),(10,window_y-64,800,50))
        mechant.combat(combattant)
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.draw.rect(window,(110,0,0),(10,window_y-64,800,50))
        i += 1
    if combattant.estVivant():
        afficheScore(combattant.nom +" a gagné")
    else:
        afficheScore(mechant.nom+" a gagné")
    pygame.display.update()
    pygame.time.wait(3000)

#==Fin personnages==
#création des personnages
player = Guerrier("Ash",30,100,1,1,False,TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso2 = Guerrier("Gandalf",10,100,1,1,[3,3],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso3 = Personnage("Gandalf_lefrerejumau",10,100,1,[3,5],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso4 = Personnage("Gentil",10,100,1,[8,8],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso5 = Personnage("EhOh",10,100,1,[8,8],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso6 = Personnage("Le Chat",10,100,1,[8,8],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso6 = Personnage("Max",10,100,1,[8,8],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)

aventuriers = pygame.sprite.Group()
aventuriers.add(player)
aventuriers.add(perso3)

mechants = pygame.sprite.Group()
mechants.add(perso2)

tiles = load_tiles() #Charge les images
loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Ferme la fenetre (croix rouge)
            loop = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_z]:
        player.haut()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.droite()
    if keys[pygame.K_LEFT] or keys[pygame.K_q]:
        player.gauche()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.bas()
    if keys[pygame.K_ESCAPE]:
        loop = False
    if mechants.has(perso2):
        if pygame.sprite.collide_rect(player, perso2):
            print("ATTENTION COLLISION")
            duel(player,perso2)
            mechants.remove(perso2)
            perso2 = 0

    draw_tiles(niveau) #affiche le niveau
    afficheScore("Score")
    aventuriers.update()
    aventuriers.draw(window)
    mechants.update()
    mechants.draw(window)
    pygame.display.update() #mets à jour la fenetre graphique
    clock.tick(30)
pygame.quit()

