import pygame, random
pygame.init()

class Bacteria():
    def __init__(self):
        self.bacteria_limit = 10 
        self.bodies = []
    
    class Bacterium():
        def __init__(self, WIDTH, HEIGHT):
            self.x = random.randint(15, WIDTH - 15)
            self.y = random.randint(HEIGHT + 100, HEIGHT + 500)
            self.side = 12
            self.color = (255, 0, 0)
            self.vel = 1.1

        def render(self, WIN):
            pygame.draw.rect(WIN, self.color, (self.x, self.y, self.side, self.side))
            
        def move(self, HEIGHT):
            if self.y > 0:
                self.y -= self.vel
        
        def update(self, WIN, HEIGHT):
            self.render(WIN)
            self.move(HEIGHT)

    def initialise(self, WIDTH, HEIGHT):
        for i in range(self.bacteria_limit):
            bacterium = self.Bacterium(WIDTH, HEIGHT)
            self.bodies.append(bacterium)
            
    def update(self, WIN, HEIGHT):
        for i in self.bodies:
            i.update(WIN, HEIGHT)
            
class Fungi():
    def __init__(self):
        self.fungi_limit = 12
        self.bodies = []
        
    class Fungus():
        def __init__(self, WIDTH, HEIGHT):
            self.x = random.randint(15, WIDTH - 15)
            self.y = random.randint(HEIGHT + 100, HEIGHT + 500)
            self.side = 15
            self.color = (0, 255, 0) 
            self.vel = 1
            self.health = 2 
        
        def render(self, WIN):
            pygame.draw.rect(WIN, self.color, (self.x, self.y, self.side, self.side))
        
        def move(self, HEIGHT):
            if self.y > 0:
                self.y -= self.vel
                
        def update(self, WIN, HEIGHT):
            self.render(WIN)
            self.move(HEIGHT)
            
    def initialise(self, WIDTH, HEIGHT):
        for i in range(self.fungi_limit):
            fungus = self.Fungus(WIDTH, HEIGHT)
            self.bodies.append(fungus)
            
    def update(self, WIN, HEIGHT):
        for i in self.bodies:
            i.update(WIN, HEIGHT)  