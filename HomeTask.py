string=input("Please enter your word :")

while len(string) < 8:
    print("The length of your word is", len(string))
    string=input("Please enter your word again :")

print("Criteria met.", len(string), "letters")
    