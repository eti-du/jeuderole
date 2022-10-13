"""
Programme réalisé par moi
"""
import pygame
from os.path import join,dirname

#variables du niveau
NB_TILES = 666   #nombre de tuiles a charger (ici de 00.png à 666.png) 667 au total !
TILE_SIZE = 64  #definition du dessin (carré)
largeur = 20     #hauteur du niveau
hauteur = 12     #largeur du niveau
tiles=[]         #liste des images des tuiles
clock = pygame.time.Clock()


#la taille de la fenetre dépend de la largeur et de la hauteur du niveau
#on rajoute une rangée de 32 pixels en bas de la fentre pour afficher le score d'ou (hauteur +1)
pygame.init()
window = pygame.display.set_mode((0,0))
#window = pygame.display.set_mode((largeur*TILE_SIZE, (hauteur+1)*TILE_SIZE))
pygame.display.set_caption("Role Playing Game | The Mysterious Hill")
font = pygame.font.Font('freesansbold.ttf', 20)
fontG = pygame.font.Font('freesansbold.ttf', 120)
window_x,window_y = pygame.display.Info().current_w,pygame.display.Info().current_h
window.blit(fontG.render("CHARGEMENT …", True, (113,52,134)),(window_x//4,window_y//2-50))
pygame.display.update()

#definition du niveau

niveau = [
[ 23, 24, 24, 24, 24, 25, 73, 73, 73, 73, 73, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 48, 73, 73, 73, 73, 73, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 48, 73, 73, 73, 73, 73, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[189,189,189,171, 47, 48, 73, 73, 73, 73, 73, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
[ 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47],
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
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]
"""[[  0,  0,253,  0,  0,  0,  0,  0],
       [  0,  0,  0,  0,  0,  0,  0,  0],
       [184,  0,  0,138,  0,278,279,  0],
       [  0,  0,  0,  0,  0,276,277,  0],
       [  0,  0,  0,  0,  0,299,300,  0],
       [186,  0,  0,  0,  0,  0,  0,  0],
       [  0,  0,  0,  0,  0,  0,  0,  0],
       [  0,  0,  0,  0,  0,  0,  0,  0]]"""


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
"""[[  1,  1,  1,  1,  1,  1,  1,  1],
            [  1,  0,  0,  0,  0,  0,  0,  1],
            [  1,  0,  0,  0,  0,  1,  1,  1],
            [  1,  0,  0,  0,  0,  1,  1,  1],
            [  1,  0,  0,  0,  0,  1,  1,  1],
            [  1,  0,  0,  0,  0,  0,  0,  1],
            [  1,  0,  0,  0,  0,  0,  0,  1],
            [  1,  1,  1,  1,  1,  1,  1,  1]]"""


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
            self.x+=x*0.05
            self.y+=y*0.05

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


def chargetiles(tiles):
    """
    fonction permettant de charger les images tiles dans une liste tiles[]
    """
    for n in range(0,NB_TILES):
        #print('data/'+str(n)+'.png')
        tiles.append(pygame.transform.scale(pygame.image.load(join(dirname(__file__),'data/'+str(n)+'.png')),(64,64))) #attention au chemin

def afficheNiveau(niveau):
    """
    affiche le niveau a partir de la liste a deux dimensions niveau[][]
    """
    for y in range(hauteur):
        for x in range(largeur):
            window.blit(tiles[niveau[y][x]],(x*TILE_SIZE,y*TILE_SIZE))
            if (decor[y][x]>0):
                window.blit(tiles[decor[y][x]],(x*TILE_SIZE,y*TILE_SIZE))

def afficheScore(score):
    """
    affiche le score
    """
    #exemple
    #scoreAafficher = font.render(str(score), True, (0, 255, 0))
    #window.blit(scoreAafficher,(120,250))
    pass


perso = Personnage([1,1],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso2 = Personnage([3,3],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso3 = Personnage([3,5],TILE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)

aventuriers = pygame.sprite.Group()
aventuriers.add(perso)
aventuriers.add(perso3)

mechants = pygame.sprite.Group()
mechants.add(perso2)



chargetiles(tiles)#charge les images
loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
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
        """
        elif event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_UP:    #est-ce la touche UP
                perso.haut()
            elif event.key == pygame.K_DOWN:  #est-ce la touche DOWN
                perso.bas()
            elif event.key == pygame.K_RIGHT:  #est-ce la touche RIGHT
                perso.droite()
            elif event.key == pygame.K_LEFT:  #est-ce la touche LEFT
                perso.gauche()
            elif event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False"""
    if mechants.has(perso2):
        if pygame.sprite.collide_rect(perso, perso2):
            perso.gauche()
            print("collision")
            mechants.remove(perso2)
            perso2 = 0


    window.fill((0,0,0))
    afficheNiveau(niveau)   #affiche le niveau
    aventuriers.update()
    aventuriers.draw(window)
    mechants.update()
    mechants.draw(window)
    pygame.display.update() #mets à jour la fenetre graphique
    #pygame.display.flip()
    clock.tick(30)
pygame.quit()

