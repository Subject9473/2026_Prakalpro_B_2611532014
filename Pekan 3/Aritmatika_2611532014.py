#buat file dengan nama aritmatika_nim.py
#buat program untuk operator aritmatika dalam python
#nama variabel ditambah 4 digit nim terakhir contoh : angka1_2014
#program ini menggunakan fungsi input()
#

angka1_2014 = int(input("Input angka-1: "))
angka2_2014 = int(input("Input angka-2: "))

# Penjumlahan
hasil = angka1_2014 + angka2_2014
print("\nOperator Penjumlahan")
print("Hasil =", hasil)

# Pengurangan
hasil = angka1_2014 - angka2_2014
print("\nOperator Pengurangan")
print("Hasil =", hasil)

# Perkalian
hasil = angka1_2014 * angka2_2014
print("\nOperator Perkalian")
print("Hasil =", hasil)

# Pembagian, pembagian bulat, dan sisa pembagian
if angka2_2014 != 0:
    hasil = angka1_2014 / angka2_2014
    print("\nOperator Pembagian")
    print("Hasil =", hasil)

    hasil = angka1_2014 // angka2_2014
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil)

    hasil = angka1_2014 % angka2_2014
    print("\nOperator Sisa Pembagian")
    print("Hasil =", hasil)
else:
    print("Angka kedua tidak bleh bernilai 0.")

# Pangkat
hasil = angka1_2014 ** angka2_2014
print("\nOperator Pangkat")
print("Hasil =", hasil)





