import sys

#This program not working check it 

def add(n1, n2):
    result = n1+n2
    return result

def sub(n1, n2):
    result = n1-n2
    return result

def mul(n1, n2):
    result = n1*n2
    return result

def div(n1, n2):
    result = n1/n2
    return result


n1 = sys.argv[1]
operation = sys.argv[2]
n2 = sys.argv[3]

if operation == "add":
    output =add(num1, num2)
    print(output)