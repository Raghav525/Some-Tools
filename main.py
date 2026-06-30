from Math_Tools import calculator
from Pwd_Tools import Pwd_generate, Pwd_check
from Games import Guess, RPS
from File_Editor import File_Editor
from Budget_storage import menu as budget_menu
from My_language import converter, main as My_laguage

def main():
    while True:
        Pass = input("What is the password? ")
        Pass = converter(Pass)
        
        if Pass == "HtJ#X#":
            while True:
                print("\nSelect a tool:")
                print("1. Calculator")
                print("2. Password Generator")
                print("3. Password Checker")
                print("4. Guessing Game")
                print("5. Rock, Paper, Scissors")
                print("6. File Editor")
                print("7. Budget Manager")
                print("8. Code Converter")
                print("9. Exit")

                menu = {
                    "1": calculator,
                    "calculator": calculator,
                    "calc": calculator,
                    "2": Pwd_generate,
                    "passwordgenerator": Pwd_generate,
                    "3": Pwd_check,
                    "passwordchecker": Pwd_check,
                    "4": Guess,
                    "guessinggame": Guess,
                    "5": RPS,
                    "rockpaperscissors": RPS,
                    "rps": RPS,
                    "6": File_Editor,
                    "file editor": File_Editor,
                    "7": budget_menu,
                    "budgetmanager": budget_menu,
                    "budget": budget_menu,
                    "8": My_laguage,
                    "codeconverter": My_laguage,
                    "code": My_laguage,
                    "coder": My_laguage
                }

                choice = input("Enter the number of your choice: ").strip().lower()

                if choice in menu:
                    menu[choice]()
                    
                elif choice in ["exit", "9"]:
                    print("Exiting the program.")
                    break
                
                else:
                    print("Invalid choice.")
                
        elif Pass in ["oMt#Z#", "oMT#Z#"]:
            break  
        
        else:
            print("INCORRECT PASSWORD. TRY AGAIN.")

if __name__ == "__main__":
    main()
