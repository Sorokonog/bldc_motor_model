import math
import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

RADIUS_OF_MAGNETS = 15
RADIUS_OF_UPPER_END_OF_COILS = 14.9
RADIUS_OF_DOWN_END_OF_COILS = 12.9

class Magnet:
    def __init__(self, x, y, polarity):
        self.x = x
        self.y = y
        self.polarity = polarity

class Motor:
    def __init__(self, number_of_magnets, number_of_coils, phy, offset):
        self.number_of_magnets = number_of_magnets
        self.number_of_coils = number_of_coils
        self.phy = phy
        self.magnets = pin_magnets(self.number_of_magnets, RADIUS_OF_MAGNETS)
        """
        self.coils = assemble_down_coils(self.number_of_coils, 
                                            RADIUS_OF_DOWN_END_OF_COILS,
                                            assemble_upper_coils(self.number_of_coils, 
                                                                RADIUS_OF_UPPER_END_OF_COILS,
                                                                self.phy)
                                            , self.phy)
        """
        self.coils = assemble_upper_coils(self.number_of_coils, 
                                                                RADIUS_OF_UPPER_END_OF_COILS,
                                                                self.phy)
        set_voltage(self.coils,10, offset)


    def set_state(self):
        pass

    def rotate_motor(self, angle):
        pass


class Coil:
    def __init__(self, x, y, polarity, V):
        self.x = x
        self.y = y
        self.polarity = polarity
        self.V = V


def count_curent_moment(Motor):
    M = [0 for i in range(len(Motor.coils))]
    for i in range(len(Motor.coils)):
        for j in range(len(Motor.magnets)):
            M[i] = Motor.coils[i].V/((Motor.coils[i].x - Motor.magnets[j].x)**2 + (Motor.coils[i].y - Motor.magnets[j].y)**2 
                    * (Motor.coils[i].polarity * Motor.magnets[j].polarity))
    return sum(M)

def pin_magnets(n_magnets, r):
    magnets = []
    for i in range(n_magnets):
        phy = 2*math.pi / n_magnets * i
        magnets.append(Magnet(r*math.cos(phy), r*math.sin(phy), (i%2*2-1)))
    return magnets

def assemble_upper_coils(n_coils, r, rotate_angle):
    coils = []
    for i in range(n_coils):
        phy = 2*math.pi / n_coils * i
        coils.append(Coil(r*math.cos(phy + rotate_angle), r*math.sin(phy + rotate_angle), (i%2*2-1), 0))
    return coils

def assemble_down_coils(n_coils, r, coils, rotate_angle):
    for i in range(n_coils):
        phy = 2*math.pi / n_coils * i
        coils.append(Coil(r*math.cos(phy + rotate_angle), r*math.sin(phy + rotate_angle), -(i%2*2-1), 0))
    return coils

def set_voltage(coils, level, offset):
    coils[0].V = math.sin(offset) * level
    coils[1].V = math.sin(offset) * level
    coils[6].V = math.sin(offset) * level
    coils[7].V = math.sin(offset) * level

    coils[2].V = math.sin(offset + 2*math.pi/3) * level
    coils[3].V = math.sin(offset + 2*math.pi/3) * level
    coils[8].V = math.sin(offset + 2*math.pi/3) * level
    coils[9].V = math.sin(offset + 2*math.pi/3) * level

    coils[4].V = math.sin(offset + 4*math.pi/3) * level
    coils[5].V = math.sin(offset + 4*math.pi/3) * level
    coils[10].V = math.sin(offset + 4*math.pi/3) * level
    coils[11].V = math.sin(offset + 4*math.pi/3) * level

    #for i in range(11):
    #    coils[i+11].V = 0

moments = []
moments_single = []


phy = np.arange(-math.pi,math.pi,0.01)
#offset = np.arange(-math.pi, math.pi, 0.01)

"""
for i in range(len(offset)):
    moments.append(count_curent_moment(Motor(14,12,-2*math.pi/12,offset[i])))
"""

for i in range(len(phy)):
    moments.append(count_curent_moment(Motor(14,12,0,phy[i])))

plt.figure()
#plt.subplot(211)
plt.plot(phy, moments, lw=2)

'''
xs = []
ys = []
for i in m.coils:
    xs.append(i.x)
    ys.append(i.y)
plt.plot(xs,ys,lw=3)
'''

#plt.plot(offset, moments_single, lw=2)
plt.show()
