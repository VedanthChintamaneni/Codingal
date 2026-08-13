s = input("Enter a whole number: ")
if:
    n = int(s)
else:
    if n == 0:
        print("Binary of your input: 0")
    else:
        binary = ""
        while n > 0:
            remainder = n % 2
            new_binary = str(remainder)
            for ch in binary:
                new_binary += ch
            binary = new_binary
            n = n // 2
        print("Binary of your input:", binary)