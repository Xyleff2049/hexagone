# { Objects } #

class Tile:

	length = 0         # Number of objects
	tiles = []         # List of all objects
	tilesCoords = []   # List of coords of objects
	external = []      # List of external Tile

	def __init__(self, listSprite, posTile, external=False, selected=False, team="Neutral", occup=False):

		if external == False:
			self.pos = (self.x, self.y) = posTile

			if team == "Neutral": self.sprite = listSprite[0]
			elif team == "Zeta": self.sprite = listSprite[1]
			elif team == "Meya": self.sprite = listSprite[2]
			self.listSprite = listSprite

			self.width = self.sprite.get_width()
			self.height = self.sprite.get_height()

			self.selected = selected # Status of the Tile, selected or not
			self.team = team         # To which team belongs the Tile
			self.occup = occup       # Status of the Tile, occuped or not

			Tile.length += 1

			Tile.tiles.append(self)
			Tile.tilesCoords.append((self.x,self.y))

		else:
			self.sprite = listSprite[3] # External sprite
			self.pos = (self.x, self.y) = posTile
			Tile.external.append(self)

	def changeTeam(self, team):

		self.team = team
		if team == "Neutral":
			self.sprite = self.listSprite[0]
			self.occup = False
		elif team == "Zeta":
			self.sprite = self.listSprite[1]
			self.occup = True
		elif team == "Meya":
			self.sprite = self.listSprite[2]
			self.occup = True

class Unit:

	length = 0
	units = [] # List of all objects

	def __init__(self, listSprite, aTile, team="", life=20):

		if team == "Zeta": self.sprite = listSprite[0]
		elif team == "Meya": self.sprite = listSprite[1]

		(xTile, yTile) = aTile.pos
		self.x = xTile + (aTile.width // 2 - self.sprite.get_width() // 2)
		self.y = yTile + (aTile.height // 2 - self.sprite.get_height() // 2)
		self.pos = (self.x, self.y)

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

	def __init__(self, Surface, spriteInv, spriteSelect, step=50, listStuff=[]):

		Inv.spriteInv = spriteInv
		Inv.spriteSelect = spriteSelect
		Inv.posInv = Inv.posSelect = (Surface.get_width() // 2 - spriteInv.get_width() // 2, Surface.get_height() - 50)
		Inv.step = step

		Inv.stuff = listStuff

	def moveSelector(self, case):

		(xInv, yInv) = Inv.posInv
		Inv.posSelect = (xInv + (self.step * case), yInv)