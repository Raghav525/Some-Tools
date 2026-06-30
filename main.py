from Math_Tools import calculator
from Pwd_Tools import Pwd_generate
from Games import Guess, RPS
from File_Editor import File_Editor
from Budget_storage import menu as budget_menu
from My_language import main as My_laguage

def main():
        while True:
            print("\nSelect a tool:")
            print("1. Calculator")
            print("2. Password Generator")
            print("3. Guessing Game")
            print("4. Rock, Paper, Scissors")
            print("5. File Editor")
            print("6. Budget Manager")
            print("7. Code Converter")
            print("8. Exit")

            menu = {
                "1": calculator,
                "calculator": calculator,
                "calc": calculator,
                "2": Pwd_generate,
                "passwordgenerator": Pwd_generate,
                "3": Guess,
                "guessinggame": Guess,
                "4": RPS,
                "rockpaperscissors": RPS,
                "rps": RPS,
                "5": File_Editor,
                "file editor": File_Editor,
                "6": budget_menu,
                "budgetmanager": budget_menu,
                "budget": budget_menu,
                "7": My_laguage,
                "codeconverter": My_laguage,
                "code": My_laguage,
                "coder": My_laguage
            }

            choice = input("Enter the number of your choice: ").strip().lower()

            if choice in menu:
                menu[choice]()
                
            elif choice in ["exit", "8"]:
                print("Exiting the program.")
                break
            
            else:
                print("Invalid choice.")
                

if __name__ == "__main__":
    main()
