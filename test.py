from pygame.locals import *
from Buttons import Button, Menu
import pygame

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Papyrus', 30)
window = pygame.display.set_mode((350, 400))

first = pygame.image.load('mainButtons.png')
second = [first.subsurface(x,y, 200,50) for x in range(0, 200, 200) for y in range(0, 150, 50)]

playButton = Button(window, (75,50), second, text="Jouer", send="start")
menu = Menu(playButton)

user = True
while user:

	if pygame.event.get(QUIT): quit()

	menu.menu_event(None)
	menu.menu_display(window)

	print(menu.result)

	pygame.display.flip()
