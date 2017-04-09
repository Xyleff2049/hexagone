from pygame.locals import *
import pygame

class Player(pygame.sprite.Sprite):

	def __init__(self, listSprites):

		pygame.sprite.Sprite.__init__(self)

		self.sprites = listSprites
		self.image = listSprites[0][0]
		self.rect = self.image.get_rect()

		self.step = 0

	def move(self, direction):

		(x,y) = (self.rect.x, self.rect.y)
		(neX, neY)  =(x+direction[0], y+direction[1])

		if 0 <= neX < (300 - self.rect.width) and 0 <= neY < (300 - self.rect.height):
			self.rect.move_ip(direction[0],direction[1])

		if   direction[0] < 0: self.image = self.sprites[1][self.step]
		elif direction[0] > 0: self.image = self.sprites[2][self.step]
		elif direction[1] < 0: self.image = self.sprites[3][self.step]		
		elif direction[1] > 0: self.image = self.sprites[0][self.step]

	def showInfos(self):

		print(self.rect)

pygame.init()
pygame.display.init()

Window = pygame.display.set_mode((300,300))
pygame.display.set_caption('} Test {')
Window.fill((81,91,90))

clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT, 120)

tilesetChara = pygame.image.load('tilesetChara.png')
listImgZeta = [[tilesetChara.subsurface(x,y,64,64) for x in range(0,192,64)] for y in range(0,256,64)]
Zeta = Player(listImgZeta, clock)

playGroup = pygame.sprite.GroupSingle()
playGroup.add(Zeta)

direction = [0,0]

user = True
while user == True:

	clock.tick(120)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			quit()
		elif event.type == KEYUP and event.key == K_ESCAPE:
			pygame.quit()
			quit()
		elif event.type == KEYUP and event.key == K_RETURN: Zeta.showInfos()

		elif event.type == USEREVENT:
			if Zeta.step < 2: Zeta.step += 1
			else: Zeta.step = 0

	keystate = pygame.key.get_pressed()

	direction = [0,0]
	direction[0] = keystate[K_RIGHT] - keystate[K_LEFT]
	direction[1] = keystate[K_DOWN] - keystate[K_UP]
	if direction != [0,0]: Zeta.move(direction)

	Window.fill((81,91,90))

	playGroup.draw(Window)
	pygame.display.flip()