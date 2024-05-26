print("[1] Javascript [2] Python [3] PHP [4] Java [5] Cpp" )
lang = input("What's the programming language you want to learn -")

def choose_lang(lang):
  match lang:
    case "Javascript":
        print("You can become a web developer")
    case "Python":
        print("You can become Data Scientist")
    case "PHP":
        print("You can become a backend developer")
    case "Java":
        print("You can become a mobile app developer")
    case "Cpp":
        print("You can become a competitive programmer")
    case _:
        print("The language doesn't matter, you are right to choose anyone")



    