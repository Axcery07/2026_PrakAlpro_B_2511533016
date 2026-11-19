menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

for i in range(1, number_of_days + 1):
    row = []
    for j in menus:
        porsi = int(input(f"Day {i}, {j}: "))
        row.append(porsi)
    sales.append(row)

print("Total per day: ")
for i in range(len(sales)):
    total_hari=0
    for porsi in sales[i]:
        total_hari += porsi
    print(f"Day ", i+1 , ": ", total_hari) 

menu_totals = []
for m in range(len(menus)):
    total_menu = 0
    for n in range(len(sales)):
        total_menu += sales[n][m]
    menu_totals.append((menus[m], total_menu))
print("Total per menu:", menu_totals)

best_name, best_total = menu_totals[0]
for name, total in menu_totals:
    if total > best_total:
        best_name, best_total = name, total
print(f"Best seller: {best_name} ({best_total})")