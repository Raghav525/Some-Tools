import os
import shutil

def extract_extension(Folder_Path):
    files = os.listdir(Folder_Path)
    extensions = []
    names = []
    
    for f in files:
        full_path = os.path.join(Folder_Path, f)
        
        if os.path.isfile(full_path):
            name, ext = os.path.splitext(f)
            
            if ext:
                extensions.append(ext)
                names.append(name)
    
    return extensions, names

def create_folders(Folder_Path, extensions):
    for ext in extensions:
        folder_name = ext[1:].upper() + "_Files"    
        folder_path = os.path.join(Folder_Path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
    
def move_files(Folder_Path, extensions, names):
    folders = []
    for ext in extensions:
        folder_name = ext[1:].upper() + "_Files"
        folders.append(folder_name)
    
    for ext, name, folder in zip(extensions, names, folders):
        file_name = name + ext
        src = os.path.join(Folder_Path, file_name)
        dest = os.path.join(Folder_Path, folder, file_name)
        shutil.move(src, dest)
        
def main():
    while True:
        Folder_Path = input("Enter the folder path: ")
        if Folder_Path.lower() == "exit":
            print("Exiting the program.")
            break
        
        elif os.path.exists(Folder_Path):
            extensions, names = extract_extension(Folder_Path)
            create_folders(Folder_Path, extensions)
            move_files(Folder_Path, extensions, names)
            print("Files have been organised successfully!")
        else:
            print("The specified folder path does not exist.")
    
if __name__ == "__main__":
    main()
    