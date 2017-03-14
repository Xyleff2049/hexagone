# { Objects } #

class Tile:

	tileWidth = 0      # Tile width
	tileHeight = 0     # Tile height
	length = 0         # Number of objects
	tiles = []         # List of all objects
	tilesCoords = []   # List of coords of objects
	external = []      # List of external Tile

	def __init__(self, listSprite, posTile, external=False, selected=False, team="Neutral", occup=False):

		if external == False:
			(self.x, self.y) = posTile # Position (in px) of the Tile
			self.pos = posTile

			if team == "Neutral": self.sprite = listSprite[0]
			elif team == "Zeta": self.sprite = listSprite[1]
			elif team == "Meya": self.sprite = listSprite[2]

			self.selected = selected # Status of the Tile, selected or not
			self.team = team         # To which team belongs the Tile
			self.occup = occup       # Status of the Tile, occuped or not

			Tile.length += 1

			Tile.tiles.append(self)
			Tile.tilesCoords.append((self.x,self.y))

		else:
			self.sprite = listSprite[3] # External sprite
			(self.x, self.y) = posTile  # Position (in px) of the Tile
			self.pos = posTile
			Tile.external.append(self)

class Unit:

	length = 0
	units = [] # List of all objects

	def __init__(self, listSprite, Tile, posTile, team="", life=20):

		if team == "Zeta": self.sprite = listSprite[0]
		elif team == "Meya": self.sprite = listSprite[1]

		(xTile, yTile) = posTile
		self.x = (xTile // 2) + (self.sprite.get_width() // 2)
		self.y = (yTile // 2) + (self.sprite.get_height() // 2)

		self.team = team
		self.life = life

		Unit.length += 1
		Unit.units.append(self)

class Selector:

	pos = (0,0)
	sprite = None

	def __init__(self, sprite, posSelect):

		Selector.pos = posSelect
		Selector.sprite = sprite

class Inv:

	spriteInv = None
	spriteSelect = None
	posInv = (0,0)
	posSelect = (0,0)
	step = 0
	stuff = []

	def __init__(self, spriteInv, spriteSelect, posInv, step=50, listStuff=[]):

		Inv.spriteInv = spriteInv
		Inv.spriteSelect = spriteSelect
		Inv.posInv = Inv.posSelect = posInv
		Inv.step = step

		Inv.stuff = listStuff

	def moveSelector(case):

		Inv.posSelect[0] = Inv.posInv[0] + (step * case)
		Inv.posSelect[1] = Inv.posInv[1] + (step * case)