from pygame.locals import *
import pygame

# { Class } #
class Button:

	buttons = []

	def __init__(self, Surface, listSprite, pos, command, status=0):

		"""
		Parameters:
		-------------------------
		listSprite .. -Required : A list of sprite which contains:
			- [0] : Normal sprite
			- [1] : Pressed sprite
			- [2] : Disabled sprite
		pos ......... -Required : Coords in px of the button
		status ...... -Optional : Actual status of the button
		"""

		self.status = status
		self.listSprite = listSprite
		if status != "Hide": self.sprite = listSprite[0]

		(maxX, maxY) = (Surface.get_width(), Surface.get_height())

		if (0,0) <= pos < (maxX, maxY): self.pos = (self.x, self.y) = pos
		else:
			print('Coords are invalid, sprite pos has been changed to (0,0)')
			self.pos = (self.x, self.y) = (0,0)

		self.rect = Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())
		Button.buttons.append(self)

		self.surface = Surface
		if isinstance(command, str): self.command = command
		else:
			print('Invalide command, must be a executable string')
			self.command = 'print("Invalide command")'

	def execute(self):

		exec(self.command)

	def changeStatus(self, newStatus):

		self.status = newStatus
		self.sprite = self.listSprite[newStatus]

	def displayButton():

		for obj in Button.buttons:
			if obj.status != "Hide": obj.surface.blit(obj.sprite, obj.pos)

def click(event):

	for obj in Button.buttons:
		if obj.rect.collidepoint(event.pos) and event.type == MOUSEBUTTONDOWN:
			obj.changeStatus(1)
			obj.execute()
		elif event.type == MOUSEBUTTONUP: obj.changeStatus(0)

if __name__ == '__main__':

	# { Examples } #
	pygame.init()
	pygame.display.init()

	Window = pygame.display.set_mode((200,200))

	tileset = pygame.image.load('tilesetButton.png')
	listSprite = [tileset.subsurface(0,0, 100,50), tileset.subsurface(100,0, 100,50)]

	x = (Window.get_width() // 2) - (listSprite[0].get_width() // 2)
	y = (Window.get_height() // 2) - (listSprite[0].get_height() // 2)
	myButton = Button(Window, listSprite, (x,y), 'quit()')

	user = True
	while user == True:

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				quit()

			if event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP: click(event)

		Button.displayButton()
		pygame.display.flip()
