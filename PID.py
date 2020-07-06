MAX_THRUST = 15 #N
class PID:
    def __init__(self,KP,KD,KI,TIME_STEP,target):
        self.kp = KP
        self.kd = KD
        self.ki = KI
        self.target = target
        self.time_step = TIME_STEP
        self.error = 0
        self.error_last = 0
        self.integral_error = 0
        self.proportional_error = 0
        self.derivative_error = 0

    def compute(self,pos):
        self.error = self.target - pos
        self.proportional_error = self.error 
        self.derivative_error = (self.error - self.error_last)/self.time_step
        self.integral_error += (self.error*self.time_step)
        print("proportional: ", self.proportional_error)
        print("derivative: ",self.derivative_error)
        print("integral: ",self.integral_error)
        output = self.kp*self.proportional_error + self.kd*self.derivative_error+ self.ki*self.integral_error
        print("output: ",output)
        if(output >= MAX_THRUST):
            output = MAX_THRUST
        elif(output <= 0):
            output = 0
        self.error_last = self.error
        return output




