from My_language import converter, deconverter
import os

def Pwd_generate():
    import random

    def generate_password(length):
        Char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        Num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        Sym = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?"]
        password = ""
        for _ in range(length):
            password += random.choice(Char + Num + Sym)
        return password

    while True:
            length = input("Enter the length of the password(or exit): ")
            try:
                len = int(length)
                if len < 1:
                    print("Please enter a positive integer for the password length.")
                    continue
                else:
                    print("Generated password:", generate_password(len))
                
            except ValueError:
                if length.lower() == "exit":
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid input. Please enter a valid integer or 'exit'.")
                    continue

def Pwd_check():
    def check_password(password):

        length = len(password)

        digits = 0
        lower = 0
        upper = 0
        special = 0
        counts = {}

        for char in password:

            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1


            if char.isdigit():
                digits += 1

            elif char.islower():
                lower += 1

            elif char.isupper():
                upper += 1

            elif not char.isalnum():
                special += 1
            
    
        score = 0

        if length >= 8:
            score += 1

        if digits > 0:
            score += 1

        if lower > 0:
            score += 1

        if upper > 0:
            score += 1

        if special > 0:
            score += 1

        for count in counts.values():
            if count > 3:
                score -= 1
                break

        print("Length:", length)
        print("Digits:", digits)
        print("Lowercase letters:", lower)
        print("Uppercase letters:", upper)
        print("Special characters:", special)
        print("Character repetition:")
        for char, count in counts.items():
            print(char, "→", count)
        print("Score: ", score)

        if score <= 2:
            print("Strength: Weak")

        elif score <= 4:
            print("Strength: Moderate")

        else:
            print("Strength: Strong")
        

    while True:
        pwd = input("Enter password (or type exit): ")

        if pwd.lower() == "exit":
            break

        check_password(pwd)

def Pwd_view():
    if os.path.exists("Passwords.txt"):
        with open("Passwords.txt", "r") as f:
            passwords = f.readlines()
            passkeys = {}
            for pwd in passwords:
                try:
                    Pwd = deconverter(pwd.strip().split("--")[1])
                    key = pwd.strip().split("--")[0].strip()
                    passkeys[key] = Pwd

                except IndexError:
                    pass
        
        
        View = input("Which password do you want to view? (Enter the key): ")
        
        try:
            print("Password:", passkeys[View])
        except KeyError:
            print("No password found for the given key.")
            
    else:
        with open("Passwords.txt", "w") as f:
            pass
        print("No stored passwords found.")

def Pwd_add():
    key = input("Enter a key for the password: ")
    password = converter(input("Enter the password: "))
    if os.path.exists("Passwords.txt"):
        with open("Passwords.txt", "a") as f:
            f.write(f"{key} -- {password}\n")
            print("Password added successfully.")
    
    else:
        with open("Passwords.txt", "w") as f:
            f.write(f"{key} -- {password}\n")
            print("Password added successfully.")

def Pwd_ALL():
    while True:
        pwd = input("Enter the password to access the Password VAULT: ")
        if converter(pwd) == "HtZ#_qS#HqB#Ztu#XS#":
            while True:
                choice = input("What do you want to do? (add/view): ").strip().lower()
                
                if choice in ["view", "v", "2", "viewpassword", "viewpwd", "passwordview", "pwdview"]:
                    Pwd_view()
                
                elif choice in ["add", "a", "1", "store", "passwordadd", "addpassword", "addpwd", "pwdadd", "storepassword", "storepwd", "addpass", "passadd"]:
                    Pwd_add()
                
                elif choice in ["exit", "e", "3", "quit", "q"]:
                    print("Exiting the Password vault.")
                    break
                
                else:
                    print("Invalid choice. Please choose 'add', 'view', or 'exit'.")
        
        elif choice in ["exit", "e", "3", "quit", "q"]:
            print("Exiting the Password vault.")
            break
        
        else:
            print("Incorrect password. Access denied.")
      