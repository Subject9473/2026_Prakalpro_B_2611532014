deposit = int(input())
cash = {}
total_cash = 0

for _ in range(deposit):
    data = input().split()
    name = data[0]
    amount = int(data[1])

    total_cash += amount
    if name in cash:
        cash[name] += amount
    else:
        cash[name] = amount

top_name = ""
top_amount = -1

for name, total in cash.items():
    print(f"{name}: {total}")
    if total > top_amount:
        top_amount = total
        top_name = name

print(f"Total cash: {total_cash}")
print(f"Top contributor: {top_name} ({top_amount})")





















