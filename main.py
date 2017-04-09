# { Imports } #
from pygame.locals import *
from Functions import *
from Objects import *
from button import *
import pygame

# { Inits } #
pygame.init()
pygame.display.init()
pygame.key.set_repeat(100,100)

Window = pygame.display.set_mode((800,600))
pygame.display.set_caption('} Display Map Beta {')
# background = pygame.image.load('background.png')
Window.fill((81,91,90))

tileset = pygame.image.load('Tileset.png')
tilesTile = [tileset.subsurface(0,0, 50,50), tileset.subsurface(50,0, 50,50), tileset.subsurface(100,0, 50,50), tileset.subsurface(150,0, 50,50)]
tilesetAlien = pygame.image.load('TilesetAliens.png')
tilesAlien = [tilesetAlien.subsurface(0,0, 25,25), tilesetAlien.subsurface(25,0, 25,25)]
invImage = tileset.subsurface(0,50, 200,50)
invSelectImg = tileset.subsurface(0,100, 50,50)
selectImg = tileset.subsurface(50,100, 50,50)

Selector(selectImg, (0,0))
Inv = Inv(Window, invImage, invSelectImg)

tilesetButton = pygame.image.load('tilesetButton.png')
listButton = [tilesetButton.subsurface(0,0, 100,50), tilesetButton.subsurface(100,0, 100,50)]
myButton = Button(Window, listButton, (0,0), 'quit()')

generateMap(Window, tilesTile)
displayMap(Window)

actualTeam = "Zeta"

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

		if event.type == KEYUP:

			if event.key == K_F5: pygame.image.save(Window, 'screen.png')

			if event.key == K_SPACE:
				if actualTeam == "Zeta": actualTeam = "Meya"
				else: actualTeam = "Zeta"

			if event.key == K_q: Inv.moveSelector(0)
			if event.key == K_w: Inv.moveSelector(1)
			if event.key == K_e: Inv.moveSelector(2)
			if event.key == K_r: Inv.moveSelector(3)

			if event.key == K_k: clearArmy(Window, (81,91,90))

		if event.type == MOUSEBUTTONUP:

			i=0
			for coord in Tile.tilesCoords:
				if coord == Selector.pos: createArmy(Window, tilesAlien, Tile.tiles[i], actualTeam)
				i += 1

		if event.type == MOUSEBUTTONUP or event.type == MOUSEBUTTONDOWN: click(event)

	Window.fill((81,91,90))
	# Window.blit(background, (0,0))

	displayMap(Window)
	Button.displayButton()
	pygame.display.flip()