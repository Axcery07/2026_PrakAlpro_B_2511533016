# Name : Muhammad Fedora Argadyaksa
# Nim : 2511533016
# Question 7

name = "siti aisyah"
nim = "2610511023"

clean = name.strip()
space = clean.find(" ")
if space == -1:
    first_name = clean
else:
    first_name = clean[:space]
username = first_name.lower() + nim[-3:]

intake = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print("Name".ljust(10) + ": " + name.title())
print("NIM".ljust(10) + ": " + nim)
print("Username".ljust(10) + ": " + username)
print("Intake".ljust(10) + ": " + intake)
print("=" * 30)