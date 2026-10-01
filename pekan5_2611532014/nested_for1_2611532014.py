#program perulangan for

batas_2014 = int(input("masukkan nilai batas: "))
for line in range(1, batas_2014 + 1):
    for j_2014 in range(1, (-1 * line + batas_2014) + 1):
        print(" . ", end=" ")
    print(line)















