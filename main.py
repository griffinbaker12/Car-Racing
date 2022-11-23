import pygame
import time
import math
from utils import scale_image

# surfaces represent the image object and the position on screen
GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)
TRACK_BORDER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
FINISH = pygame.image.load("imgs/finish.png")
RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)
GREY_CAR = pygame.image.load("imgs/grey-car.png")
PURPLE_CAR = pygame.image.load("imgs/purple-car.png")
WHITE_CAR = pygame.image.load("imgs/white-car.png")

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

FPS = 60

def draw(win, images):
  for img, pos in images:
    WIN.blit(img, pos)
  
run = True
clock = pygame.time.Clock()
images = [(GRASS, (0,0)), (TRACK, (0,0))]

while run:
  clock.tick(FPS)

  draw(WIN, images)

  # we represent the data or the state of the app, and then here we paint that state onto the screen
  pygame.display.update()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      break

pygame.quit()