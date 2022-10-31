import math

class Magnet:
    def __init__(self, x, y, polarity):
        self.x = x
        self.y = y
        self.polarity = polarity

class Motor:
    def __init__(self, number_of_magnets, number_of_coils):
        self.number_of_magnets = number_of_magnets
        self.number_of_coils = number_of_coils
        self.magnet = pin_magnets()
        self.coils = assemble_coils()

    def set_state(self):
        pass

    def rotate_motor(self, angle):
        pass

class Coil:
    def __init__(self, x, y, polarity):
        self.x = x
        self.y = y
        self.polarity = polarity



def count_curent_moment(Motor, V):
    M = []
    for i in range(len(Motor.coils)):
        for j in range(len(Motor.magnets)):
            M[i] = V/(Motor.coils[i].x - Motor.magnet[j].x)^2 + (Motor.coils[i].x - Motor.magnet[j].x)^2 * (Motor.coils[i].V * Motor.magnets[j].polarity)
    return sum(M)

def pin_magnets(n_magnets, r):
    magnets = []
    for i in range(n_magnets):
        phy = 2*math.pi / n_magnets * i
        magnets.append(Magnet(r*math.cos(phy), r*math.sin(phy), i%2))
    return magnets

def assemble_coils(n_coils, r):
    coils = []
    for i in range(n_coils):
        phy = 2*math.pi / n_coils * i
        coils.append(Coil(r*math.cos(phy), r*math.sin(phy), i%2))
    return coils


m = Motor(magnets = 14,coils = 12)