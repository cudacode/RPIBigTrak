# Copyright (c) 2015 'cudacode'

# Permission is hereby granted, free of charge, to any person obtaining a copy of this 
# software and associated documentation files (the "Software"), to deal in the Software 
# without restriction, including without limitation the rights to use, copy, modify, 
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject to the following 
# conditions:

# The above copyright notice and this permission notice shall be included in all copies 
# or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
# OR OTHER DEALINGS IN THE SOFTWARE.

import Tkinter
import math
import time

TANK_LENGTH = 13
TANK_WIDTH = 6
REVERSE_HEADING_ADJ = 3.14159265
STARTING_HEADING = 3.14159265

# The actual toy only allow entry of two digits and they made it so that 60 was a full
# rotation of the tank.
FULL_ROTATION_UNITS = 60

class Robot:
	'Test Class for Robot: should allow you to see the programmed movements'

	def __init__ (self):
		self.top = Tkinter.Tk()
		self.top.wm_title("Map")
		self.top.geometry('{}x{}'.format(1000, 1000))
		# Tank is 13"x6"
		self.tank = Tkinter.Canvas(self.top, height=TANK_LENGTH, width=TANK_WIDTH, bg='blue')
		
		#Start in the middle of the map
		self.tankx = 500
		self.tanky = 500
		
		#Heading is due North in Radians
		self.tankh = STARTING_HEADING
		
		self.tank.place(x=self.tankx, y=self.tanky)
		print ("Robot Ready")

	def execute(self, command):
		print 'Name: ', command.name, ", Parameter: ", command.param1 

		if command.name == 'fwd':
			self.forward(int(command.param1))
		elif command.name == 'back':
			self.reverse(int(command.param1))
		elif command.name == 'hold':
			self.hold(int(command.param1))
		elif command.name == 'left':
			self.rotate(int(command.param1))
		elif command.name == 'right':
			self.rotate(-int(command.param1))

	def forward(self, distance):
		x = math.sin(self.tankh)
		y = math.cos(self.tankh)
		while distance > 0:
			self.tankx = int(round(self.tankx + (TANK_LENGTH * x)))
			self.tanky = int(round(self.tanky + (TANK_LENGTH * y)))
			self.tank.place(x=self.tankx, y=self.tanky)
			distance = distance - 1
		print 'x=', self.tankx, ' y=', self.tanky
		
	def hold(self, seconds):
		time.sleep(seconds)	
	
	# Doing left as adding rotation and right as subtracting 
	def rotate(self, rotation):
		print 'Heading:', self.tankh
		print 'Rotation:', rotation
		adjHeading = ((rotation / 60.0) * (2.0 * STARTING_HEADING))
		print 'Adjustment:', adjHeading
		self.tankh = self.tankh + adjHeading
		print 'Heading:', self.tankh
		
	def reverse(self, distance):
		revHeading = self.tankh - REVERSE_HEADING_ADJ
		x = math.sin(revHeading)
		y = math.cos(revHeading)
		while distance > 0:
			self.tankx = int(round(self.tankx + (TANK_LENGTH * x)))
			self.tanky = int(round(self.tanky + (TANK_LENGTH * y)))
			self.tank.place(x=self.tankx, y=self.tanky)
			distance = distance - 1
		print 'x=', self.tankx, ' y=', self.tanky
		
		