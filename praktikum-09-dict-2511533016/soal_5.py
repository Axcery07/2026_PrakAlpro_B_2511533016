n = int(input())

cash = {}

for i in range(n):
    data = input().split()
    name = data[0]
    amount = int(data[1])

    if name in cash:
        cash[name] += amount
    else:
        cash[name] = amount

total_cash = sum(cash.values())

for name, total in cash.items():
    print(name + ":", total)

print("Total cash:", total_cash)

top_name = ""
top_total = 0

for name, total in cash.items():
    if total > top_total:
        top_name = name
        top_total = total

print("Top contributor:", top_name, "(" + str(top_total) + ")")