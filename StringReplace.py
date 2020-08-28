class Stringreplace:
	# instance attributes or variables
	def __init__(self,name):
		self.name = name
		self.stringTemp = "Hello UserName, How are you?"
	# instance methods (behaviours)
	def replaceStr(self):
		if len(self.name) < 3 :
			print("The Name Should be More Than Three Characters")
		else :
			outputStr = self.stringTemp.replace("UserName", self.name)
			print ("Before Replacing String is : ", self.stringTemp)
			print ("After Replacing String is : ", outputStr)

print("Welcome to the string replace program\n")
#taking input from user
nameString = input("Enter You Name : ")

# creating objects of class StringReplace
userNameObj = Stringreplace(nameString)
userNameObj.replaceStr()

