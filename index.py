import pygame, os, random
import player

WIDTH = HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = (0, 0, 0)
ICON_IMG = pygame.image.load(os.path.join('Assets', 'virus.png'))
FPS = 60 

pygame.display.set_caption('GAME WINDOW')
pygame.display.set_icon(ICON_IMG)

monocyte = player.Monocyte()
lyphocyte = player.Lyphocyte()    

def draw():
    WIN.fill(BACKGROUND_COLOR)
    # monocyte.update(WIN) 
    lyphocyte.update(WIN) 

clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    draw()
    pygame.display.update()
    
pygame.quit() 