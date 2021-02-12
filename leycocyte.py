import pygame, random
pygame.init()

# NEUTROPHIL - ENGULFING PATHOGNE - TARGET PATHOGENS = BACTERIA AND FUNGI
# EOSINOPHIL - SECRETE CHEMICALS -  TARGET PATHOGENS = LARGER PARASITES

class Neutorphil():
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = 10 
        self.color = (255, 255, 0)
        self.vel = 5
        self.pathogen_limit = 20
        
    def render(self, WIN):
        pygame.draw.circle(WIN, self.color, (self.center_x, self.center_y), self.radius)

    def move(self, WIDTH, HEIGHT):
        keypressed = pygame.key.get_pressed()
        
        if keypressed[pygame.K_a] and self.center_x - self.radius > 0 :
            self.center_x -= self.vel
        if keypressed[pygame.K_d] and self.center_x + self.radius < WIDTH :
            self.center_x += self.vel
        
        if keypressed[pygame.K_w] and self.center_y - self.radius > 0 :
            self.center_y -= self.vel
        if keypressed[pygame.K_s] and self.center_y + self.radius < HEIGHT :
            self.center_y += self.vel

    def update(self, WIN, WIDTH, HEIGHT):
        self.render(WIN)
        self.move(WIDTH, HEIGHT)
        
class Eosionphil():
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = 10
        self.color = (0, 0, 255)
        self.vel = 6
        self.chemical_limit = 100
        self.chemicals = [] 
        
    class Eosionphil_chemical():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.width = 5
            self.height = 5 
            self.vel = pygame.math.Vector2(random.randint(-5, 5), random.randint(-5, 5)) 
            self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

        def render(self, WIN):
            pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))
            
        def move(self):
            self.x += self.vel.x
            self.y += self.vel.y
            
        def update(self, WIN):
            self.render(WIN)
            self.move() 
    
    def render(self, WIN):
        pygame.draw.circle(WIN, self.color, (self.center_x, self.center_y), self.radius)
        
    def move(self, WIDTH, HEIGHT):
        keypressed = pygame.key.get_pressed()
        
        if keypressed[pygame.K_a] and self.center_x - self.radius > 0 :
            self.center_x -= self.vel
        if keypressed[pygame.K_d] and self.center_x + self.radius < WIDTH :
            self.center_x += self.vel
        
        if keypressed[pygame.K_w] and self.center_y - self.radius > 0 :
            self.center_y -= self.vel
        if keypressed[pygame.K_s] and self.center_y + self.radius < HEIGHT :
            self.center_y += self.vel

    def release_chemicals(self, WIN):
        chemical = self.Eosionphil_chemical(self.center_x, self.center_y)
        self.chemicals.append(chemical)
        for i in self.chemicals:
            i.update(WIN)
        
        self.chemical_limit -= 1

    def update(self, WIN, WIDTH, HEIGHT):
        self.render(WIN)
        self.move(WIDTH, HEIGHT)