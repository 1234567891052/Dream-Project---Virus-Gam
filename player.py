import pygame, os, random
pygame.init() 
WIDTH = HEIGHT = 600

class Monocyte():
    # Monocytes. They have a longer lifespan than many white blood cells and help to break down bacteria.
    def __init__(self):
        self.color = (0, 255, 0) 
        self.center_x = WIDTH / 2 
        self.center_y = HEIGHT / 6
        self.radius = 15
        self.vel = 5 

    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.center_x, self.center_y), self.radius) 

    def move(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_a] and self.center_x - self.radius > 0:
            self.center_x -= self.vel
        if keypressed[pygame.K_d] and self.center_x + self.radius < WIDTH:
            self.center_x += self.vel
        if keypressed[pygame.K_w] and self.center_y - self.radius > 0:
            self.center_y -= self.vel
        if keypressed[pygame.K_s] and self.center_y + self.radius < HEIGHT:
            self.center_y += self.vel 

    def update(self, surface):
        self.render(surface)
        self.move() 

class Lyphocyte():
    # Lymphocytes. They create antibodies to fight against bacteria, viruses, and other potentially harmful invaders.
    def __init__(self):
        self.color = (0, 0, 255) 
        self.center_x = WIDTH / 2 
        self.center_y = HEIGHT / 6 
        self.radius = 10 
        self.vel = 5 

    def render(self, surface):
        pygame.draw.circle(surface, self.color, (self.center_x, self.center_y), self.radius) 
    
    def move(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_a] and self.center_x - self.radius > 0:
            self.center_x -= self.vel
        if keypressed[pygame.K_d] and self.center_x + self.radius < WIDTH:
            self.center_x += self.vel
        if keypressed[pygame.K_w] and self.center_y - self.radius > 0:
            self.center_y -= self.vel
        if keypressed[pygame.K_s] and self.center_y + self.radius < HEIGHT:
            self.center_y += self.vel 

    def update(self, surface):
        self.render(surface)
        self.move() 