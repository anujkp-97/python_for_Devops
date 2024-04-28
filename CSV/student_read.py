import csv

with open("student_list.csv", "r") as file:
    content = file.read()

with open("student_list.csv", "w") as file1:
    file1.write("Hello, this is from the python file!!")

with open("student_list.csv","r") as file2:
    cont = file2.read()
print(cont)
print("----------------------------------------")

with open("student_list.csv", "a") as file1:
    file1.write("\n"+ "I am writing this line using the append!!")

with open("student_list.csv","r") as readFile:
    fileRead = readFile.read()

print(fileRead)


