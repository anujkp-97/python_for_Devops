#Regex is used to search the string in text or find the matching 
import re
text = "this is world wide technology"
pattern =r"wrld"

search = re.search(pattern, text)
if search:
    print("find in the text")
else: 
    print("Not found in text")
print("-------------------------------------------")

text1 = "This is the new world of Bharat"
pattern =r"is"

match = re.match(pattern, text1)
if match:
    print("Match found")
else:
    print("Match not found")
print("--------------------------------------------")

text3="Red, Yellow, Orange, Blue, Safforn, Green"
pattern = r","

result = re.split(pattern, text3)
print("Split the string ", result)
