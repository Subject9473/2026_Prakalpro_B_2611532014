LAST_DIGIT = 4 # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below

for i in range(1, 8):
    amount = int(input(f"day {i}: "))
    expenses.append(amount)

total = 0
highest_day = 1
highest_val = expenses[0]
days_above = 0

for i in range(len(expenses)):
    total += expenses[i]
    if expenses[i] > highest_val:
        highest_val = expenses[i]
        highest_day = i + 1
    if expenses[i] > daily_limit:
        days_above += 1

average = total/len(expenses)

print("daily limit: ", daily_limit)
print("total: ", total)
print(f"average: {average:.1f}")
print(f"highest: day {highest_day} ({highest_val})")
print("days above limit: ", days_above)










