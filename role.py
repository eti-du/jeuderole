"""
Programme réalisé par moi
"""
import pygame
from os.path import join,dirname

#variables du niveau
NB_TILES = 666   #nombre de tiles a chager (ici de 00.png à 26.png) 27 au total !!
TITLE_SIZE=64   #definition du dessin (carré)
largeur=8       #hauteur du niveau
hauteur=8       #largeur du niveau
tiles=[]       #liste d'images tiles
clock = pygame.time.Clock()


#definition du niveau

niveau=[[ 23, 24, 24, 24, 24, 24, 24, 25],
        [189,189,171, 47, 47, 47, 47, 48],
        [ 46, 47,187, 47, 47, 47, 47, 48],
        [ 46,118,217,120, 47, 47, 47, 48],
        [ 46,141,142,143, 47, 47, 47, 48],
        [ 46,164,165,166, 47, 47, 47, 48],
        [506,507,507,507,507,507,507,508],
        [529,486,486,486,486,486,486,531]]

decor=[[  0,  0,253,  0,  0,  0,  0,  0],
       [  0,  0,  0,  0,  0,  0,  0,  0],
       [184,  0,  0,138,  0,278,279,  0],
       [  0,  0,  0,  0,  0,276,277,  0],
       [  0,  0,  0,  0,  0,299,300,  0],
       [186,  0,  0,  0,  0,  0,  0,  0],
       [  0,  0,  0,  0,  0,  0,  0,  0],
       [  0,  0,  0,  0,  0,  0,  0,  0]]


collisions=[[  1,  1,  1,  1,  1,  1,  1,  1],
            [  1,  0,  0,  0,  0,  0,  0,  1],
            [  1,  0,  0,  0,  0,  1,  1,  1],
            [  1,  0,  0,  0,  0,  1,  1,  1],
            [  1,  0,  0,  0,  0,  1,  1,  1],
            [  1,  0,  0,  0,  0,  0,  0,  1],
            [  1,  0,  0,  0,  0,  0,  0,  1],
            [  1,  1,  1,  1,  1,  1,  1,  1]]



class Personnage(pygame.sprite.Sprite):

    def __init__(self,position,size,img,collisions):
        super().__init__()


        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.size=size
        self.collisions=collisions
        self.x,self.y=position
        self.rect.x=self.x*size
        self.rect.y=self.y*size

    def testCollisionsDecor(self,x,y):
        if (self.collisions[self.y+y][self.x+x]==0):
            self.x+=x
            self.y+=y

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




#la taille de la fenetre dépend de la largeur et de la hauteur du niveau
#on rajoute une rangée de 32 pixels en bas de la fentre pour afficher le score d'ou (hauteur +1)
pygame.init()
fenetre = pygame.display.set_mode((largeur*TITLE_SIZE, (hauteur+1)*TITLE_SIZE))
pygame.display.set_caption("Dungeon | RPG")
font = pygame.font.Font('freesansbold.ttf', 20)



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
            fenetre.blit(tiles[niveau[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))
            if (decor[y][x]>0):
                fenetre.blit(tiles[decor[y][x]],(x*TITLE_SIZE,y*TITLE_SIZE))



def afficheScore(score):
    """
    affiche le score
    """
    #exemple bidon
    #scoreAafficher = font.render(str(score), True, (0, 255, 0))
    #fenetre.blit(scoreAafficher,(120,250))
    pass



fenetre.fill((0,0,0))   #efface la fenetre
chargetiles(tiles)  #chargement des images


perso = Personnage([1,1],TITLE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso2 = Personnage([3,3],TITLE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)
perso3 = Personnage([3,5],TITLE_SIZE,join(dirname(__file__),"data/perso.png"),collisions)

aventuriers = pygame.sprite.Group()
aventuriers.add(perso)
aventuriers.add(perso3)

mechants = pygame.sprite.Group()
mechants.add(perso2)



loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
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
                loop = False
    col = pygame.sprite.collide_rect(perso, perso2)
    if col==1:
        print("collision",col)
        mechants.remove(perso2)


    fenetre.fill((0,0,0))
    afficheNiveau(niveau)   #affiche le niveau
    aventuriers.update()
    aventuriers.draw(fenetre)
    mechants.update()
    mechants.draw(fenetre)
    pygame.display.update() #mets à jour la fentre graphique
    #pygame.display.flip()
    #clock.tick(60)
pygame.quit()

