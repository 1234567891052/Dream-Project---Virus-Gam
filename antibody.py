import pygame
pygame.init() 
WIDTH = HEIGHT = 600

class Antibody():
    def __init__(self):
        self.side = 20
        self.x = WIDTH / 2 - self.side / 2
        self.y = HEIGHT / 6 - self.side / 2
        self.color = (0, 0, 255)
        self.vel = 5
        self.body = pygame.Rect(self.x, self.y, self.side, self.side)
        
    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.side, self.side))
        
    def move(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_a] and self.x > 0:
            self.x -= self.vel
        if keypressed[pygame.K_d] and self.x + self.side < WIDTH:
            self.x += self.vel
        if keypressed[pygame.K_w] and self.y > 0:
            self.y -= self.vel
        if keypressed[pygame.K_s] and self.y + self.side < HEIGHT:
            self.y += self.vel 
            
    def update(self, surface):
        self.render(surface)
        self.move() 
