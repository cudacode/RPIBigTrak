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