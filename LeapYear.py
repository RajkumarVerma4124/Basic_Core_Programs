class Leapyear:
	# instance attributes or variables	
	def __init__(self):
		self.year = int(input("Enter a year to check if its leap year or not : "))
	
	# instance methods (behaviours)
	def checkYearLength(self):
		if (self.year < 1000) :
			print("Enter The Four Digit Year ")
			exit()
		
	def checkLeapOrNot(self):
		if (self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0):
			print("It is a leap year")
		else:
			print("it is not a leap year")

# creating objects of class Leapyear
yearObj = Leapyear()
yearObj.checkYearLength()
yearObj.checkLeapOrNot()

