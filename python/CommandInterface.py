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
import CommandModel

class CommandInterface:
	'Command User Interface Methods'

	def __init__ (self, cmdBtns, cntBtns, cmdModel):
		self.cmdBtns = cmdBtns
		self.cntBtns = cntBtns
		self.cmdModel = cmdModel
		self.mode = 'open'

	def enableBtns(self, btnArray):
		for btn in btnArray:
			btn['state'] = Tkinter.NORMAL

	def disableBtns(self, btnArray):
		for btn in btnArray:
			btn['state'] = Tkinter.DISABLED

	def commandMode(self):
		print ('Command Mode')
		self.mode = 'command'
		self.enableBtns(self.cmdBtns)
		self.disableBtns(self.cntBtns)

	def countMode(self):
		print ('Count Mode')
		self.mode = 'count'
		self.enableBtns(self.cntBtns)
		self.disableBtns(self.cmdBtns)

	def openMode(self):
		print ('Open Mode')
		self.mode = 'open'
		self.enableBtns(self.cntBtns)
		self.enableBtns(self.cmdBtns)

	# The mode reflects the input we are looking for command | count | open (command or number)
	def getMode(self):
		return self.mode

	def isOpenMode(self):
		if self.mode == 'open':
			return True
		else:
			return False

#	def updateCmdVar(command):
#		cmdVar.set(command.name)

	def clrCallBack(self):
		print ('Clear Command')
		self.cmdModel.clear()
		self.commandMode()
		

	def clsCallBack(self):
		print ('Clear Last Command')
		self.cmdModel.clearLast()
		self.commandMode()

	def fireCallBack(self):
		print ('Fire Command')
		self.countMode()
		self.cmdModel.newCommand('fire')

	def goCallBack(self):
		print ('Go Command')
		self.cmdModel.execute()
		self.commandMode()

	def fwdCallBack(self):
		print ('Forward Command')
		self.countMode()
		self.cmdModel.newCommand('fwd')

	def backCallBack(self):
		print ('Back Command')
		self.countMode()
		self.cmdModel.newCommand('back')

	def leftCallBack(self):
		print ('Left Command')
		self.countMode()
		self.cmdModel.newCommand('left')

	def rightCallBack(self):
		print ('Right Command')
		self.countMode()
		self.cmdModel.newCommand('right')

	def holdCallBack(self):
		print ('Hold Command')
		self.countMode()
		self.cmdModel.newCommand('hold')

	def numCallBack(self, num):
		print ('Num Button', num)
		self.cmdModel.updateParam(num)
		if self.isOpenMode():
			self.commandMode()
		else:
			self.openMode()

