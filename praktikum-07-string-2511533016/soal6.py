# Name : Muhammad Fedora Argadyaksa
# Nim : 2511533016
# Question 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())


full_name = "Muhammad Fedora Argadyaksa"
nim = "2511533016"

full_name = full_name.strip()
space = full_name.find(" ")

if space == -1:
    first_name = full_name
else:
    first_name = full_name[:space]

username = first_name.lower() + nim[-3:]
print(username)