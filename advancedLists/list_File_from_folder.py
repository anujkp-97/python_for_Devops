import os
folders = input("Please! provide all the folder name with space between them: ").split()


for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Provide a valid folder name!")
        break
    except PermissionError:
        print("Permission denied for folder ", folder)
        break
    except ZeroDivisionError:
        print("Cannot divided by zero!")
        break
    
    print("=== print all the files of ", folder)
    for file in files:
        print(file)