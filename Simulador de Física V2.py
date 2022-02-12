import sys, pygame
pygame.init()

size = width, height = 1200, 800
screen = pygame.display.set_mode(size)

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 20, 20)
blue = (20, 20, 200)

def soma_vetor2D(A, B): 
    return [A[0] + B[0], A[1] + B[1]]

class Ball: 
    def __init__(self): 
        self.radius = 20
        self.pos = [400, 300]
        self.vel = [1, 1]
        self.acc = [0, 0]

    def move(self):
        mouse = pygame.mouse.get_pos() 
        self.acc[0] = (mouse[0] - self.pos[0])/50000
        self.acc[1] = (mouse[1] - self.pos[1])/50000
        self.vel = soma_vetor2D(self.vel, self.acc) 
        self.pos = soma_vetor2D(self.pos, self.vel)

    def elastic_force(self):
        return True

    def mouse_force(self): 
        force = [] 
        force[0] = (mouse[0] - self.pos[0])/50000
        force[1] = (mouse[1] - self.pos[1])/50000
        return force 

    def get_acc(self, force):
        return True 
    
    def add_acc(self, acc): 
        self.acc[0] += force[0]
        self.acc[1] += force[1]


    def edges(self):
        if self.pos[0] < 0 or self.pos[0] > width:
            self.vel[0] = -self.vel[0]
        if self.pos[1] < 0 or self.pos[1] > height:
            self.vel[1] = -self.vel[1]

    def show(self):
        mouse = pygame.mouse.get_pos()
        pygame.draw.circle(screen, white, self.pos, self.radius)
        pygame.draw.line(screen, red, self.pos, (mouse[0], mouse[1]), 3) #Vetor Aceleração 
        pygame.draw.line(screen, blue,self.pos, (self.pos[0] + self.vel[0]*100, self.pos[1] + self.vel[1]*100), 3) #Velor Velocidade
     

ball = Ball()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    ball.move()
    ball.edges()
    screen.fill(black)

    ball.show()
    pygame.display.flip()
