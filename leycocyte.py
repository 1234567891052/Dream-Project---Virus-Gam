import pygame, random
pygame.init()

class Macrophage():
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
        
        if keypressed[pygame.K_a] and self.center_x - self.radius > 0:
            self.center_x -= self.vel
        if keypressed[pygame.K_d] and self.center_x + self.radius < WIDTH:
            self.center_x += self.vel
        
        if keypressed[pygame.K_w] and self.center_y - self.radius > 0 :
            self.center_y -= self.vel
        if keypressed[pygame.K_s] and self.center_y + self.radius < HEIGHT:
            self.center_y += self.vel

    def kill_pathogen(self, arr):
        self_temp = pygame.Rect(self.center_x - self.radius, self.center_y - self.radius, 2 * self.radius, 2 * self.radius) 

        for i in arr:
            i_temp = pygame.Rect(i.x, i.y, i.side, i.side)
            if self_temp.colliderect(i_temp):
                arr.remove(i) 

    def update(self, WIN, WIDTH, HEIGHT):
        self.render(WIN)
        self.move(WIDTH, HEIGHT)
        
class Neutrophil():
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = 10
        self.color = (0, 0, 255)
        self.vel = 6
        self.chemical_limit = 50
        self.chemicals = [] 
        
    class Neutorphilphil_chemical():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.side = 5 
            self.vel = pygame.math.Vector2(random.randint(-2, 2), random.randint(-2, 2)) 
            self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            self.offset = 10 

        def render(self, WIN):
            pygame.draw.rect(WIN, self.color, (self.x, self.y, self.side, self.side))
            
        def move(self):
            self.x += self.vel.x
            self.y += self.vel.y

            if random.random() < 0.5:
                self.vel.x + self.offset
                self.vel.y + self.offset
            else:
                self.vel.x - self.offset
                self.vel.y - self.offset
                
        def kill_bacteria(self, arr):
            self_temp = pygame.Rect(self.x, self.y, self.side, self.side)

            for i in arr:
                i_temp = pygame.Rect(i.x, i.y, i.side, i.side)

                if self_temp.colliderect(i_temp):
                    arr.remove(i)
                    
        def kill_fungi(self, arr):
            self_temp = pygame.Rect(self.x, self.y, self.side, self.side)

            for i in arr:
                i_temp = pygame.Rect(i.x, i.y, i.side, i.side)

                if self_temp.colliderect(i_temp):
                    i.health -= 1

                if i.health <= 0:
                    arr.remove(i) 
            
        def update(self, WIN, bac_arr, fung_arr):
            self.render(WIN)
            self.move()
            self.kill_bacteria(bac_arr)
            self.kill_fungi(fung_arr) 
    
    def render(self, WIN):
        pygame.draw.circle(WIN, self.color, (self.center_x, self.center_y), self.radius)
        
    def move(self, WIDTH, HEIGHT):
        keypressed = pygame.key.get_pressed()
        
        if keypressed[pygame.K_a] and self.center_x - self.radius > 0:
            self.center_x -= self.vel
        if keypressed[pygame.K_d] and self.center_x + self.radius < WIDTH:
            self.center_x += self.vel
        
        if keypressed[pygame.K_w] and self.center_y - self.radius > 0:
            self.center_y -= self.vel
        if keypressed[pygame.K_s] and self.center_y + self.radius < HEIGHT:
            self.center_y += self.vel

    def release_chemicals(self, WIN, bac_arr, fung_arr):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_SPACE] and self.chemical_limit > 0:
            chemical = self.Neutorphilphil_chemical(self.center_x, self.center_y)
            self.chemicals.append(chemical)
            self.chemical_limit -= 0.4
            
        for i in self.chemicals:
            i.update(WIN, bac_arr, fung_arr) 

    def update(self, WIN, WIDTH, HEIGHT, bac_arr, fung_arr):
        self.render(WIN)
        self.move(WIDTH, HEIGHT)
        self.release_chemicals(WIN, bac_arr, fung_arr)  