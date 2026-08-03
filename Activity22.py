units=int(input("What is the number of units you have used ?"))
if units < 50:
    print("Your electricity bill will be", units * 2.60 + 25)
elif 50 < units < 100:
    print("Your electricity bill will be", units * 3.25 + 35)
elif 100 < units < 200:
    print("Your electricity bill will be", units * 5.26 + 45)
else:
    print("Your electricity bill will be", units * 8.45 + 75)