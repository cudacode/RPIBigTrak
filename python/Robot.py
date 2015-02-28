import Tkinter
import math

class Robot:
	'Test Class for Robot'

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