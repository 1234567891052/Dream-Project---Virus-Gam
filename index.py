import pygame, os, random
import antibody, pathogen 

WIDTH = HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = (0, 0, 0)
ICON_IMG = pygame.image.load(os.path.join('Assets', 'virus.png'))
FPS = 60 

pygame.display.set_caption('GAME WINDOW')
pygame.display.set_icon(ICON_IMG)

player = antibody.Antibody()

pathogens = []
PATHOGEN_LIMIT = 5
for i in range(PATHOGEN_LIMIT):
    pathogen_body = pathogen.Pathogen(random.randint(15, WIDTH - 15), random.randint(HEIGHT - 15, HEIGHT + 15)) 
    pathogens.append(pathogen_body) 

def draw():
    WIN.fill(BACKGROUND_COLOR)

    player.update(WIN)
    player_temp = pygame.Rect(player.x, player.y, player.side, player.side)
    
    for i in pathogens:
        i.update(WIN)
        i_temp = pygame.Rect(i.x, i.y, i.side, i.side)

        if player_temp.colliderect(i_temp):
            pathogens.remove(i) 

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