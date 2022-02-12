import sys, pygame
pygame.init()

size = width, height = 1200, 800
screen = pygame.display.set_mode(size)

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 20, 20)
blue = (20, 20, 200)



class Ball: 
    def __init__(self): 
        self.radius = 20
        self.x_pos = 400
        self.y_pos = 300
        self.x_vel = 1
        self.y_vel = 1 
        self.x_acc = 0
        self.y_acc = 0

    def move(self):
        mouse = pygame.mouse.get_pos() 
        self.x_acc = (mouse[0] - self.x_pos)/50000
        self.y_acc = (mouse[1] - self.y_pos)/50000
        self.x_vel += self.x_acc
        self.y_vel += self.y_acc
        self.x_pos += self.x_vel 
        self.y_pos += self.y_vel


    def edges(self):
        if self.x_pos < 0 or self.x_pos > width:
            self.x_vel = -self.x_vel
        if self.y_pos < 0 or self.y_pos > height:
            self.y_vel = -self.y_vel

    def show(self):
        mouse = pygame.mouse.get_pos()
        center = (self.x_pos, self.y_pos)
        pygame.draw.circle(screen, white, center, self.radius)
        pygame.draw.line(screen, red, (self.x_pos, self.y_pos), (mouse[0], mouse[1]), 3) #Vetor Aceleração 
        pygame.draw.line(screen, blue,(self.x_pos, self.y_pos), (self.x_pos + self.x_vel*100, self.y_pos + self.y_vel*100), 3) #Velor Velocidade


        

ball = Ball()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    ball.move()
    ball.edges()
    screen.fill(black)

    ball.show()
    pygame.display.flip()







    
