# len, concat, uppercase, lowercase, capitalize, replace, strip, split, substring

text = "welcome to the python programming"
print(text)
print("--------------------------------------------")
length = len(text)
print("Length of text : ", length)
text2 = "with Anuj Kumar"
con = text + " " + text2
print("String after concat: ", con)
print("--------------------------------------------")

#To uppercase
toUpper = text.upper()
print("Uppercase String: ", toUpper) 
print("--------------------------------------------")

toLower = text.lower()
print("Lowercase String: ", toLower)
print("--------------------------------------------")

toCapitalize = text.capitalize()
print("To capitalize String: ", toCapitalize)
print("--------------------------------------------")

replace = text.replace("python" ,"Java")
print("Python to Java replace: ", replace)
print("--------------------------------------------")

text1 ="       This is from the strip function of the python"
print("Without the strip(): ", text1)
print("With strip(): ", text1.strip())
print("--------------------------------------------")

split1 = "My contact no. /99302843"
split1 = split1.split("/")
print(split1)

print("--------------------------------------------")
#substring
s ="I am Anuj Kumar"
# print s[0,5], sub[:5], sub[2:]
substrin = s[1:6]   #excluding the 6
print(substrin)
inn = "Anu"
if inn in s:
    print("Found in s")
else:
    print("Not found")
