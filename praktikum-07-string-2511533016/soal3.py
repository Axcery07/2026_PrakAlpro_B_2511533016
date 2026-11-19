# Name : Muhammad Fedora Argadyaksa
# Nim : 2511533016
# Question 3

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

text = "Algoritma dan pemrograman"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)
