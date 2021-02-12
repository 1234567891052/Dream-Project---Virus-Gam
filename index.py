import pygame, os, random
import leycocyte

WIDTH = HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = (0, 0, 0)
ICON_IMG = pygame.image.load(os.path.join('Assets', 'virus.png'))
FPS = 60  

pygame.display.set_caption('GAME WINDOW')
pygame.display.set_icon(ICON_IMG)

neutrophil = leycocyte.Neutorphil(WIDTH / 2, HEIGHT / 6)
eosionphil = leycocyte.Eosionphil(WIDTH / 2, HEIGHT / 4)

def draw():
    WIN.fill(BACKGROUND_COLOR)
    neutrophil.update(WIN, WIDTH, HEIGHT)
    eosionphil.update(WIN, WIDTH, HEIGHT) 

clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and eosionphil.chemical_limit > 0:
                eosionphil.release_chemicals(WIN)
                print('hu')
    draw()
    pygame.display.update()
    
pygame.quit() 