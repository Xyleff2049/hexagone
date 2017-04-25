from pygame.locals import *
from pathFinding import *
import pygame
import os

class Player(pygame.sprite.Sprite):

    def __init__(self, listSprites, coords, Stats):

        # -- Check Zone -- #

        try:
            if type(listSprites) != list: raise TypeError
            # Possibiliter d'utiliser des MachinError perso en les nomants en début de code: MachinError = Excepetion
            # Ajouter les test sur l'attribut Stats
        except TypeError:
            print('An error has occured during the initialisation of the Player object\n','TypeError: the argument listSprites must be a <class \'list\'>')
            quit()

        # -- Initialisation Zone -- #

        pygame.sprite.Sprite.__init__(self)
        
        # -> Spritesheet
        self.sprite_sheet = listSprites

        # -> Setup Animation
        self.direction = 'down'
        self.dict_image = {'down':self.sprite_sheet[0], 'left':self.sprite_sheet[1], 'right':self.sprite_sheet[2], 'up':self.sprite_sheet[3]}
        self.setup_delay()
        self.anim_step = 0
        self.state_walking = False

        # -> Display
        self.image = self.dict_image[self.direction][0]
        self.rect = self.image.get_rect()
        (self.rect.x, self.rect.y) = coords


    def setup_delay(self):

        self.STEP_DELAY = USEREVENT + 1
        pygame.time.set_timer(self.STEP_DELAY, 240)

    def walking(self, moveVector, Surface):

        self.image = self.dict_image[self.direction][self.anim_step]

        (targetX, targetY) = (self.rect.x + moveVector[0], self.rect.y + moveVector[1])
        if 0 <= targetX <= (Surface.get_width() - self.rect.width) and 0 <= targetY <= (Surface.get_height() - self.rect.height): self.rect.move_ip(moveVector[0], moveVector[1])

    def update(self, Surface, actualEvent, keyState):

        moveVector = [0,0]

        for event in actualEvent:

            if event.type == KEYDOWN:
                keyName = pygame.key.name(event.key)
                if keyName in ['down', 'left', 'right', 'up']:
                    self.direction = keyName

            if event.type == self.STEP_DELAY:
                if self.anim_step < 2: self.anim_step += 1
                else: self.anim_step = 0

            else:
                moveVector = [keyState[K_RIGHT] - keyState[K_LEFT], keyState[K_DOWN] - keyState[K_UP]]

        moveVector = [keyState[K_RIGHT] - keyState[K_LEFT], keyState[K_DOWN] - keyState[K_UP]]
        if moveVector != [0,0]: self.walking(moveVector, Surface)

first = pygame.image.load('tilesetChara.png')
second = [[first.subsurface(x,y,64,64) for x in range(0,192,64)] for y in range(0,256,64)]
foo = Player(second, (0,0), None)
game_clock = pygame.time.Clock() # -> Dans la class map

# *- Groups (dans la class map) -* #
allSprites = pygame.sprite.Group()
player = pygame.sprite.Group()
allSprites.add(foo)
player.add(foo)

pygame.init()
window = pygame.display.set_mode((250,250))

user = True
while user:

    game_clock.tick(100)

    actualEvent = pygame.event.get()
    keyState = pygame.key.get_pressed()

    for event in actualEvent:
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE: quit()

    # -> dans le code final, la class map aura une fonction blit_everythings qui appelera entre autre les fonctions suivantes
    window.fill((0,0,0))
    foo.update(window, actualEvent, keyState)

    allSprites.draw(window)

    pygame.display.flip()