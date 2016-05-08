# A Simple Obstacle Avoidance System Simulation - PV 

import serial
from visual import *

ard = serial.Serial('/dev/cu.usbmodem1421', 9600)
rod = cylinder(length=50, color=color.green, radius=0.5, pos=(-25,-2,0))
len = label(text = 'Distance to Obstacle: ', pos=(0,20,0), height=30, box=false)
target = box(color=color.red, length =.2, width=3, height=5, pos=(0,-0.5,0))
sonic = box(color=color.gray(0.5), length=1, width=3, height=3, pos=(-27,-2,0))
sonic2 = cylinder(color=color.blue, radius=1, length=1, pos=(-26,-2,0))
arr = arrow(pos=vector(0,-20,1), axis=vector(5,0,0), shaftwidth=2)


while True:
    rate(50)
    data = ard.readline().decode('utf-8').split()
    idata = float(data[0])
    rod.length = idata
    lenlabel = 'Distance to Obstacle: ' + str(idata)
    len.text = lenlabel
    target.pos = (-25+idata,-0.5, 0)
    if idata < 15:
        rod.color = color.red
        arr.axis=(-5,0,0)
    else:
        rod.color = color.green
        arr.axis=(5,0,0)

