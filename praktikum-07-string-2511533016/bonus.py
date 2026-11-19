# Name : Muhammad Fedora Argadyaksa
# Nim : 2511533016
# Question Bonus

sentence = input("Kalimat: ")

clean = sentence.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")