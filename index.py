import pygame, random, os
pygame.init() 

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
BACKGROUND_COLOR = (0, 0, 0) 
CAPTION_IMAGE = pygame.image.load(os.path.join('Assets', 'virus.png')) 
pygame.display.set_caption('Game Terminal') 
pygame.display.set_icon(CAPTION_IMAGE) 

class Player():
    def __init__(self):
        self.width = self.height = 20 
        self.pos = pygame.math.Vector2(WIDTH/2 - self.width/2, HEIGHT/5 - self.height/2) 
        self.color = (0,0,255) 

    def render(self):
        pygame.draw.rect(WIN, self.color, (self.pos.x, self.pos.y, self.width, self.height)) 

    def move(self, x_vel, y_vel):
        self.pos.x += x_vel
        self.pos.y += y_vel 

player = Player() 

def draw():
    WIN.fill(BACKGROUND_COLOR) 
    player.render() 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    draw() 
    pygame.display.update() 

pygame.quit() 