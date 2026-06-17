class Calculator:

    def add(self,a,b):
        return a + b
    

    def subtract(self,a,b):
        return a - b
    

    def multiply(self,a,b):
        return a * b
    

    def divide(self,a,b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    

    def square(self, a):
        return a ** 2
    

    def cube(self, a):
        return a ** 3
    

    def sqrt(self, a):
        if a < 0:
            return "Square Root of negative number is not possible"
        return a ** 0.5
    

    def power(self, a, b):
        return a ** b
     

    def factorial(self, a):
        if a < 0:
            return "Factorial of negative numbers is n ot possible"

        fact = 1
        for i in range(1, int(a)+1):
            fact *= i
        return fact
    

    def is_prime(self, a):
        
        if a < 2:
            return False
        
        for i in range(2, int(a)):
            if a % i == 0:
                return False
            
        return True


calc = Calculator()

print("           SCIENTIFIC  CALCULATOR        ")

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Sqaure")
    print("6. Cube")
    print("7. SquareRoot")
    print("8. Power")
    print("9. Factorial")
    print("10. Prime Number")
    print("11. Exit")

    try:
       choice = int(input("Enter your choice : "))
    except ValueError:
       print("Please enter a valid choice!")
       continue

    if choice == 11:
       print("GOODBYEEE!!!!")
       break

    try:
        if choice in [1, 2, 3, 4, 8]:
            a = float(input("Enter First Number : "))
            b = float(input("Enter Second Number : "))
        else:
            a = float(input("Enter Number : "))
    except ValueError:
        print("Please enter valid numbers!")
        continue



    if choice == 1:
        print("Result : ", calc.add(a,b))

    elif choice == 2:
        print("Result : ", calc.subtract(a,b))

    elif choice == 3:
        print("Result : ", calc.multiply(a,b))

    elif choice == 4:
        print("Result : ", calc.divide(a,b))

    elif choice == 5:
        print("Result : ", calc.square(a))

    elif choice == 6:
        print("Result : ", calc.cube(a))

    elif choice == 7:
        print("Result : ", calc.sqrt(a))

    elif choice == 8:
        print("Result : ", calc.power(a,b))

    elif choice == 9:
        print("Result : ", calc.factorial(a))

    elif choice == 10:
        if calc.is_prime(a):
            print(a, "is a Prime Number")
        else:
            print(a, "is not a Prime Number")


    else:
        print("Invalid Choice..!!!")
