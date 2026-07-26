word=input ("What is your word ?")
word=word.lower()
backward_word = word[::-1]
print("Your word backward is", backward_word)
if word == backward_word:
    print("Palindrome")