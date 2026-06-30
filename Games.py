import random
from My_language import converter
import os
import datetime 

def RPS_history(message):
    file = "Text Files/RPS_History.txt"
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(file) == False:
        with open(file, "w") as f:
            f.write(f"{message} -- {date}\n")
    
    elif os.path.exists(file) == True:
        with open(file, "a") as f:
            f.write(f"{message} -- {date}\n")

def RPS():
    pwd = converter(input("Enter the password to play this game: "))
    
    if pwd == "ytr#Fa_#S#":
        comp_win = 0
        player_win = 0
        rps = ["rock", "paper", "scissors"]

        choices = {
            "rock": "rock",
            "r": "rock",
            "1": "rock",
            "paper": "paper",
            "p": "paper",
            "2": "paper",
            "scissors": "scissors",
            "s": "scissors",
            "3": "scissors"
        }

        try:
            x = int(input("How many matches to play: "))
        except ValueError:
            print("Enter a valid amount of matches")
            exit()

        while comp_win < x and player_win < x:
            comp = random.choice(rps)
            person_input = input("Choose Rock, Paper or Scissors: ").lower()

            if person_input not in choices:
                print("Invalid choice")
                continue

            person = choices[person_input]

            print("Computer chose:", comp)

            if comp == person:
                print("It's a tie!")

            elif (comp == "rock" and person == "paper") or \
                (comp == "paper" and person == "scissors") or \
                (comp == "scissors" and person == "rock"):
                player_win += 1
                print("You win this round!")

            else:
                comp_win += 1
                print("Computer wins this round!")

            print("Computer score:", comp_win)
            print("Your score:", player_win)
            print("-" * 20)

        if comp_win > player_win:
            print("Computer Wins the Game!")
            RPS_history(f"Computer wins this game with a score of {comp_win} to {player_win}")
        else:
            print("You Win the Game!")
            RPS_history(f"Player wins this game with a score of {player_win} to {comp_win}")
    else:
        print("Incorrect password. Access denied.")

def get_number():
        while True:
            try:
                return int(input("Enter a number to guess: "))
            except ValueError:
                print("Invalid input. Please enter a number.")

def Guess_history(message):
    file = "Text Files/Guess_History.txt"
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(file) == False:
        with open(file, "w") as f:
            f.write(f"{message} -- {date}\n")
    
    elif os.path.exists(file) == True:
        with open(file, "a") as f:
            f.write(f"{message} -- {date}\n")

def Guess():
    pwd = converter(input("Enter the password to play this game: "))
    
    if pwd == "tXu#SS#":
        mode = input("Enter the difficulty level of the game(easy, medium, hard or custom): ").strip().lower()
        number = 1
        
        if mode in ["easy", "1", "e"]:   
            num_find = random.randint(1, 100)

            while True:
                guess = get_number()

                if guess > num_find:
                    if guess - num_find >= 20:
                        print("Too high!!")
                        number += 1
                        
                    else:
                        print("High!")
                        number += 1
                        
                elif guess < num_find:
                    if num_find - guess >= 20:
                        print("Too low!!")
                        number += 1
                        
                    else:
                        print("Low!")
                        number += 1

                else:
                    Guess_history(f"Player found the correct number, {num_find}, in {number} guesses in easy difficulty")
                    print(f"You found the correct number!!!! in {number} guesses")
                    break
        
        if mode in ["medium", "2", "m", "mid", "med"]:   
            num_find = random.randint(1, 250)

            while True:
                guess = get_number()

                if guess > num_find:
                    if guess - num_find >= 30:
                        print("Too high!!")
                        number += 1
                        
                    else:
                        print("High!")
                        number += 1
                        
                elif guess < num_find:
                    if num_find - guess >= 30:
                        print("Too low!!")
                        number += 1
                        
                    else:
                        print("Low!")
                        number += 1

                else:
                    Guess_history(f"Player found the correct number, {num_find}, in {number} guesses in medium difficulty")
                    print(f"You found the correct number!!!! in {number} guesses")
                    break
        
        if mode in ["hard", "3", "h"]:   
            num_find = random.randint(1, 500)

            while True:
                guess = get_number()

                if guess > num_find:
                    if guess - num_find >= 50:
                        print("Too high!!")
                        number += 1
                        
                    else:
                        print("High!")
                        number += 1
                        
                elif guess < num_find:
                    if num_find - guess >= 50:
                        print("Too low!!")
                        number += 1
                        
                    else:
                        print("Low!")
                        number += 1

                else:
                    Guess_history(f"Player found the correct number, {num_find}, in {number} guesses in hard difficulty")
                    print(f"You found the correct number!!!! in {number} guesses")
                    break
        
        if mode in ["custom", "4", "c",]:
            try: 
                l = int(input("Enter the lower limit: "))
                try:
                    u = int(input("Enter the upper limit: "))
                except ValueError:
                    print("Enter a valid integer value.")
            except ValueError:
                print("Enter a valid integer value.")
            
            num_find = random.randint(l, u)

            too = int((u - l) / 3)
            
            while True:
                guess = get_number()

                if guess > num_find:
                    if guess - num_find >= too:
                        print("Too high!!")
                        number += 1
                        
                    else:
                        print("High!")
                        number += 1
                        
                elif guess < num_find:
                    if num_find - guess >= too:
                        print("Too low!!")
                        number += 1
                        
                    else:
                        print("Low!")
                        number += 1

                else:
                    Guess_history(f"Player found the correct number, {num_find}, in {number} guesses in custom difficulty with lower limit {l} and upper limit {u}")
                    print(f"You found the correct number!!!! in {number} guesses")
                    break
    
    else:
        print("Incorrect password. Access denied.")
