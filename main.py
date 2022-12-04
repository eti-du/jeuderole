#coding:utf-8
"""
Programme d'un jeu de rôle
"""
#importation des bibliothèques
import pygame
from os.path import join,dirname
from random import randint
from assets.map import ground,layer_1,layer_2
from assets.tilecollisions import collision as tilecollisions

#initialisation
TILE_SIZE = 64   #taille d'une tuile
COLOR_1 = (0,0,0)
COLOR_2 = (231,231,231)
COLOR_3 = (20, 135, 234)

pygame.init()
window = pygame.display.set_mode((0,0),flags=pygame.FULLSCREEN)
pygame.display.set_caption("Role Playing Game | The Mysterious Hill")
window_x,window_y = pygame.display.Info().current_w,pygame.display.Info().current_h #taille de la fenêtre
window.blit(pygame.font.Font(None, 120).render("CHARGEMENT …", True, (113,52,134)),(window_x//4,window_y//2-50)) #écran de chargement
pygame.display.update()

font    = pygame.font.Font(join(dirname(__file__),'assets/font/CourierNew.ttf'), 30)
font_lf = pygame.font.Font(join(dirname(__file__),'assets/font/futura_heavy.ttf'), 20)
fontmn  = pygame.font.Font(None, 18)

clock = pygame.time.Clock()

tiles_xmax = window_x//TILE_SIZE-5 #hauteur du niveau
tiles_ymax = window_y//TILE_SIZE-3 #longueur du niveau
offset_x = tiles_xmax//2
offset_y = tiles_ymax//2

mainscreenpart_background = pygame.Surface((tiles_xmax*TILE_SIZE,tiles_ymax*TILE_SIZE),flags=pygame.SRCALPHA)
mainscreenpart_foreground = pygame.Surface((tiles_xmax*TILE_SIZE,tiles_ymax*TILE_SIZE),flags=pygame.SRCALPHA)

messages = ["_________________________"] #texte à afficher à droite de l'écran
messages_max = 15 #nombre maximum de messages

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

def load_tiles(filename,tile_size:int):#,transparency:bool):
    """
    fonction permettant de charger les images des tuiles dans la liste tiles
    """
    #filename = join(dirname(__file__),"assets/textures/tilesetV2.png")
    image = pygame.image.load(join(dirname(__file__),filename)).convert_alpha()
    imagesize = image.get_size()
    tiles = []
    for y in range(0, imagesize[1]//tile_size):
        for x in range(0, imagesize[0]//tile_size):
            tiles.append(pygame.transform.scale(image.subsurface(x*tile_size, y*tile_size, tile_size, tile_size),(TILE_SIZE,TILE_SIZE)))
            #if not transparency:
            #    tiles[-1].set_colorkey((109,170,44))
    tiles.append(pygame.Surface((0,0)))
    return tiles

def load_tiles_2(filename):
    """
    fonction permettant de charger les images des tuiles dans la liste tiles
    """
    tile_size = (32,36)
    #filename = join(dirname(__file__),"assets/textures/tilesetV2.png")
    image = pygame.image.load(join(dirname(__file__),filename)).convert_alpha()
    imagesize = image.get_size()
    tiles = []
    for y in range(0, imagesize[1]//tile_size[1]):
        for x in range(0, imagesize[0]//tile_size[0]):
            tiles.append(pygame.transform.scale(image.subsurface(x*tile_size[0], y*tile_size[1], tile_size[0], tile_size[1]),(TILE_SIZE,TILE_SIZE)))
            
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
    window.fill(COLOR_1)
    mainscreenpart_background.fill((0,0,0,0))#µ simp blit directly the scaled layers
    mainscreenpart_foreground.fill((0,0,0,0))
    mainscreenpart_background.blit(ground_srf,(-player.offset_x*TILE_SIZE,-player.offset_y*TILE_SIZE))
    mainscreenpart_foreground.blit(layer_1_srf,(-player.offset_x*TILE_SIZE,-player.offset_y*TILE_SIZE))
    mainscreenpart_foreground.blit(layer_2_srf,(-player.offset_x*TILE_SIZE,-player.offset_y*TILE_SIZE))
    window.blit(mainscreenpart_background,(0,0))
    for i in range(1,len(characters)):
        if player.offset_x+tiles_xmax > characters[i].x >= player.offset_x and player.offset_y+tiles_ymax >characters[i].y >= player.offset_y:
            window.blit(characters[i].image,((-player.offset_x+characters[i].x)*TILE_SIZE,(-player.offset_y+characters[i].y)*TILE_SIZE))
    window.blit(player.image,((tiles_xmax//2)*TILE_SIZE,(tiles_ymax//2)*TILE_SIZE))
    window.blit(mainscreenpart_foreground,(0,0))

    pygame.draw.rect(window,COLOR_2,(tiles_xmax*64,0,15,window_y))
    pygame.draw.rect(window,COLOR_2,(0,tiles_ymax*64,window_x,15))
    pygame.draw.rect(window,COLOR_1,(tiles_xmax*64+7,0,3,window_y+8))
    pygame.draw.rect(window,COLOR_1,(0,tiles_ymax*64+7,window_x,3))
    draw_panel()#µ

def draw_panel():#µ
    window.blit(font.render("Vie : "+str(player.vie), True, COLOR_2),(20,tiles_ymax*TILE_SIZE+20))
    window.blit(font.render("Force : "+str(player.force), True, COLOR_2),(20,tiles_ymax*TILE_SIZE+60))
    window.blit(font.render("Expérience : "+str(player.xp), True, COLOR_2),(20,tiles_ymax*TILE_SIZE+100))
    window.blit(font.render("Niveau : "+str(player.niveau), True, COLOR_2),(20,tiles_ymax*TILE_SIZE+140))
    window.blit(font.render("Nom : "+str(player.nom), True, COLOR_2),(20,tiles_ymax*TILE_SIZE+180))

def draw_right_panel(messages):
    """
    affichage du panneau de droite
    """
    pygame.draw.rect(window, COLOR_1, (tiles_xmax*TILE_SIZE+15, 0, window_x,tiles_ymax*TILE_SIZE)) #efface la zone de droite
    window.blit(font.render("x : "+str(player.offset_x+tiles_xmax//2)+" y : "+str(player.offset_y+tiles_ymax//2), True, COLOR_3),(tiles_xmax*TILE_SIZE+15,10)) #affiche les coordonnées
    for i in range(len(messages)): #affiche tous les messages de la liste, un message par ligne
        window.blit(font_lf.render(messages[(i+1)*-1], True, COLOR_3),(tiles_xmax*TILE_SIZE+20, 70+i*30))
    pygame.display.update(pygame.Rect(tiles_xmax*TILE_SIZE,0,window_x-tiles_xmax*TILE_SIZE,window_y))#actualise l'écran

def newmessage(text):#ajoute un nouveau message
    messages.append(str(text))
    if len(messages) > messages_max:
        messages.pop(0)
    draw_right_panel(messages)

class Moveable_element:
    """
    Classe de tous les éléments visuels qui ne sont pas des tuiles
    """
    def __init__(self,name,position,img,collisions):
        self.name = name
        #self.image = pygame.transform.scale(pygame.image.load(img),(TILE_SIZE,TILE_SIZE))
        self.image = img
        #self.image.blit(fontmn.render(self.name[:9], True, (20, 23, 34)),(0,0))
        self.collisions=collisions
        self.x,self.y=position
        self.rightdirection = True
        self.offset_x,self.offset_y = 11-tiles_xmax//2,13-tiles_ymax//2

    def collision(self,x,y):
        if (self.collisions[int(self.offset_y+tiles_ymax//2+y)][int(self.offset_x+tiles_xmax//2+x)]==0):
            return False
        return True

    def move(self,x:float,y:float):
        if not self.collision(x,y):
            self.offset_x += x
            self.offset_y += y
        if self.rightdirection and x<0:
            self.image = pygame.transform.flip(self.image,True,False)
            self.rightdirection = False
        elif not self.rightdirection and x>0:
            self.image = pygame.transform.flip(self.image,True,False)
            self.rightdirection = True

class Personnage(Moveable_element):
    """
    Classe de tous les personnages
    """
    def __init__(self,nom,vie,xp,niveau,position,size,img,collisions):#µ simpl size,collisions
        Moveable_element.__init__(self,nom,position,img,collisions)
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
        méthode de l'attaque du guerrier sur un autre personnage : inflige des dégats à l'adversaire
        incrémente le nombre de points d’expérience correspondant aux dégâts infligés, monte le niveau en fonction du nombre de points xp et retire de la vie à l'adversaire
        """
        degats=randint(1, 4)*self.niveau*self.force
        if adversaire.estVivant():
            adversaire.retirerVie(degats)
        self.monterExperience(degats)
        if not adversaire.estVivant():
            self.augmenterForce()
        newmessage(str(degats)+" dégats infligés à "+adversaire.nom)

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
        méthode de l'attaque du magicien sur un autre personnage : inflige des dégats à l'adversaire s'il est vivant et si le magicien dispose assez de mana, 
        incrémente le nombre de points d’expérience correspondant aux dégâts infligés, retire de la vie à l'advervaire et diminue le mana
        """
        degats=randint(1,4)*self.niveau*2
        newmessage(str(degats) + " dégats infligés à "+adversaire.nom)
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
        pygame.time.wait(500)
        adversaire.combat(combattant)
        pygame.time.wait(500)
        i += 1
    if combattant.estVivant():
        newmessage(combattant.nom +" a gagné")
        return True
    newmessage(adversaire.nom+" a gagné")
    return False

collisions = find_collisions()#trouve les collisions du niveau
tiles = load_tiles("assets/textures/tilesetV2.png",32) #Charge les images dans la liste des images des tuiles
#characters_images = [load_tiles("assets/textures/characters/Tiny16-3.png",16,False),load_tiles("assets/textures/characters/Tiny16-1.png",16,False),load_tiles("assets/textures/characters/Tiny16-1.png",16,False)]
characters_images = load_tiles_2("assets/textures/characters/ranger_f.png")
ground_srf=create_ground(ground)
layer_1_srf=create_ground(layer_1)
layer_2_srf=create_ground(layer_2)

#création des personnages
player = Guerrier("Ash",100,1,1,1,[0,0],TILE_SIZE,characters_images[3],collisions)
perso2 = Guerrier("Gandalf",25,1,1,1,[27,18],TILE_SIZE,characters_images[3],collisions)
perso3 = Personnage("Gandalf_lefrerejumau",10,100,1,[45,18],TILE_SIZE,characters_images[3],collisions)
perso4 = Magicien("Gentil",150,18,1,10,[32,98],TILE_SIZE,characters_images[3],collisions)
perso5 = Personnage("EhOh",100,1,10,[52,11],TILE_SIZE,characters_images[3],collisions)
perso6 = Personnage("Le Chat",100,1,10,[32,12],TILE_SIZE,characters_images[3],collisions)
perso7 = Personnage("Max",100,1,10,[52,40],TILE_SIZE,characters_images[3],collisions)

characters = [player,perso2,perso3,perso4,perso5,perso6,perso7]
ennemis = [perso2,perso4]

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Ferme la fenetre (croix rouge)
            loop = False
    keys = pygame.key.get_pressed()# Détecte les touches pressées
    if keys[pygame.K_UP] or keys[pygame.K_z]:
        player.move(0,-1)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move(1,0)
    if keys[pygame.K_LEFT] or keys[pygame.K_q]:
        player.move(-1,0)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.move(0,1)
    if keys[pygame.K_ESCAPE]:
        loop = False
    for i in range(len(ennemis)):
        if player.offset_x+tiles_xmax//2 == ennemis[i].x and player.offset_y+tiles_ymax//2 == ennemis[i].y:
            if duel(player,ennemis[i]):
                ennemis[i].x,ennemis[i].y = 1,1
                ennemis.pop(i)
            else:
                player.ajouterVie(100)
                player.offset_x = 0
                player.offset_y = 0
            messages = [messages[-1]]
            break
    draw_tiles() #affiche le niveau
    draw_right_panel(messages)
    pygame.display.update() #mets à jour la fenetre graphique
    clock.tick(10)
pygame.quit()

