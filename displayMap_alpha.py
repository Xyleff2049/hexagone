# { Import } #
from pygame.locals import *
from loading import *
import pygame

# { Class } #

# ╔════════════════════════════════════════════════════════════════╗ #
# ║ La class aTile correspond aux objets qui compose la map du jeu,║ #
# ║ Chaque polygone est un objet definis par cette classe          ║ #
# ╚════════════════════════════════════════════════════════════════╝ #

class Tile:

	tileWidth = 0    # Largeur sprite
	tileHeight = 0   # Hauteur sprite
	length = 0       # Nb element de la class
	list = []       # list des objets créés
	listCoords = [] # list des coords des objets créés
	listExternal = []

	def __init__(self, sprite, xTile, yTile, external=False, selected=0):

		if external == False:

			self.x = xTile
			self.y = yTile
			self.sprite = sprite
			self.external = external
			self.selected=selected

			Tile.length += 1

			Tile.list.append(self)
			Tile.listCoords.append((self.x, self.y))

		else:
			self.sprite = sprite
			(self.x, self.y) = (xTile, yTile)
			Tile.listExternal.append(self)

# { Fonctions }

def generateMap(window, listSprite, typeSprite="losange"):

	wipMap = loadingBar(0, 2, prefix="Map generation", endMessage="Completed")

	wipMap.displayBar(0)
	maxX = window.get_width()
	maxY = window.get_height()
	
	spriteWidth = listSprite[0].get_width()
	spriteHeight = listSprite[0].get_height()
	Tile.list = []
	Tile.listCoords = []
	wipMap.displayBar(1)

	if typeSprite == "losange":
		evenLine = True
		(x,y) = (-spriteWidth//2,-spriteHeight//2)

	for y in range(y, maxY, spriteHeight//2):

		if evenLine == False:
			for x in range(x, maxX, spriteWidth):
				if 0 <= x <= 360 and 0 <= y <= 360: Tile(listSprite[0], x, y)
				else: Tile(listSprite[2], x, y, external=True)
			x = -spriteWidth//2
			evenLine = True

		else:
			for x in range(x, maxX, spriteWidth):
				if 0 <= x <= 360 and 0 <= y <= 360: Tile(listSprite[0], x, y)
				else: Tile(listSprite[2], x, y, external=True)
			x = 0
			evenLine = False

	wipMap.displayBar(2)

def displayMap(window):

	(x,y) = (0,0)
	for i in range(len(Tile.list)):
		(x,y) = Tile.listCoords[i]
		window.blit(Tile.list[i].sprite, (x,y))

	for elem in Tile.listExternal:
		window.blit(elem.sprite, (elem.x,elem.y))

def displaySelector(window, pos):

	(x,y) = pos
	window.blit(listLosange[3], pos)

# { Exemple } #
def displaySelector2(window, pos):

	(x,y)=pos
	window.blit(select2,pos)

def selectionTile(pos):
        (x,y)=pos
        co=0
        co=int(co)
        i=0
        for co in Tile.listCoords:
                if (x,y) == co:
                        Tile.list[i].selected=1
                        print(Tile.list[i].selected)
                i+=1


pygame.init()
pygame.display.init()
pygame.key.set_repeat(150,150)

Window = pygame.display.set_mode((400,480))
pygame.display.set_caption('} Display Map Alpha {')

# sprite = pygame.image.load('losange.png')
tilesetLosange = pygame.image.load('TilesetLosange.png')
listLosange = [tilesetLosange.subsurface(0,0, 50,50), tilesetLosange.subsurface(50,0, 50,50), tilesetLosange.subsurface(100,0, 50,50), tilesetLosange.subsurface(150,0, 50,50)]

spellbar= pygame.image.load("bar.png")
select2= pygame.image.load("selec2.png").convert_alpha()

generateMap(Window, listLosange)
displayMap(Window)

(selectX,selectY) = (0,0)
(selectX2,selectY2) = (100,400)

user = 1
while user == 1:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			quit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE: quit()
			if event.key == K_RETURN: user = 0
			if event.key == K_F1:
				pygame.display.set_mode((400,480), FULLSCREEN)
				generateMap(Window, listLosange)
			if event.key == K_F2:
				pygame.display.set_mode((400,400))
				generateMap(Window, listLosange)
			if event.key == K_F5:
				pygame.image.save(Window, 'screen.png')
				print('[== Screenshot "screen.png" ==]')

			if event.key == K_KP4 and selectX > 25: selectX -= 50
			if event.key == K_KP6 and selectX < 325: selectX += 50
			if event.key == K_KP8 and selectY > 25: selectY -= 50
			if event.key == K_KP5 and selectY < 325: selectY += 50

			if event.key == K_KP7 and selectX > 0 and selectY > 0:
				selectX -= 25
				selectY -= 25
			if event.key == K_KP9 and selectX < 350 and selectY > 0:
				selectX += 25
				selectY -= 25
			if event.key == K_KP1 and selectX > 0 and selectY < 350:
				selectX -= 25
				selectY += 25
			if event.key == K_KP3 and selectY < 350 and selectX < 350:
				selectX += 25
				selectY += 25

			if event.key == K_q: (selectX2,selectY2) = (100,400)
			if event.key == K_w: (selectX2,selectY2) = (150,400)
			if event.key == K_e: (selectX2,selectY2) = (200,400)
			if event.key == K_r: (selectX2,selectY2) = (250,400)

			if event.key == K_KP0:
				selectionTile((selectX,selectY))
			
		# if event.type == MOUSEMOTION:

		# 	(xM, yM) = pygame.mouse.get_pos()
	Window.fill((81,91,90))
	displayMap(Window)
	displaySelector(Window, (selectX,selectY))
	displaySelector2(Window, (selectX2,selectY2))
	Window.blit(spellbar,(100,400))
	Window.blit(select2,(selectX2,selectY2))
	pygame.display.flip()