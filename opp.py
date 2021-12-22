

class Computer :
	def __init__(self,cpu,ram):
		self.cpu = cpu
		self.ram = ram

	def config(self):
		print("this is config" + self.cpu + self.ram)

com1 = Computer('3i',"128")
com1.config()