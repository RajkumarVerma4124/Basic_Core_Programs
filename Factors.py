class Factors:
    # instance attributes	
    def __init__(self, factors):
        self.factors = factors

    # instance methods (behaviours)
    def getFactValue(self, i=2):
        while i <= self.factors / i:
            print("i = ", i, " factors = ", self.factors)

            while self.factors % i == 0:
                self.factors = self.factors / i
                print("Factors is : ", int(i))
            i = i + 1

        if self.factors > 1:
            print("Factors is : ", int(self.factors))

#taking user input from  the user
factNumber = float(input("Enter a number to get the factorial : "))

# creating objects of class factors
factObj = Factors(factNumber)
factObj.getFactValue()

