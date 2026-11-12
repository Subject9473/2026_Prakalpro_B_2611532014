<<<<<<< HEAD
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
=======
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
>>>>>>> 15a643f990a229fb10923e5a4a73c7ce8adbbb2d
print(f"Total: {total}")