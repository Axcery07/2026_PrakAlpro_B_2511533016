LAST_DIGIT = 6  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below

# Baca 7 pengeluaran
for i in range(1, 8):
    nilai = int(input(f"Day {i}: "))
    expenses.append(nilai)

# Hitung total
total = 0
for e in expenses:
    total = total + e

# Hitung average
average = total / 7

# Cari hari dengan pengeluaran tertinggi
highest_val = expenses[0]
highest_day = 1
for i in range(1, 7):
    if expenses[i] > highest_val:
        highest_val = expenses[i]
        highest_day = i + 1

# Hitung days above limit
days_above = 0
for e in expenses:
    if e > daily_limit:
        days_above = days_above + 1

# Cetak output
print("Daily limit:", daily_limit)
print("Total:", total)
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest_val})")
print("Days above limit:", days_above)
