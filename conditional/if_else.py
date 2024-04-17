
# marks = int(input("Enter your marks: "))
# result = ""
# if marks < 30:
#    result = "Failed"
# elif marks > 75:
#    result = "Passed with distinction"
# else:
#    result = "Passed"

# print(result)

# program to check whether you can allow to play the tourname or not, 
# if your weight is in the range of 65 kg to 70 kg then you can play
# weight = int(input("Enter your weight: "))
# result=""

# if weight in range(65, 71):
#     result="Congratulations! You are qualified"
# else:
#     result="OOPS! Better luck next!"
# print(result)

#switch statement
# print("[1] Sunday [2] Monday [3] Tuesday [4] Wednesday [5] Thursday")
# choose = int(input("Choose any one option: "))

# match choose:
#     case 1: print("Today is holiday!")
#     case 2: print("Today is working day!")
#     case 3: print("Today is working day!")
#     case 4: print("Today is holiday!")
#     case 5: print("Today is working day!")
#     case _: print("Today is half day!")

discount =0
amount = int(input("Enter the amount: "))
if(amount>1000):
    discount= (amount*10)/100
    print("Your total bill: ",amount-discount)
else:
    print("Your total bill: ",amount)
