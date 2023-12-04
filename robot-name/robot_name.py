import random
import string

##class Robot:
##    def __init__(self):
##        letters = ''.join(random.choice(string.ascii_uppercase)for i in range(2))
##        numbers = ''.join(random.choice(string.digits)for i in range(3))
##        name = (letters + numbers)
##        self.name = name    
##    def reset(self):
##        self.name = name
##    
##robot = Robot()
##name = robot.name


class Robot:
    def __init__(self):
        name = random.choice([A-Z]{2}\d{3}$)
        self.name = name
    def reset(self):
        self.name = name
