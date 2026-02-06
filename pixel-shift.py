#!/usr/bin/env python3

import os
import shutil

extension = (".jpg", ".png", ".jpeg", ".gif", ".ico", ".bmp",".tiff", ".tif", ".webp")

count = 0

while True:
    
    try:
        user_input = int(input("Enter 1. if you want to copy and 2. to move: "))
        if user_input in (1,2):
            break
        else:
            print("Error! Enter 1 or 2.\n")
    except ValueError:
        
        print("Error! Try again.")
        
src_dir = input("Enter source directory: ")
dest_dir = input("Enter destination directory: ")

if os.path.isdir(src_dir):
    print("Source directory found.")
elif os.path.isdir(src_dir) == False:
    print("Source directory not found.")

    while os.path.isdir(src_dir) == False:
        print("Wrong input!")
        src_dir = input("Enter source directory again: ")


if os.path.isdir(dest_dir):
    print("Destination directory found.")
elif os.path.isdir(dest_dir) == False:
    print("Destination directory not found.")

    while os.path.isdir(dest_dir) == False:
        print("Wrong input!")
        dest_dir = input("Enter destination directory again: ")


print("\n")

if user_input == 1:
    
 

    for filename in os.listdir(src_dir):
        
        src_path = os.path.join(src_dir, filename)    
        if os.path.isfile(src_path) and filename.lower().endswith(extension):

            shutil.copy(src_path , dest_dir)
            count = count + 1
            
            
    print(f"Task completed succesfully, {count} files copied.") 


elif user_input == 2:
    

    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)
        if os.path.isfile(src_path) and filename.lower().endswith(extension):
        
            shutil.move(src_path , dest_dir)
            count = count + 1
        

    print(f"Task completed succesfully, {count} files moved.") 

