'''
Modified version of
http://stackoverflow.com/questions/21754903/using-pyserial-to-plot-time-against-voltage-from-an-arduino-serial-port
'''

import serial
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class AnalogPlot:
  # constr
  def __init__(self, strPort, maxLen):
      # open serial port
      self.ser = serial.Serial(strPort, 9600)

      self.ax = deque([0.0]*maxLen)
      self.ay = deque([0.0]*maxLen)
      self.maxLen = maxLen

  def addToBuf(self, buf, val):
      if len(buf) < self.maxLen:
          buf.append(val)
      else:
          buf.pop()
          buf.appendleft(val)

  def add(self, data):
      assert(len(data) == 2)
      self.addToBuf(self.ax, data[0])
      self.addToBuf(self.ay, data[1])

  def update(self, frameNum, a0, a1):
      try:
          line = self.ser.readline()
          idat = line.decode('utf-8').strip()
          data = [idat, idat]
          # print data
          if(len(data) == 2):
              self.add(data)
              a0.set_data(range(self.maxLen), self.ax)
              a1.set_data(range(self.maxLen), self.ay)
      except KeyboardInterrupt:
          print('exiting')

      return a0,

  def close(self):
      # close serial
      self.ser.flush()
      self.ser.close()


def main():

  strPort = '/dev/cu.usbmodem1421'

  print('reading from serial port %s...' % strPort)

  analogPlot = AnalogPlot(strPort, 100)

  print('plotting data...')

  fig = plt.figure()
  ax = plt.axes(xlim=(0, 50), ylim=(0, 50))
  plt.axhline(y=10)
  a0, = ax.plot([], [])
  a1, = ax.plot([], [])
  anim = animation.FuncAnimation(fig, analogPlot.update,
                                 fargs=(a0, a1),
                                 interval=50)
  plt.show()

  analogPlot.close()

  print('exiting.')


if __name__ == '__main__':
  main()
