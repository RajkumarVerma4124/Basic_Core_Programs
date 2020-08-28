class Poweroftwo:
	# instance attributes
	def __init__(self, num):
		self.num = num
	
	# instance methods (behaviours)
	def powerOfValue(self): 		       
		if self.num <= 0 or self.num > 30:
			print ("Enter a value between 1 to 31")
		else:
			for i in range(1,self.num+1):
				power = int(pow(2,i))
				print("Table of 2 ^",i ," is :", power)

#taking input from user
getExponent = int(input("Enter a exponential number to get the power : "))

# creating objects of class Poweroftwo
powOfNumObj = Poweroftwo(getExponent)
powOfNumObj.powerOfValue()

