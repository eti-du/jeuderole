#coding:utf-8
"""
Programme d'un jeu de rôle
"""
import pygame
from os.path import join,dirname
from random import randint
from assets.map import ground,layer_1,layer_2
from assets.tilecollisions import collision as tilecollisions

#initialisation
TILE_SIZE = 64   #definition du dessin (carré)
pygame.init()
window = pygame.display.set_mode((0,0),flags=pygame.FULLSCREEN)
pygame.display.set_caption("Role Playing Game | The Mysterious Hill")
font = pygame.font.Font(join(dirname(__file__),'assets/font/CourierNew.ttf'), 40)
fontmn = pygame.font.Font(None, 18)
fontbold = pygame.font.Font(None, 120)
window_x,window_y = pygame.display.Info().current_w,pygame.display.Info().current_h #taille de la fenêtre
window.blit(fontbold.render("CHARGEMENT …", True, (113,52,134)),(window_x//4,window_y//2-50)) #écran de chargement
pygame.display.update()
clock = pygame.time.Clock()

tiles_xmax = min(20,window_x//TILE_SIZE-5) #hauteur du niveau
tiles_ymax = min(14,window_y//TILE_SIZE-3) #longueur du niveau

offset_x = tiles_xmax//2
offset_y = tiles_ymax//2

mainscreenpart_background = pygame.Surface((tiles_xmax*TILE_SIZE,tiles_ymax*TILE_SIZE),flags=pygame.SRCALPHA)
mainscreenpart_foreground = pygame.Surface((tiles_xmax*TILE_SIZE,tiles_ymax*TILE_SIZE),flags=pygame.SRCALPHA)

def find_collisions():
    collisions = []
    for i in range(len(ground)):
        ligne = []
        for j in range(len(ground[0])):
            if tilecollisions[ground[i][j]] <= 0 and tilecollisions[layer_1[i][j]] <= 0 and tilecollisions[layer_2[i][j]] <= 0:
                ligne.append(0)
            else:
                ligne.append(1)
        ligne[-1] = 1
        collisions.append(ligne)
    collisions.append([1]*len(ground[0]))
    return collisions

def load_tiles(TILE_SIZE):
    """
    fonction permettant de charger les images des tuiles dans la liste tiles
    """
    tile_size = 32
    file = join(dirname(__file__),"assets/textures/tilesetV2.png")
    image = pygame.image.load(file).convert_alpha()
    size = image.get_size()
    tiles = []
    for y in range(0, size[1]//tile_size):
        for x in range(0, size[0]//tile_size):
            tiles.append(pygame.transform.scale(image.subsurface(x*tile_size, y*tile_size, tile_size, tile_size),(TILE_SIZE,TILE_SIZE)))
    tiles.append(pygame.Surface((0,0)))
    return tiles

def create_ground(layer):
    surface = pygame.Surface((TILE_SIZE*len(layer[0]),(TILE_SIZE*len(layer))),flags=pygame.SRCALPHA)
    for y in range(len(layer)):
        for x in range(len(layer[0])):
            surface.blit(tiles[layer[y][x]],(x*TILE_SIZE,y*TILE_SIZE))
    return surface

def draw_tiles():
    """
    fonction qui affiche le terrain à partir de la matrice "ground"
    """
    window.fill((0,0,0))
    mainscreenpart_background.fill((0,0,0,0))#µ simp blit directly the scaled layers
    mainscreenpart_foreground.fill((0,0,0,0))
    mainscreenpart_background.blit(ground_srf,(-player.offset_x*TILE_SIZE,-player.offset_y*TILE_SIZE))
    mainscreenpart_foreground.blit(layer_1_srf,(-player.offset_x*TILE_SIZE,-player.offset_y*TILE_SIZE))
    mainscreenpart_foreground.blit(layer_2_srf,(-player.offset_x*TILE_SIZE,-player.offset_y*TILE_SIZE))
    window.blit(mainscreenpart_background,(0,0))
    for i in range(1,len(characters)):
        if player.offset_x+tiles_xmax >= characters[i].x >= player.offset_x and player.offset_y+tiles_ymax >=characters[i].y >= player.offset_y:
            window.blit(characters[i].image,((-player.offset_x+characters[i].x)*TILE_SIZE,(-player.offset_y+characters[i].y)*TILE_SIZE))
    window.blit(player.image,((tiles_xmax//2)*TILE_SIZE,(tiles_ymax//2)*TILE_SIZE))
    window.blit(mainscreenpart_foreground,(0,0))

    pygame.draw.rect(window,(231,231,231),(tiles_xmax*64,0,15,window_y))
    pygame.draw.rect(window,(231,231,231),(0,tiles_ymax*64,window_x,15))
    pygame.draw.rect(window,(0,0,0),(tiles_xmax*64+7,0,3,window_y+8))
    pygame.draw.rect(window,(0,0,0),(0,tiles_ymax*64+7,window_x,3))
    draw_panel()#µ

def draw_panel():#µ
    window.blit(font.render("Vie : "+str(player.vie), True, (230, 230, 230)),(20,tiles_ymax*TILE_SIZE+20))
    window.blit(font.render("Force : "+str(player.force), True, (230, 230, 230)),(20,tiles_ymax*TILE_SIZE+60))
    window.blit(font.render("Expérience : "+str(player.xp), True, (230, 230, 230)),(20,tiles_ymax*TILE_SIZE+100))
    window.blit(font.render("Niveau : "+str(player.niveau), True, (230, 230, 230)),(20,tiles_ymax*TILE_SIZE+140))
    window.blit(font.render("Nom : "+str(player.nom), True, (230, 230, 230)),(20,tiles_ymax*TILE_SIZE+180))

def draw_left_panel(text):#µ cont
    """
    affichage du panneau de gauche
    """
    #window.blit(font.render(str(text), True, (20, 235, 134)),(tiles_xmax*TILE_SIZE+20,20))
    window.blit(fontmn.render(str(text), True, (20, 235, 134)),(tiles_xmax*TILE_SIZE+20,20))

class Moveable_element:
    """
    Classe de tous les éléments visuels qui ne sont pas des tuiles
    """
    def __init__(self,name,position,size,img,collisions):
        self.name = name
        self.image = pygame.transform.scale(pygame.image.load(img),(size,size))
        self.image.blit(fontmn.render(self.name[:9], True, (20, 23, 34)),(0,0))
        self.size=size
        self.collisions=collisions
        self.x,self.y=position
        self.rightdirection = True
        self.offset_x,self.offset_y = 0,1

    def collision(self,x,y):
        if (self.collisions[int(self.offset_y+self.y+y)][int(self.offset_x+self.x+x)]==0):
            return False
        return True

    def droite(self):
        if not self.collision(1,0):
                self.offset_x += 1
        if not self.rightdirection:
            self.image = pygame.transform.flip(self.image,True,False)
            self.rightdirection = True

    def gauche(self):
        if not self.collision(-1,0):
            self.offset_x -= 1
        if self.rightdirection:
            self.image = pygame.transform.flip(self.image,True,False)
            self.rightdirection = False

    def haut(self):
        if not self.collision(0,-1):
            self.offset_y -= 1

    def bas(self):
        if not self.collision(0,1):
                self.offset_y += 1

class Personnage(Moveable_element):
    """
    Classe de tous les personnages
    """
    def __init__(self,nom,vie,xp,niveau,position,size,img,collisions):#µ simpl size,collisions
        if position == False:#µ simpl
            position = (tiles_xmax//2,tiles_ymax//2)#µ simpl
        Moveable_element.__init__(self,nom,position,size,img,collisions)
        self.nom=nom
        self.vie=vie
        self.maxVie=vie
        self.xp=xp
        self.niveau=niveau
    def ajouterVie(self,vie):#ajoute de la vie à "vie" sans dépasser maxVie
        if self.vie+vie >= self.maxVie:
            self.vie = self.maxVie
        else:
            self.vie += vie
    def retirerVie(self,vie):#retire de la vie mais en restant supérieur à 0
        if self.vie-vie <= 0:
            self.vie = 0
        else:
            self.vie -= vie
    def monterExperience(self,xp):#ajoute 2 points d’expérience, Augmente d’un niveau tous les 10 xp
        self.xp += xp
        self.niveau = self.xp//10+1#µimpr
    def estVivant(self):
        return self.vie>0
    #def __repr__(self):
    #    return "("+str(self.niveau)+") "+self.nom+" à "+str(self.vie)+" points de vie, soit est à "+str(100*self.vie//self.maxVie)+"% vivant et à "+str(self.xp)+" points d'expériences"

class Guerrier(Personnage):
    def __init__(self,nom,vie,xp,niveau,force,position,size,img,collisions):
        super().__init__(nom,vie,xp,niveau,position,size,img,collisions)
        self.force=force
    def augmenterForce(self):
        self.force += 1
    def combat(self,adversaire):
        """
        méthode de l'attaque du guerrier sur un autre personnage :
        inflige des dégats à l'adversaire
        incrémente le nombre de points d’expérience correspondant aux dégâts infligés, 
        monte si nécessaire en niveau en fonction du nombre de points xp et retire de la vie à l'adversaire
        """
        degats=randint(1, 4)*self.niveau*self.force
        if adversaire.estVivant():
            adversaire.retirerVie(degats)
        self.monterExperience(degats)
        if not adversaire.estVivant():
            self.augmenterForce()
        draw_left_panel(str(degats)+" dégats infligés à "+adversaire.nom)

class Magicien(Personnage):
    def __init__(self,nom,vie,xp,niveau,mana,position,size,img,collisions):
        super().__init__(nom,vie,xp,niveau,position,size,img,collisions)
        self.maxMana=mana
        self.mana=mana
    def augmenterMana(self):#augmente maxMana de 10 
        self.maxMana += 10
    def ajouterMana(self):#ajoute 1 de mana sans dépasser maxMana
        if self.mana + 1 <= self.maxMana:
            self.mana += 1#µ impr
    def retirerMana(self,mana):#retire du mana retourne vrai si le magicien à assez de mana
        if self.mana -1 >= 0:#µ impr
            self.mana -= 1
            return True
        else:
            return False
    def combat(self,adversaire):
        """
        méthode de l'attaque du magicien sur un autre personnage :
        inflige des dégats à l'adversaire s'il est vivant et si le magicien dispose assez de mana, 
        incrémente le nombre de points d’expérience correspondant aux dégâts infligés, 
        retire de la vie à l'advervaire et diminue le mana
        """
        degats=randint(1,4)*self.niveau*2
        draw_left_panel(str(degats) + " dégats infligés du magicien sur "+adversaire.nom)
        if adversaire.estVivant() and self.mana>0:#µ simp
            adversaire.vie -= degats
            self.monterExperience(degats)
            self.retirerMana(1)
        if not adversaire.estVivant():#µimpr
            self.augmenterMana()

def duel(combattant,adversaire):
    #combat entre deux personnages
    i = 0
    while adversaire.estVivant() and combattant.estVivant() or i>200:
        combattant.combat(adversaire)
        pygame.display.update()#µ impr
        pygame.time.wait(1000)#µ impr
        pygame.draw.rect(window,(90,0,0),(tiles_xmax*TILE_SIZE+15,20,800,50))#µ impr
        adversaire.combat(combattant)
        pygame.display.update()#µ impr
        pygame.time.wait(1000)#µ impr
        pygame.draw.rect(window,(110,0,0),(tiles_xmax*TILE_SIZE+15,20,800,50))#µ impr
        i += 1
    if combattant.estVivant():
        draw_left_panel(combattant.nom +" a gagné")
        pygame.display.update()#µ impr
        pygame.time.wait(2000)#µ impr
        return True
    draw_left_panel(adversaire.nom+" a gagné")#µ impr
    pygame.display.update()#µ impr
    pygame.time.wait(2000)#µ impr
    return False
    
collisions = find_collisions()#trouve les collisions du niveau
tiles = load_tiles(TILE_SIZE) #Charge les images dans la liste des images des tuiles
ground_srf=create_ground(ground)
layer_1_srf=create_ground(layer_1)
layer_2_srf=create_ground(layer_2)

#création des personnages
player = Guerrier("Ash",100,1,1,1,False,TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso2 = Guerrier("Gandalf",50,1,1,1,[8,3],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso3 = Personnage("Gandalf_lefrerejumau",10,100,1,[3,5],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso4 = Magicien("Gentil",100,1,1,10,[8,8],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso5 = Personnage("EhOh",100,1,10,[9,8],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso6 = Personnage("Le Chat",100,1,10,[10,8],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso6 = Personnage("Max",100,1,10,[11,8],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)

characters = [player,perso2,perso3,perso4,perso5,perso6]
ennemis = [perso2,perso4,perso6]

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Ferme la fenetre (croix rouge)
            loop = False
    keys = pygame.key.get_pressed()# Détecte les touches pressées
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
    for i in range(len(ennemis)):
        if player.offset_x+tiles_xmax//2 == ennemis[i].x and player.offset_y+tiles_ymax//2 == ennemis[i].y:
            if duel(player,ennemis[i]):
                ennemis[i].x,ennemis[i].y = 1,1
                ennemis.pop(i)
                break
            else:
                player.ajouterVie(100)
                player.offset_x = 0
                player.offset_y = 0           
    draw_tiles() #affiche le niveau
    draw_left_panel("Score")#affiche les informations de gauche
    pygame.display.update() #mets à jour la fenetre graphique
    clock.tick(10)
pygame.quit()

