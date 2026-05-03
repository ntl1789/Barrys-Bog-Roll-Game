import pygame
from pygame import Rect
from pygame.locals import *

YELLOW = (255, 255, 204)
RED = (255, 0, 0)
width = 900
height = 700


class Sprite:
    def __init__(self, img):
        self.sprite = pygame.image.load(img)
        self.sprite.convert()
        self.rect = self.sprite.get_rect()
        self.screen_rect = Rect((0,0), (width, height))

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)


class Barry(Sprite):
    def __init__(self, img):
        super().__init__(img)
        self.rect.center = 50,650
        self.moving = False

    def update(self, vector):
        self.rect.move_ip(vector)
        #Add checking for collisions with screen borders
        self.rect.clamp_ip(self.screen_rect)


class Owner(Sprite):
    def __init__(self, img):
        super().__init__(img)        
        self.speed = [1,1]

    def update(self):
        self.rect.move_ip(self.speed)
        #Add checking for collisions with screen borders
        if self.rect.left < self.screen_rect.left:
            self.speed[0] = abs(self.speed[0])
        if self.rect.right > self.screen_rect.right:
            self.speed[0] = -abs(self.speed[0])

        if self.rect.top < self.screen_rect.top:
            self.speed[1] = abs(self.speed[1])
        if self.rect.bottom > self.screen_rect.bottom:
            self.speed[1] = -abs(self.speed[1])


class Game():
    def __init__(self):
        pygame.init()
        #Create screen (Surface object representing app window.)
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.barry = None
        self.owner = None
        self.movements = {K_LEFT: (-1,0),
                          K_RIGHT: (1,0),
                          K_UP: (0,-1),
                          K_DOWN: (0,1)}
        

    def run(self):
        while self.running:
            self.screen.fill(color=YELLOW)
            if pygame.time.get_ticks() % 75 == 0:
                self.owner.update()

            for event in pygame.event.get():
                print(event)
                if event.type == QUIT:
                    self.running = False

                if event.type == KEYDOWN:
                    barry.moving = True
                
                if event.type == KEYUP:
                    barry.moving = False

            if barry.moving:
                if event.key in self.movements:
                        self.barry.update(self.movements[event.key])

              
                    

                
                            

            if pygame.sprite.collide_rect(self.barry, self.owner):
                font = pygame.font.SysFont(None, 20)
                img = font.render("Game Over", True, RED)
                self.screen.blit(img, (450,350))
                pygame.time.delay(100)
                pygame.quit()
            self.draw()
            
        pygame.quit()

    def add_barry(self, object):
        self.barry = object

    def add_owner(self, object):
        self.owner = object        

    def draw(self):
        self.barry.draw(self.screen)
        self.owner.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    barry = Barry("Demo_Dog.png")
    owner = Owner("Demo_Owner.png")
    game.add_barry(barry)
    game.add_owner(owner)
    game.run()



