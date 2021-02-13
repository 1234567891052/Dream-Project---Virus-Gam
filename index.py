import pygame, os, random
import leycocyte, pathogen

WIDTH = HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = (0, 0, 0)
ICON_IMG = pygame.image.load(os.path.join('Assets', 'virus.png'))
FPS = 60  

pygame.display.set_caption('GAME WINDOW')
pygame.display.set_icon(ICON_IMG)

macrophage = leycocyte.Macrophage(WIDTH / 2, HEIGHT / 6)
neutrophil = leycocyte.Neutrophil(WIDTH / 2, HEIGHT / 4)

bacteria = pathogen.Bacteria()
bacteria.initialise(WIDTH, HEIGHT)

fungi = pathogen.Fungi()
fungi.initialise(WIDTH, HEIGHT) 

def draw():
    WIN.fill(BACKGROUND_COLOR)

    # macrophage.update(WIN, WIDTH, HEIGHT)
    # macrophage.kill_pathogen(bacteria.bodies)
    # macrophage.kill_pathogen(fungi.bodies)
    
    neutrophil.update(WIN, WIDTH, HEIGHT, bacteria.bodies, fungi.bodies) 

    bacteria.update(WIN, HEIGHT)
    fungi.update(WIN, HEIGHT) 
    
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