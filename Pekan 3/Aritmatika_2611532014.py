#buat file dengan nama aritmatika_nim.py
#buat program untuk operator aritmatika dalam python
#nama variabel ditambah 4 digit nim terakhir contoh : angka1_2014
#program ini menggunakan fungsi input()
#nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2014 = int(input("Input angka-1: "))
angka2_2014 = int(input("Input angka-2: "))

# Penjumlahan
hasil_2014 = angka1_2014 + angka2_2014
print("\nOperator Penjumlahan")
print("Hasil =", hasil_2014)

# Pengurangan
hasil_2014 = angka1_2014 - angka2_2014
print("\nOperator Pengurangan")
print("Hasil =", hasil_2014)

# Perkalian
hasil_2014 = angka1_2014 * angka2_2014
print("\nOperator Perkalian")
print("Hasil =", hasil_2014)

# Pembagian, pembagian bulat, dan sisa pembagian
if angka2_2014 != 0:
    hasil_2014 = angka1_2014 / angka2_2014
    print("\nOperator Pembagian")
    print("Hasil =", hasil_2014)

    hasil_2014 = angka1_2014 // angka2_2014
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2014)

    hasil_2014 = angka1_2014 % angka2_2014
    print("\nOperator Sisa Pembagian")
    print("Hasil =", hasil_2014)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_2014 = angka1_2014 ** angka2_2014
print("\nOperator Pangkat")
print("Hasil =", hasil_2014)





