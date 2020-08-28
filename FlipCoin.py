import random 

#array 
arr = []

class Flipcoin:
	# instance attributes or variables
	def __init__(self,flipCount):
		self.flipCount = flipCount
		self.num = 0.5
		self.headSum = 0
		self.tailSum = 0

	# instance methods (behaviours)
	def randomFlips(self):
		if self.flipCount < 0:
			print("Enter The Positive Number \n")
			self.randomFlips()
		else:
			for i in range (self.flipCount):
				randomNumber = random.random()
				randomFloat = round(randomNumber,1)
				arr.append(randomFloat)
				print("The Random Value is :", randomFloat) 
		print("The Random Value ",arr,"\n")

	def flipsPercent(self):
		for i in range (self.flipCount):
			if arr[i] > self.num:
				print("Heads")
				self.headSum = self.headSum + 1
			else:
				print("Tails")
				self.tailSum = self.tailSum + 1

		headPercent = int(self.headSum / self.flipCount * 100)
		tailPercent = int(self.tailSum / self.flipCount * 100)
		print("\nPercentage of Heads : ",headPercent)
		print("\nPercentage of Tails : ",tailPercent)
	
#taking the input from user
flipCount = int(input("Enter The No. Of Time You Want To Flip The Coin : "))

# creating objects of class Flipcoin
flipObj = Flipcoin(flipCount)
flipObj.randomFlips()
flipObj.flipsPercent()

