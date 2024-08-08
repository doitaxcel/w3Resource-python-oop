# day 1 - modified
# Write a Python program to create a person class. Include attributes like name, 
# country and date of birth. Implement a method to determine the person's age.

class Person:
    def __init__(self, name, country, birthYear, currentYear) -> None:
        self.name = name
        self.country = country
        self.birthYear = birthYear
        self.currentYear = currentYear
    
    #info Method
    def Age(self):
        return  self.currentYear - self.birthYear
    # wholeInfo Method
    def wholeInfo(self):
        return f"name is: '{self.name}' from: '{self.country}' and '{self.Age()}' years old"
        
# Attribute Inputs
name = str(input("Input name: "))
country = str(input("Input country: "))

print("******WARNING*****")
print("MAKE SURE THE INPUT YEARS ARE CORRECT")
birthYear = int(input("Input BirthYear: "))
currentYear = int(input("Input CurrentYear: "))

# inputs info that will be read to the object Person (class)
inputs = Person(name, country, birthYear, currentYear)

# access the Object and its one method to identify the Age
age = inputs.Age()
# access the Object and its one method to identify the Infos
wholeInfo = inputs.wholeInfo()

while(True):
    try:
        print("What do you want to print? 1: Whole Info, 2: Age")
        choose = int(input("Select: "))

        if choose == 1:
            print(wholeInfo)
            break
        elif choose == 2:
            if age == 1:
                print(f"{age} year old")
                break
            else:
                print(f"{age} Years Old")
                break
        else:
            print("\n-----Invalid Input, input only '1' and '2'-----")
            print("             ***TRY AGAIN*** \n")
    
    except(ValueError):
        print("Invalid Input, input numbers only")




        

        
    
