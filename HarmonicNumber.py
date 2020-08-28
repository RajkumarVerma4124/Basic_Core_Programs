class Harmonicnumber:
	# instance attributes
	def __init__(self,numRange):
		self.num = 0.0
		self.numRange = numRange
	
	# instance methods (behaviours)
	def getHarmonicValue(self):
		if(self.numRange != 0):
			for i in range(1,self.numRange + 1):
				self.num = self.num + (1/i)
		else:
			print("Enter a positive number")
		sum = round(self.num,2)
		print("The Nth Harmonic Value : ", sum)

#taking input from the user
numRange = int(input("Enter a range for harmonic number : "))

#creating objects of class Harmonicnumber
numberObj = Harmonicnumber(numRange)
numberObj.getHarmonicValue()

