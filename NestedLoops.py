string=input("Please enter your word :")
char=input("Enter the character you want to find out: ")
i = 0
count = 0
while(i < len(string)):
    if(string[i]== char):
        count=count + 1
    i = i + 1
print("The total number of times", char, "has occurred =", count)