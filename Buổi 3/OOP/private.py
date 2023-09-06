
class Geek:
	def __init__(self, name, roll, branch):
		self.__name = name
	def __displayDetails(self):
		print("Name: ", self.__name)
	
	def accessPrivateFunction(self):
		self.__displayDetails()

# creating object
obj = Geek("R2J", 1706256, "Information Technology")


obj.accessPrivateFunction()
print(obj.__name)