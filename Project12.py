
amount_paid = int(input("How much did you pay ?"))
total_bill = int(input("How much was the total bill"))

change = amount_paid - total_bill

print(f"The shopkeeper should return:", change)