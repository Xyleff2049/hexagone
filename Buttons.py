from pygame.locals import *
import pygame

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Papyrus', 30)

class Button(pygame.sprite.Sprite):

    def __init__(self, Surface, coords, listSprite, send=None, action=None, text="", group=None):

                        # -- Check Zone -- #
        #                   § Arguments §
        #       - Surface    : type = pygame Surface
        #       - coords     : type = tuple
        #       - listSprite : type = list / contains = pygame image
        #       - text       : type = string (optional)
        #       - group      : type = pygame Group
        #       - send       : type = str, bool, Object, ...
        #       - action     : type = str that Python can exec

        try:
            if type(coords) != tuple or type(listSprite) != list or type(text) != str: raise TypeError
            if send != None and action != None: raise AttributeError
        except TypeError:
            print('[>Button] A TypeError has occurred, read the help')
            quit()
        except AttributeError:
            print('[>Button] One of the send or action arguments have to be empty (None)')
            quit()

        # -- Initialisation Zone -- #
        if group != None: pygame.sprite.Sprite.__init__(self, group)
        else: pygame.sprite.Sprite.__init__(self)

        # -> Display
        self.sprite_sheet = listSprite
        self.statut = 0
        self.image = self.sprite_sheet[0]
        self.rect = self.image.get_rect()
        (self.rect.x, self.rect.y) = coords
        (self.width, self.height) = self.image.get_size()
        self.surface = Surface

        # -> Text
        self.text = font.render(text, True, (235,170,170))
        self.text_pos = self.text.get_rect(centerx= self.rect.x + (self.width / 2), centery=self.rect.y + (self.height / 2))
        # self.text_pos = self.text.get_rect(centerx=self.width / 2, centery=self.height / 2)
        # self.image.blit(self.text, self.text_pos) # -> Inutilisable ? Modifie l'image source : les textes se superposent

        # -> Group
        self.item_group = pygame.sprite.Group(self)

        # -> Action
        self.send = send
        self.action = action

    def add_to_group(self, listGroup):

        for group in listGroup:
            if self not in group.sprites(): group.add(self)

    def when_clicked(self):

        if self.action != None and type(self.action) == str: exec(self.action)
        elif self.send != None: return self.send

    def change_statut(self, statut):
        self.statut = statut
        self.image = self.sprite_sheet[statut]

class Menu(pygame.sprite.Group):

    def __init__(self, *argv):

        pygame.sprite.Group.__init__(self, argv)

        self.result = None

    def menu_display(self, Surface):

        for sprite in self.sprites():

            sprite.item_group.draw(Surface)
            Surface.blit(sprite.text, sprite.text_pos)

    def menu_event(self, actualEvent):

        # for event in actualEvent:

        if pygame.event.get(MOUSEBUTTONUP):

            for sprite in self.sprites():

                if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                    # return sprite.when_clicked()
                    self.result = sprite.when_clicked()

        elif pygame.event.get(MOUSEMOTION):

            (x,y) = pygame.mouse.get_pos()

            for sprite in self.sprites():

                if sprite.rect.collidepoint(x,y): sprite.change_statut(1)
                elif sprite.rect.collidepoint(x,y) == False and sprite.statut == 1: sprite.change_statut(0)

def game_quit():

    print('[>Game] Shutting down')
    # Stop music
    pygame.quit()
    print('Bye ' + chr(3))
    quit()

if __name__ == '__main__':

    first = pygame.image.load('mainButtons.png')
    second = [first.subsurface(x,y, 200,50) for x in range(0, 200, 200) for y in range(0, 150, 50)]

    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Papyrus', 30)
    window = pygame.display.set_mode((350, 400))

    playButton = Button(window, (75,50), second, text="Jouer", send="start")
    setButton = Button(window, (75, 175), second, text="Options", send="settings")
    quitButton = Button(window, (75, 300), second, text="Quitter", action="game_quit()")

    test = Menu(playButton, setButton, quitButton)

    user = True
    while user:

        if pygame.event.get(QUIT): game_quit()

        test.menu_event(None)
        test.menu_display(window)

        if test.result != None:        
            if test.result == 'start': print('[>Menu] Game start')
            elif test.result == 'settings': print('[>Menu] Open settings')
            test.result = None

        pygame.display.flip()