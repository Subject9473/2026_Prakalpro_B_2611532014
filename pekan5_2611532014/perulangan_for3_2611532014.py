#program perulangan for

ulang_2014 = int(input("masukkan jumlah perulangan: "))

jumlah_2014 = 0
for i_2014 in range(1, ulang_2014+1):
    print(i_2014, end=" ")
    jumlah_2014 = jumlah_2014 + i_2014

    if i_2014 < ulang_2014:
        print("+", end=" ")
    else:
        print("=", jumlah_2014, end=" ")
print()
print("jumlah =", jumlah_2014)








