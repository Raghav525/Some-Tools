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
