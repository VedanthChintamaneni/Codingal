string = input("Enter your word : ")

has_uppercase = any(ch.isupper() for ch in string)

if has_uppercase:
    print("Criteria Met")
else:
    print("Criteria not met.")