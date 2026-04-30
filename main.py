import pygame
from pygame import Rect
from pygame.locals import *

YELLOW = (255, 255, 204)
RED = (255, 0, 0)
width = 900
height = 700



class Barry:
    def __init__(self) -> None:
        #Create dog sprite (Surface object of image to display.)
        self.dog = pygame.image.load("Demo_Dog.png")
        self.dog.convert() #Optimises image format and makes drawing faster.
        #Returns rect object from an image.
        self.rect = self.dog.get_rect()

    def update(self, vector):
        self.rect.move_ip(vector)
        #Add checking for collisions with screen borders

    def draw(self, surface):
        surface.blit(self.dog, self.rect)

class Game():
    def __init__(self):
        pygame.init()
        #Create screen (Surface object representing app window.)
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.barry = None
        self.owner = None
        self.movements = {K_LEFT: (-5,0),
                          K_RIGHT: (5,0),
                          K_UP: (0,-5),
                          K_DOWN: (0,5)}

    def run(self):
        
        while self.running:
            self.screen.fill(color=YELLOW)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key in self.movements:
                        vector = self.movements[event.key]
                        self.barry.update(vector)
            self.draw()
            
        pygame.quit()

    def add_barry(self, object):
        self.barry = object

    def add_owner(self, object):
        self.owner = object        

    def draw(self):
        self.barry.draw(self.screen)
        pygame.display.flip()
        

                
                #Check sprite within borders
                # if rect.left < 0 or rect.right > WIDTH:
                #     pass
                # if rect.top < 0 or rect.bottom > HEIGHT:
                #     pass

if __name__ == "__main__":
    game = Game()
    barry = Barry()
    game.add_barry(barry)
    game.run()



