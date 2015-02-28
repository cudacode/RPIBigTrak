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

class Robot:
	'Test Class for Robot: should allow you to see the programmed movements'

	def __init__ (self):
		self.top = Tkinter.Tk()
		self.top.wm_title("Map")
		self.top.geometry('{}x{}'.format(1000, 1000))
		self.tank = Tkinter.Canvas(self.top, height=13, width=6, bg='blue')
		self.tankx = 500
		self.tanky = 500
		self.tankh = 3.1415926499999998
		self.tank.place(x=500, y=500)
		print ("Robot Ready")

	def execute(self, command):
		print 'Name: ', command.name, ", Parameter: ", command.param1 

		if command.name == 'fwd':
			self.forward(int(command.param1))

	def forward(self, distance):
		# Tank is 13" long so that is what 1 =
		x = math.sin(self.tankh)
		y = math.cos(self.tankh)
		while distance > 0:
			self.tankx = self.tankx + (13 * x)
			self.tanky = self.tanky + (13 * y)
			self.tank.place(x=self.tankx, y=self.tanky)
			distance = distance - 1
		print 'x=', self.tankx, ' y=', self.tanky