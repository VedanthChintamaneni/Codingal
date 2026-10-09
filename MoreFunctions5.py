import random
name = input("What is your name ?")
print(name + ", we are going to play a game. I am thinking of a number between 1 and 100. Try figure it out !")
playing = True 
number = str(random.randint(0, 100))

print("I will generate a number from 0 to 100, and you have to guess the number one digit at a time.")
print("The game ends when you get it right!")


 
while playing:
        guess = input("Give me your best guess!\n")
if (number%2==0):
        print("its even")
else:
        print("its odd")
if number == guess:
        print("You win the game")
        print("The number was", number)
else:
        print("Your guess is not right, try again.\n")