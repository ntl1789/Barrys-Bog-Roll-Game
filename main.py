import pygame
from pygame import Rect
from pygame import locals

YELLOW = (255, 255, 204)
RED = (255, 0, 0)

pygame.init()

#Create screen (Surface object representing app window.)
screen = pygame.display.set_mode((900, 700))
screen.fill(color=YELLOW)

#Create dog sprite (Surface object of image to display.)
dog = pygame.image.load("Demo_Dog.png")
dog.convert()
#Create Rect object - bounding rectangle of image
rect = dog.get_rect()

#Add dog and rect to screen
screen.blit(dog, rect)
pygame.draw.rect(screen, RED, rect, 1)
pygame.display.update()


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


