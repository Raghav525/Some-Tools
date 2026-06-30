alphabets = {
        "a": "q",
        "A": "Q",
        "b": "w",
        "B": "W",
        "c": "e",
        "C": "E",
        "d": "r",
        "D": "R",
        "e": "t",
        "E": "T",
        "f": "y",
        "F": "Y",
        "g": "u",
        "G": "U",
        "h": "i",
        "H": "I",
        "i": "o",
        "I": "O",
        "j": "p",
        "J": "P",
        "k": "L",
        "K": "l",
        "l": "K",
        "L": "k",
        "m": "J",
        "M": "j",
        "n": "H",
        "N": "h",
        "o": "g",
        "O": "G",
        "p": "F",
        "P": "f",
        "q": "d",
        "Q": "D",
        "r": "a",
        "R": "A",
        "s": "S",
        "S": "s",
        "t": "Z",
        "T": "z",
        "u": "X",
        "U": "x",
        "v": "C",
        "V": "c",
        "w": "V",
        "W": "v",
        "x": "M",
        "X": "m",
        "y": "b",
        "Y": "n",
        "z": "B",
        "Z": "N"
    }

def add_3(message):
    new_message = ""
    for char in message:
        if char in alphabets:
            new_message += alphabets[char]
            
        elif char == "_":
            new_message += "_"
            
        else:
            new_message += char
    return new_message

def block_reverse(message):
    blocks = [message[i:i+3] for i in range(0, len(message), 3)]
    
    new_message = ""
    for block in blocks:
        new_message += f"{block[::-1]}#"
        
    return new_message

def converter(message):
    message = message.replace(" ", "_")
    
    message = add_3(message)
    
    message = block_reverse(message)

    message = message.replace(" ", "#")

    return message

def de_block_reverse(message):
    blocks = message.split("#")
    
    new_message = ""
    for block in blocks:
        new_message += block[::-1]
    return new_message

def minus_3(message):
    new_message = ""
    for char in message:
        if char in alphabets:
            for key, value in alphabets.items():
                if value == char:
                    new_message += key
            
        elif char == "_":
            new_message += "_"
            
        else:
            new_message += char
            
    return new_message

def deconverter(message):

    message = message.replace("#", " ")

    message = de_block_reverse(message)

    message = minus_3(message)

    message = message.replace("_", " ")

    return message

def main(): 
    while True:
        print("\nWelcome to the Code Converter!")
        print("Ktv#Jge#Z_t#Z_g#_ti#rge#e_t#CHg#Zat#!at#")
        print("Options:")
        print("1. Convert into code language")
        print("2. Deconvert into English")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice in ["1", "coverter", "convert", "c", "convertintocode", "convertintocodelanguage"]:
            message = input("Enter the message: ")
            print(f"Message in code language: {converter(message)}")

        elif choice in ["2", "deconverter", "deconvert", "d", "deconvertintoenglish", "coverterintoenglish"]:
            message = input("Enter the message: ")
            print(f"Message in English: {deconverter(message)}")
            
        elif choice in ["exit", "3", "back"]:
            print("Logging out...")
            print("rrJ#beg#!h#")
            break
            
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
