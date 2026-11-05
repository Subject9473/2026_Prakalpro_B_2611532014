total = 0

while True:
    angka = int(input("Enter a number: "))
    if angka < 0:
        break
    elif angka == 0:
        continue
    else:
        print(f"Positive number: {angka}")
        total += angka
print(f"Total: {total}")