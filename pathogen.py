import pygame
pygame.init()
WIDTH = HEIGHT = 600

class Pathogen():
    def __init__(self, x, y):
        self.side = 15
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.vel = 1
        self.body = pygame.Rect(self.x, self.y, self.side, self.side)
        
    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.side, self.side))
    
    def move(self):
        self.y -= self.vel
    
    def update(self, surface):
        self.render(surface)
        self.move() 