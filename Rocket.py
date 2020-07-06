import turtle
#Global Vars
INITIAL_X = 0
INITIAL_Y = -100
V_i = 0
Y_i = 0
MASS = 1 #kg
g = -9.81 #N/s

class Rocket(turtle.Turtle):
    def __init__(self):
        super(Rocket,self).__init__()
        self.ht()
        self.shape('square')
        self.color('black')
        self.penup()
        self.goto(INITIAL_X, INITIAL_Y)
        self.st()
        self.speed(0) #starts at 0
        self.ddy = 0
        self.dy = V_i
        self.y = Y_i
        self.x = INITIAL_X
    def set_ddy(self, thrust):
        self.ddy = g + thrust/MASS
    def get_ddy(self):
        return self.ddy
    def set_dy(self):
        self.dy += self.ddy 
    def get_dy(self):
        return self.dy
    def set_y(self):
        self.sety(self.y + self.dy)
        self.y = self.ycor()
    def get_y(self):
        self.y = self.ycor()
        return self.y

    def gothru(self,thrust):
        self.set_ddy(thrust)
        self.set_dy()
        self.y += self.dy
        self.sety(self.y)
        return self.y
