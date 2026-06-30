from datetime import datetime
import math
import os
from My_language import converter

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")

def history(message):
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%Y-%m-%d")
        
    if os.path.exists("Text Files/calc_history.txt"):
        with open("Text Files/calc_history.txt", "r") as f:
            data = f.read()
    
    else:
        data = ""
        
    with open("Text Files/calc_history.txt", "a") as f:
        if date not in data:
            f.write(f"\n===={date}====\n")
            
        f.write(f"\n{message} --- {time}\n")
 
def add(a, b):
    ans = a + b
    return ans

def addition():
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    
    result = add(a, b)
    
    history(f"{a} + {b} = {result}")

    if result > 10000000:
        while True:
            choice = input("Do you REALLY REALLY wanna continue man:(yes/ no)").lower()
            if choice in ["yes", "y"]:
                print(" ")
            elif choice in ["no", "n"]:
                print("THAT'S MA BOY.")
                print(result)
                break
            else:
                print("BRUH WHAT THE HELL YOU WRITING HUH")

    else:
        print(result)
    
def sub(a, b):
    return a - b

def subtract():
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    
    result = sub(a, b)
    
    history(f"{a} - {b} = {result}")

    print(result)

def mul(a, b):
    return a * b

def multiply():
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    
    result = mul(a, b)
    
    history(f"{a} x {b} = {result}")
    
    try:
        print(result)
    
    except OverflowError:
        print("The number generated was too large.")
        return None

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You cannot divide by zero.")
        return None

def divide():
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    
    result = div(a, b)
    
    history(f"{a} / {b} = {result}")

    print(result)

def sq(a):
    try:
        return a ** 2
    except OverflowError:
        print("The number generated was too large.")
        return None

def square():
    a = get_number("Enter the number: ")
    
    result = sq(a)
    
    history(f"{a} squared = {result}")
    
    print(result)

def sq_rt(a):
    if a >= 0:
        return a ** 0.5
    else:
        print("Cannot compute square root of a negative number.")
        return None

def square_root():
    a = get_number("Enter the number: ")
    
    result = sq_rt(a)
    
    history(f"Square root of {a} = {result}")
    
    print(result)

def exp(a, b):
    try:
        return a ** b
    except OverflowError:
        print("The number generated was too large.")
        return None

def exponentiation():
    a = get_number("Enter base: ")
    b = get_number("Enter exponent: ")
    
    result = exp(a, b)
    
    history(f"{a} ^ {b} = {result}")
    
    print(result)

def get_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def factorial():
    n = get_int("Enter a number: ")
    history(f"Factorial of {n} = {math.factorial(n)}")
    
    try:
        print(math.factorial(n))
    
    except OverflowError:
        print("Output is too large.")
        return None

def a_p(a, d, n):
    try:
        return (n / 2) * (2 * a + (n - 1) * d)
    except OverflowError:
        print("The number generated was too large.")
        return None

def ap():
    a = get_number("Enter the first term: ")
    d = get_number("Enter the common difference: ")
    n = get_int("Enter the number of terms: ")
    
    result = a_p(a, d, n)
    
    message = f"AP with first term {a}, common difference {d} and number of terms {n} has sum = {result}"
    history(message)
    
    print(result)

def is_prime(a):
    try:
        a = int(a)
    except ValueError:
        return ("Enter a positive integer")

    if a < 2:
        return ("Not a prime number")

    x = int(a ** 0.5)
    p = True

    for i in range(2, x + 1):
        if a % i == 0:
            p = False
    
    if p:
        return ("Prime.")
    else:
        return ("Composite.")

def prime_check():
    a = get_int("Enter a number: ")
    
    result = is_prime(a)
    
    history(f"Prime check for {a} = {result}")
    
    print(result)

def view_history():
    with open("Text Files/calc_history.txt", "r") as f:
        data = f.read()
        print("Calculation History:")
        print(data)

def clear_history():
    with open("Text Files/calc_history.txt", "w") as f:
        f.write("")
    print("History cleared.")

def calculator():
    while True:
        Pass = converter(input("What is the password? "))
        if Pass == "Kqe#KXe#gZq#a#":
            while True:
                print("\nAvailable operations:")
                print("1. addition")
                print("2. subtraction")
                print("3. multiplication")
                print("4. division")
                print("5. square")
                print("6. square root")
                print("7. exponentiation")
                print("8. factorial")
                print("9. AP(arithmetic progression)")
                print("10. Prime checker")
                print("11. view history")
                print("12. clear history")
                print("13. back")

                choices = {
                    "addition": addition,
                    "1": addition,
                    "+": addition,
                    "add": addition,
                    "subtraction": subtract,
                    "2": subtract,
                    "-": subtract,
                    "subract": subtract,
                    "multiplication": multiply,
                    "3": multiply,
                    "x": multiply,
                    "multiply": multiply,
                    "*": multiply,
                    "division": divide,
                    "4": divide,
                    "/": divide,
                    "divide": divide,
                    "square": square,
                    "5": square,
                    "square root": square_root,
                    "sq root": square_root,
                    "sq rt": square_root,
                    "6": square_root,
                    "exponentiation": exponentiation,
                    "**": exponentiation,
                    "^": exponentiation,
                    "7": exponentiation,
                    "factorial": factorial,
                    "8": factorial,
                    "!": factorial,
                    "ap": ap,
                    "arithmetic progression": ap,
                    "9": ap, 
                    "prime checker": prime_check,
                    "prime check": prime_check,
                    "prime": prime_check,
                    "10": prime_check,
                    "view history": view_history,
                    "history": view_history,
                    "view": view_history,
                    "11": view_history,
                    "clear history": clear_history,
                    "12": clear_history,
                    "clear": clear_history
                }
                
                choice = input("Choose an operation: ").lower()

                if choice in choices:
                    choices[choice]()

                elif choice in ["exit", "13", "back"]:
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice.")
            
        elif Pass in ["oMt#Z#", "oMT#Z#"]:
            break
        
        else:
            print("Incorrect password.")
            
if __name__ == "__main__":
    calculator()


def factorise(a):
    factors = []
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            factors.append(i)
        
    for i in factors:
        return i, factors
  
def factorise_ui():
    a = get_int("Enter a number: ")
    factors = factorise(a)
  
