## This Program is to list the files from the folders using functions & try and except 

import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    print(type(folder_paths))
    for folder_path in folder_paths:
        # Below Declearing variable a and b for accesing return values from list_files_in_folder(folder_path) function 
        a, b = list_files_in_folder(folder_path)
        print("a Value: ", a)
        print("b Value: ", b)
        if a:
            print("Files in: ",folder_path)
            for file in a:
                print(file)
        else:
            print(f"Error in {folder_path}: {b}")

if __name__ == "__main__":
    main()



