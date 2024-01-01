## This Program is to list the files from the folders

import os

folders = input("Provide folders names with spaces in between: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name: " + "not " + folder)
        break
#        continue (To Continue with out breaking the loop then use continue (OR) Ignore the errors)
    print("###### List files for the folder : " + folder + " ######")
    for file in files:
        print(file)


# Below code is written in FUNCTIONS

# def list_files_in_folder(folder_path):
#     try:
#         files = os.listdir(folder_path)
#         return files, None
#     except FileNotFoundError:
#         return None, "Folder not found"

# def main():
#     print("123")
#     folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
#     for folder_path in folder_paths:
# #        print("FOLDER: ",folder_path)
#         files, error_message = list_files_in_folder(folder_path)
#         if files:
#             print(files)


# if __name__ == "__main__":
#     main()
