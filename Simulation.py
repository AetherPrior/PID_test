from Rocket import Rocket
from PID import PID
import turtle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
TIME_STEP = 0.001
SETPOINT = 10
SIM_TIME = 500
#ku = 0.47
#t = 18
KP = 0.282
KD = 0.0006345
KI = 31.332

class Simulation:
    def __init__(self):
        self.PID = PID(KP,KD,KI,TIME_STEP,SETPOINT)
        self.YEETUS = Rocket()
        self.screen = turtle.Screen()
        self.screen.setup(640,768)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.left(180)
        self.marker.goto(15,SETPOINT)
        self.marker.color('red')
        self.sim = True
        self.timer = 0
        self.x = []
        self.y = []
    def cycle(self):
        while(self.sim):
            thrust = self.PID.compute(self.YEETUS.get_y())
            print(thrust)
            y = self.YEETUS.gothru(thrust)
            time.sleep(TIME_STEP)
            self.timer+=1
            if self.timer > SIM_TIME:
                self.sim = False
            elif y > 400:
                self.sim = False
            elif y < -400:
                self.sim = False
            self.x.append(self.timer)
            self.y.append(self.YEETUS.get_y())
        print("Done")
        plt.title("Position wrt time")
        plt.xlabel("time")
        plt.ylabel("ycoordinate")
        plt.plot(self.x,self.y)
        plt.show()
            
def main():
    sim = Simulation()
    sim.cycle()

if __name__ == '__main__':
    main()

