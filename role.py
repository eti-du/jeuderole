"""
Programme d'un jeu de role réalisé par moi
"""
import pygame
from os.path import join,dirname

#variables
NB_TILES = 666   #nombre de tuiles a charger (ici de 00.png à 666.png) 667 au total !
TILE_SIZE = 64   #definition du dessin (carré)
largeur = 20     #hauteur du niveau
hauteur = 12     #largeur du niveau
tiles=[]         #liste des images des tuiles
clock = pygame.time.Clock()
#La taille de la fenetre ne dépend pas de la largeur et de la hauteur du niveau
#On rajoute une rangée de quelques pixels en bas de la fentre pour afficher le score
pygame.init()
window = pygame.display.set_mode((0,0)) #window = pygame.display.set_mode((largeur*TILE_SIZE, (hauteur+1)*TILE_SIZE))
pygame.display.set_caption("Role Playing Game | The Mysterious Hill")
font = pygame.font.Font('freesansbold.ttf', 20)
fontG = pygame.font.Font('freesansbold.ttf', 120)
window_x,window_y = pygame.display.Info().current_w,pygame.display.Info().current_h
window.blit(fontG.render("CHARGEMENT …", True, (113,52,134)),(window_x//4,window_y//2-50))
pygame.display.update()

#definition du terrain
niveau = [
[ 23, 24, 24, 24, 24, 25, 73, 73, 73, 73, 73, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 48, 73, 73, 73, 73, 73, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 48, 73, 73, 73, 73, 73, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[189,189,189,171, 47, 48, 73, 73, 73, 73, 73, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47,187, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47,187, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47,187, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47,187, 47, 47,118,119,119,119, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47,193,189,189,146,168,168,168, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47,164,165,165,165, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46,  0,  1,  2,  3,  4, 82, 82, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47]]
"""[[ 23, 24, 24, 24, 24, 24, 24, 25],
        [189,189,171, 47, 47, 47, 47, 48],
        [ 46, 47,187, 47, 47, 47, 47, 48],
        [ 46,118,217,120, 47, 47, 47, 48],
        [ 46,141,142,143, 47, 47, 47, 48],
        [ 46,164,165,166, 47, 47, 47, 48],
        [506,507,507,507,507,507,507,508],
        [529,486,486,486,486,486,486,531]]"""

decor = [
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,297,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,297,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,297,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]

collisions = [
[  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
[  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1]]

class Personnage(pygame.sprite.Sprite):
    def __init__(self,position,size,img,collisions):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img),(64,64))
        self.rect = self.image.get_rect()
        self.size=size
        self.collisions=collisions
        self.x,self.y=position
        self.rect.x=self.x*size
        self.rect.y=self.y*size

    def testCollisionsDecor(self,x,y):
        if (self.collisions[int(self.y+y)+1][int(self.x+x)+1]==0):
            self.x+=x*0.1
            self.y+=y*0.1

    def droite(self):
        self.testCollisionsDecor(1,0)
        self.rect.x=self.x*self.size

    def gauche(self):
        self.testCollisionsDecor(-1,0)
        self.rect.x=self.x*self.size

    def haut(self):
        self.testCollisionsDecor(0,-1)
        self.rect.y=self.y*self.size

    def bas(self):
        self.testCollisionsDecor(0,1)
        self.rect.y=self.y*self.size

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

def afficheNiveau(niveau):
    """
    affiche le terrain à partir de la matrice "niveau"
    """
    for y in range(hauteur):
        for x in range(largeur):
            window.blit(tiles[niveau[y][x]//23][niveau[y][x]%23],(x*TILE_SIZE,y*TILE_SIZE))
            if (decor[y][x]>0):
                window.blit(tiles[decor[y][x]//23][decor[y][x]%23],(x*TILE_SIZE,y*TILE_SIZE))

def afficheScore(score):
    """
    affiche le score
    """
    #exemple
    #scoreAafficher = font.render(str(score), True, (0, 255, 0))
    #window.blit(scoreAafficher,(120,250))
    pass

#création des personnages
perso = Personnage([1,1],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso2 = Personnage([3,3],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso3 = Personnage([3,5],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)

aventuriers = pygame.sprite.Group()
aventuriers.add(perso)
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
        perso.haut()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        perso.droite()
    if keys[pygame.K_LEFT] or keys[pygame.K_q]:
        perso.gauche()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        perso.bas()
    if keys[pygame.K_ESCAPE]:
        loop = False
    if mechants.has(perso2):
        if pygame.sprite.collide_rect(perso, perso2):
            perso.gauche()
            print("collision")
            mechants.remove(perso2)
            perso2 = 0

    window.fill((0,0,0))
    afficheNiveau(niveau) #affiche le niveau
    aventuriers.update()
    aventuriers.draw(window)
    mechants.update()
    mechants.draw(window)
    pygame.display.update() #mets à jour la fenetre graphique
    #pygame.display.flip()
    clock.tick(30)
pygame.quit()

