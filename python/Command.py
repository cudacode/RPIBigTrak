class Command:
	'Common base class for all commands'

	def __init__ (self, name, param1):
		self.name = name
		self.param1 = param1

	def update (self, updatePrm):
		self.param1 = updatePrm