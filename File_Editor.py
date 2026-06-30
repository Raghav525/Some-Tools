import os
from datetime import datetime
import shutil
from My_language import converter

def History(message):
    with open("Text Files/File_History.txt", "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{message} on {time}\n\n")

def File_delete(): 
    files = [] 

    try:
        n = int(input("Enter the number of files to delete: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    while n > 0:
        a = input("Enter the name of the file to delete: ")
        files.append(a)
        n -= 1

    def delete(): 
        for file in files:
            if os.path.exists(file):
                os.remove(file)
                History(f"{file} deleted")
            else:
                print(file, "not found")

    delete()

def File_create():
    try:
        n = int(input("Enter the number of files to create: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    while n > 0:
        a = input("Enter the name of the file to create: ")
        with open(a, "w") as f:
            pass
        print(a, "created")
        n -= 1
        History(f"{a} created")

def File_view():
    a = input("Enter the name of the file to view: ")
    if os.path.exists(a):
        with open(a, "r") as f:
            content = f.read()
            print("Content of", a, ":")
            print(content)
            History(f"{a} viewed")

    else:
        print(a, "not found")
        return

def File_Copy():
    org_file = input("Enter the original file name: ")
    
    if os.path.exists(org_file):
        
        dest = input("Enter the path to copy the file to: ")
        
        if os.path.exists(dest):
            copy_name = input("Enter the name for the copied file: ")
            
            if os.path.exists(copy_name) != True:
                shutil.copy(org_file, os.path.join(dest, copy_name))
                History(f"{org_file} copied to {dest} as {copy_name}")
                print("File copied to", dest)
                
            else:
                print(copy_name, "already exists. Please choose a different name.")
                return
            
        else:
            print(dest, "not found")
            return
        
    else:
        print(org_file, "not found")
        return

def Word_Find_one_file():
    file = input("Enter file path: ")
    if os.path.exists(file):
        word = input("Enter the word to find: ")
        with open(file, "r") as f:
            content = f.read()
            word_lines = []
            if word in content:
                lines = f.readlines()
                for i in range(len(lines)):
                    if word == lines[i]:
                        word_lines.append(i + 1)
                print(f" {word} found in {file} at line(s): {', '.join(map(str, word_lines))}")
            
            else:
                print(f"'{word}' not found in '{file}'")
                return
    
    else:
        print("File not found")
        return                  

def Word_replace():
    file = input("Enter the file name: ")
    
    if os.path.exists(file):
        with open(file, "r") as f:
            data = f.read()
            print("Original data:")
            print(data)

        old_word = input("Enter the word to be replaced: ")
        new_word = input("Enter the new word: ")

        modified_data = data.replace(old_word, new_word)

        with open(file, "w") as f:
            f.write(modified_data)

        print(f"'{old_word}' has been replaced with '{new_word}' in '{file}'")
        
        History(f"{old_word} replaced with {new_word} in {file}")

    else:
        print(file, "not found")

def File_cut():
    org_file = input("Enter the path of original file: ")
    
    if os.path.exists(org_file):
        dest = input("Enter the path to move the file to: ")
        
        if os.path.exists(dest):
            shutil.move(org_file, dest)
            print("File moved to", dest)
            
            History(f"{org_file} moved to {dest}")
                
        else:
            print(dest, "not found")
            return
        
    else:
        print(org_file, "not found")
        return

def File_rename():
    old_name = input("Enter the current name of the file: ")
    new_name = input("Enter the new name for the file: ")
    
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print("File renamed from", old_name, "to", new_name)
        
        History(f"{old_name} renamed to {new_name}")

    else:
        print(old_name, "not found")

def File_edit_functions():
    print("1. Edit line by line")
    print("2. Edit the entire file")
    print("3. Replace one word with another")

def File_edit_line():
    a = input("Enter the name of the file to edit: ")
    
    if os.path.exists(a):
    
        line_number = int(input("Enter the line number to edit: "))
        line_mode = input("Enter 'overwrite' or 'append' to select the mode to edit the line: ")
        if line_mode == "overwrite":
            new_line = input("Enter the new line: ")
            with open(a, "r") as f:
                lines = f.readlines()
            if 0 < line_number <= len(lines):
                lines[line_number - 1] = new_line + "\n\n"
                with open(a, "w") as f:
                    f.writelines(lines)
                print("Line", line_number, "updated.")
                History(f"Line {line_number} in {a} updated from {lines[line_number - 1].strip()} to {new_line}")
            else:
                print("Invalid line number.")
        elif line_mode == "append":
            line_data = input("Enter the data to append: ")
            with open(a, "a+") as f:
                old_line = f.readlines()[line_number - 1] if line_number <= len(f.readlines()) else ""
                f.write(old_line + line_data + "\n\n")
            print("Data appended to line", line_number)
            
            History(f"Data appended to line {line_number} in {a}")
            
    else:
        print(a, "not found")
        return

def File_edit_full():
    a = input("Enter the name of the file to edit: ")
    
    if os.path.exists(a):
        full_mode = input("Enter 'overwrite' or 'append' to select the mode to edit the entire file: ")
        if full_mode == "overwrite":
            new_content = input("Enter the new content for the file: ")
            with open(a, "w") as f:
                f.write(new_content)
            print(a, "updated.")
            
            History(f"{a} overwritten with new content")
            
        elif full_mode == "append":
            append_content = input("Enter the content to append to the file: ")
            with open(a, "a") as f:
                f.write(append_content)
            print("Content appended to", a)
            
            History(f"Content appended to {a}")

    else:
        print(a, "not found")
        return
    
def File_edit():

    File_edit_functions()
    
    mode = input("Enter your choice: ").strip().lower()
    
    if mode in ["1", "edit line by line", "line by line", "line"]:
        File_edit_line()
        
    elif mode in ["2", "edit the entire file", "entire file", "full"]:
        File_edit_full()
            
    elif mode in ["3", "replace", "replace word"]:
        Word_replace()
        
    else:
        print("Invalid choice. Please try again.")
        return

def File_Editor():
    while True:
        Pass = input("\nEnter the password to access the File Editor: ")
        
        if converter(Pass) == "Koy#t_t#Zor#ag#":    
            while True:
                print("1. Create files")
                print("2. Delete files")
                print("3. View files")
                print("4. Edit files")
                print("5. Copy files")
                print("6. Cut files")
                print("7. Rename files")
                print("8. Back")
                choice = input("Enter your choice: ").strip().lower()

                menu = {
                "1": File_create,
                "create": File_create,
                "file create": File_create,
                "2": File_delete,
                "delete": File_delete,
                "3": File_view,
                "view": File_view,
                "4": File_edit,
                "edit": File_edit,
                "5": File_Copy,
                "copy": File_Copy,
                "6": File_cut,
                "cut": File_cut,
                "7": File_rename,
                "rename": File_rename
                }

                if choice in menu:
                    menu[choice]()

                elif choice in ["8", "back", "exit"]:
                    print("Logging out...")
                    break

                else:
                    print("Invalid choice. Please try again.")
                    
        elif Pass in ["exit", "quit"]:
            print("Exiting...")
            break

if __name__ == "__main__":
    File_Editor()
