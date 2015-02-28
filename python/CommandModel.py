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

import Command
import Robot

class CommandModel:
	'Model for command interface'

	def __init__ (self, cmdVar):
		self.cmdList = []
		self.cmdVar = cmdVar
		self.cmdVar.set("Ready...")
		self.cmdQueued = False;
		self.robot = Robot.Robot()

	def newCommand(self, name):
		if self.cmdQueued:
			self.addCommand()
		self.selectedCommand = name;
		self.enteredParam = ''
		self.cmdVar.set(self.selectedCommand)
		self.cmdQueued = True

	def updateParam(self, param):
		self.enteredParam = self.enteredParam + param
		self.cmdVar.set(self.selectedCommand + '(' + self.enteredParam + ')')

	def addCommand(self):
		print ('Add Command')
		command = Command.Command(name=self.selectedCommand, param1=self.enteredParam)
		self.cmdList.append(command)
		self.cmdQueued = False

	def clear(self):
		print ('Clear Commands')
		while (len(self.cmdList) > 0):
			print ('Remove Command')
			del self.cmdList[0]
		self.cmdQueued = False
		self.cmdVar.set('Ready...')
		
	def clearLast(self):
		if len(self.cmdList) > 0:
			self.cmdList.pop()
			self.cmdVar.set('Ready...')
		else:
			self.cmdVar.set('No More Commands')

	def execute(self):
		if self.cmdQueued:
			self.addCommand()
		self.cmdVar.set("Execute...")
		for command in self.cmdList:
			self.robot.execute(command) 
		self.cmdVar.set("Ready...")