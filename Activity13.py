buy= float(input("Enter the price of which you have bought:"))
sell= float(input("Enter the price of which you have sold:"))
profit=(sell-buy)
if sell > buy:
    print("Your profit is", sell-buy)
else:
    print("Your loss is", buy-sell)