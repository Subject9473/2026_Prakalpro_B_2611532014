# buat file dengan nama perbandingan_nim.py
# nama variabel ditambah 4 digit nim terakhir contoh : angka1_2014
# program ini menggunakan fungsi input()
# nilai yang dimasukkan akaan dikonversi menjadi tipe data integer
# program operator perbandingan dalam python

angka1_2014 = int(input("Input angka-1: "))
angka2_2014 = int(input("Input angka-2: "))

# lebih besar dari
hasil = angka1_2014 > angka2_2014
print("\nOperator lebih besar dari")
print("angka1_2014 > angka2_2014 =", hasil)

# lebih kecil dari
hasil = angka1_2014 < angka2_2014
print("\nOperator lebih kecil dari")
print("angka1_2014 < angka2_2014 =", hasil)

# Lebih besar dari atau sama dengan
hasil = angka1_2014 >= angka2_2014
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_2014 >= angka2_2014 =", hasil)

# Lebih kecil dari atau sama dengan
hasil = angka1_2014 <= angka2_2014
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1_2014 <= angka2_2014 =", hasil)

# Sama dengan
hasil = angka1_2014 == angka2_2014
print("\nOperator sama dengan")
print("angka1_2014 == angka2_2014 =", hasil)

# Tidak sama dengan
hasil = angka1_2014 != angka2_2014
print("\nOperator tidak sama dengan")
print("angka1_2014 != angka2_2014 =", hasil)

# Tambahan: perbandingan berantai dalam Python
hasil = 0 < angka1_2014 < 100
print("\nPerbandingan berantai")
print("0 < angka1_2014 < 100 =", hasil)

hasil = 0 < angka2_2014 < 100
print("0 < angka2_2014 < 100", hasil)












