import sys, pygame, math
pygame.init()


width = 1528
height = 800
size = width, height 
screen = pygame.display.set_mode(size)
 

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 20, 20)
blue = (20, 20, 200)
yellow = (150, 150, 0)

def soma_vetor2D(A, B): 
    return [A[0] + B[0], A[1] + B[1]]

class Ball: 
    def __init__(self): 
        self.radius = 20
        self.pos = [100, 150]
        self.vel = [0, 0]
        self.mod_vel = 50*(self.vel[0]**2 + self.vel[1]**2)
        self.acc = [0, 0]
        self.mass = 5

    def move(self):
        self.vel = soma_vetor2D(self.vel, self.acc) 
        self.pos = soma_vetor2D(self.pos, self.vel)

    def elastic_force(self):
        origin = [width/2, height/2]
        force = [0, 0]
        elastic_constant = 0.0001
        force = [-elastic_constant*(self.pos[0] - origin[0]), -elastic_constant*(self.pos[1] - origin[1])]
        
        return force

    def mouse_force(self): 
        force = [0, 0] 
        mouse = pygame.mouse.get_pos()

        #for event in pygame.event.get(): 
        if pygame.mouse.get_pressed(3)[0] == True: 
                pygame.draw.line(screen, red, self.pos, (mouse[0], mouse[1]), 3)
                pygame.draw.circle(screen, yellow, mouse, self.radius*2)
                force[0] = (mouse[0] - self.pos[0])/50000
                force[1] = (mouse[1] - self.pos[1])/50000
                
        return force 

    def get_acc(self, force):
        acc = [0, 0]
        acc[0] = force[0]/self.mass
        acc[1] = force[1]/self.mass
        return acc 
    
    def add_acc(self, acc): 
        self.acc[0] += acc[0]
        self.acc[1] += acc[1]

    def reset_acc(self):
        self.acc = [0, 0]


    def edges(self):
        if self.pos[0] < 0 or self.pos[0] > width:
            self.vel[0] = -self.vel[0]
        if self.pos[1] < 0 or self.pos[1] > height:
            self.vel[1] = -self.vel[1]

    def show(self):
        mouse = pygame.mouse.get_pos()
        ball_color = (255, 255, 255)
    #    r = 255 
    #    g = 255 
    #    b = 255
    #    if self.mod_vel <= 255:
    #        g = 255 - self.mod_vel
    #        b = 255 - self.mod_vel 
    #        ball_color = (r, g, b)
    #    else:
    #        ball_color = (255, 0, 0)
        pygame.draw.circle(screen, ball_color, self.pos, self.radius)
        pygame.draw.line(screen, blue,self.pos, (self.pos[0] + self.vel[0]*100, self.pos[1] + self.vel[1]*100), 6) #Velor Velocidade



class Obstacle: 
    def __init__(self, point_1, point_2, point_3, point_4 ): 
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.point_4 = point_4 

    def show(self): 
        pygame.draw.polygon(screen, (50, 50, 50), [self.point_1, self.point_2, self.point_3, self.point_4])
        upper_side = [(self.point_1), (self.point_2)]
        right_side = [(self.point_2), (self.point_3)]
        down_side = [(self.point_3), (self.point_4)]
        left_side = [(self.point_4), (self.point_1)]
        upper_line = pygame.draw.line(screen, (20, 20, 20), upper_side[0], upper_side[1], 10)
        right_line = pygame.draw.line(screen, (20, 20, 20), right_side[0], right_side[1], 10)
        left_line = pygame.draw.line(screen, (20, 20, 20), left_side[0], left_side[1], 10)
        down_line = pygame.draw.line(screen, (20, 20, 20), down_side[0], down_side[1], 10)


def collision(body, obstacle): 
    #COLISÃO POR CIMA
    if ((obstacle.point_1[0] <= body.pos[0] <= obstacle.point_2[0]) and (obstacle.point_1[1] <= body.pos[1] + 20 <= obstacle.point_1[1] + 5)):
        body.vel[1] = - body.vel[1]
    #COLISÃO POR BAIXO
    elif ((obstacle.point_1[0] <= body.pos[0] <= obstacle.point_2[0]) and (obstacle.point_3[1] - 5 <= body.pos[1] - 20 <= obstacle.point_3[1] )):
        body.vel[1] = - body.vel[1]
    #COLISÃO PELA DIREITA
    elif ((obstacle.point_2[0] - 5 <= body.pos[0] - 20 <= obstacle.point_2[0]) and (obstacle.point_2[1] <= body.pos[1] <= obstacle.point_3[1])):
        body.vel[0] = - body.vel[0]
    #COLISÃO PELA ESQUERDA
    elif ((obstacle.point_1[0] <= body.pos[0] + 20 <= obstacle.point_1[0] + 5) and (obstacle.point_2[1] <= body.pos[1] <= obstacle.point_3[1])):
        body.vel[0] = - body.vel[0]
    return True
        
        

ball = Ball()
obstacle_1 = Obstacle((0, 300),(1200, 300),(1200, 500),(0, 500))
obstacle_0 = Obstacle((0, 0), (1800, 0), (1800, 100), (0, 100)) 
obstacle_2 = Obstacle((600, 600), (800, 600), (800, 800), (600, 800))
obstacles_list = []
obstacles_list.append(obstacle_0)
obstacles_list.append(obstacle_1)
obstacles_list.append(obstacle_2)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)

    for i in range(len(obstacles_list)):
        obstacles_list[i].show()
        

    ball.move()
    ball.show()
    ball.reset_acc()

    force_mouse = ball.mouse_force()
    acc_1 = ball.get_acc(force_mouse)
    ball.add_acc(acc_1)

    #force_elast = ball.elastic_force()
    #acc_2 = ball.get_acc(force_elast)
    #ball.add_acc(acc_2)

    ball.edges()
    for i in range(len(obstacles_list)): 
        collision(ball, obstacles_list[i])
    
    pygame.display.flip()