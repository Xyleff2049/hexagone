# { Imports } #
from loading import loadingBar
from Objects import *

# { Functions } #

def generateMap(Surface, listSprite):

	"""
	Parameters :
	---------------------------------------------------------------\n
	Surface ..... -Required : A pygame.Surface object
	listSprite .. -Required : A list of sprite which contains:
		- [0] : Neutral sprite
		- [1] : Zeta sprite
		- [2] : Meya sprite
		- [3] : External sprite

	"""

	wipMap = loadingBar(0, 2, prefix="Map generation", endMessage="Completed")

	wipMap.displayBar(0)
	maxX = Surface.get_width()
	maxY = Surface.get_height()
	
	spriteWidth = listSprite[0].get_width()
	spriteHeight = listSprite[0].get_height()
	Tile.tiles = []
	Tile.tilesCoords = []
	wipMap.displayBar(1)

	evenLine = True
	(x,y) = (-spriteWidth//2,-spriteHeight//2)

	for y in range(y, maxY, spriteHeight//2):

		if evenLine == False:
			for x in range(x, maxX, spriteWidth):
				if 0 <= x <= (maxX - 40) and 0 <= y <= (maxY - 90): Tile(listSprite, (x,y), team="Neutral")
				else: Tile(listSprite, (x,y), external=True)
			x = -spriteWidth//2
			evenLine = True

		else:
			for x in range(x, maxX, spriteWidth):
				if 0 <= x <= (maxX - 40) and 0 <= y <= (maxY - 90): Tile(listSprite, (x,y), team="Neutral")
				else: Tile(listSprite, (x,y), external=True)
			x = 0
			evenLine = False

	wipMap.displayBar(2)

def createArmy(window, listSprite, Tile, team, life=20):

	if Tile.occup == False: 

		Unit(listSprite, Tile, team=team, life=life)
		Tile.changeTeam(team)

def clearArmy(window, fill):

	Unit.units = []
	Unit.length = 0

	for obj in Tile.tiles: obj.changeTeam("Neutral")

	if isinstance(fill, tuple): window.fill(fill)
	else: window.blit(fill, (0,0))

def displayMap(window, tileset=True, units=True, select=True, inv=True):

	if tileset == True:

		for tile in Tile.tiles: window.blit(tile.sprite, tile.pos)

		for tile in Tile.external: window.blit(tile.sprite, tile.pos)

	if units == True:

		for entity in Unit.units: window.blit(entity.sprite, entity.pos)

	if select == True: window.blit(Selector.sprite, Selector.pos)

	if inv == True:
		window.blit(Inv.spriteInv, Inv.posInv)
		window.blit(Inv.spriteSelect, Inv.posSelect)