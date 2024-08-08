# day 2 - modified 
# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber
        
    def Addition(self):
        return self.firstNumber + self.secondNumber
    
    def Subtraction(self):
        return self.firstNumber - self.secondNumber
    
    def Multiplication(self):
        return self.firstNumber * self.secondNumber
    
    def Division(self):
        try:
            return self.firstNumber / self.secondNumber
        except ZeroDivisionError:
            print("ZeroDivisionError: Second number can't be Zero in division")
            return None
        
def operatorSelect(calcu : Calculator) -> None:
    while True:
        try:
            print("\n*****What Operation do you want to execute?*****")
            print("1. Addition, 2. Subtraction, 3. Multiplication, 4. Division\n")
            operator = int(input("Select: "))

            if operator == 1:
                print(f"Answer: {calcu.Addition()}")
                break
            elif operator == 2:
                print(f"Answer: {calcu.Subtraction()}")
                break
            elif operator == 3:
                print(f"Answer: {calcu.Multiplication()}")
                break
            elif operator == 4:
                result = calcu.Division()
                if result is not None:
                    print(f"Answer: {result}")
                break
            else:
                print("\n *****Invalid Input, Select from 1 to 4 only*****\n")
        except ValueError:
            print("\nValueError -> Invalid input, input should be a number only\n")  

def convert_to_Number(prompt: str) -> float:
    while(True):
        try:
            value = input(prompt)
            if value.strip() == "":
                print("\nInput cannot be blank. Please enter a valid number.")
                print("*** TRY AGAIN ***\n")
                continue
            return float(value)
        except ValueError:
            print(f"\n ValueError -> Invalid input: '{value}' is not a Number")
            print("*** TRY AGAIN ***\n")
            
def main():
    while(True):
        # Input Section
        firstNumber = convert_to_Number("Input first number: ")
        secondNumber = convert_to_Number("Input second number: ")

        # part where the numbers from input will be passed in the Object "Calculator"
        calcu = Calculator(firstNumber, secondNumber) 
        # pass the Number values to select an Operator
        operatorSelect(calcu)
        
        
        decide = str(input(f"Do you want to solve another arithmetic problem? (Yes/No): ")).strip().lower()
        if decide != "yes":
            break

#runs the main method which is the # Input Section
if __name__ == "__main__":  
    main()
