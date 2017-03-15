# { Imports } #

from pygame.locals import *
from Functions import *
from Objects import *
import pygame

# { Inits } #
pygame.init()
pygame.display.init()
pygame.key.set_repeat(150,150)

Window = pygame.display.set_mode((400,450))
pygame.display.set_caption('} Display Map Beta {')

tileset = pygame.image.load('Tileset.png')
tilesTile = [tileset.subsurface(0,0, 50,50), tileset.subsurface(50,0, 50,50), tileset.subsurface(100,0, 50,50), tileset.subsurface(150,0, 50,50)]
tilesetAlien = pygame.image.load('TilesetAliens.png')
tilesAlien = [tilesetAlien.subsurface(0,0, 25,25), tilesetAlien.subsurface(25,0, 25,25)]
invImage = tileset.subsurface(0,50, 200,50)
invSelectImg = tileset.subsurface(0,100, 50,50)
selectImg = tileset.subsurface(50,100, 50,50)

Selector(selectImg, (0,0))
Inv(invImage, invSelectImg, (100,400))

generateMap(Window, tilesTile)
displayMap(Window)

user = True
while user == True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			quit()

		if event.type == MOUSEMOTION:

			(xM, yM) = pygame.mouse.get_pos()

			for (x,y) in Tile.tilesCoords:

				if (x + 10) <= xM <= (x + 40) and (y + 10) <= yM <= (y + 40):
					Selector.pos = (x,y)

		if event.type == MOUSEBUTTONUP:

			i=0
			for coord in Tile.tilesCoords:
				if coord == Selector.pos: createArmy(Window, tilesAlien, Tile.tiles[i], "Meya")
				i += 1

	Window.fill((81,91,90))

	displayMap(Window)
	pygame.display.flip()