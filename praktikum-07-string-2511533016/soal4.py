# Name : Muhammad Fedora Argadyaksa
# Nim : 2511533016
# Question 4

phone = "082511533016"
masked = phone[:4] + (len(phone) - 7) * "*" + phone[-3:]
print(masked)
