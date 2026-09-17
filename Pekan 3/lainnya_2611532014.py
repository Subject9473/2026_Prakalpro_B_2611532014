# buat file dengan nama lainnya_nim.py
# nama variabel ditambah 4 digit nim terakhir contoh : angka1_2014
# program ini menggunakan fungsi inut()
# program operator keanggotaan dan identitas

print("=================================")
print("1. OPERATOR KEANGGOTAAN")
print("=================================")

# Input beberapa data yang diisahkan dengan koma
input_data = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# mengubah input menjadi list integer
data = [int(angka.strip()) for angka in input_data.split(",")]

nilai_dicari = int(input("masukkan angka yang ingin dicari: "))

# Operator in
hasil = nilai_dicari in data 
print("\nOperator keanggotaan IN")
print(nilai_dicari, "in", data, "=", hasil)

# Operator not in
hasil = nilai_dicari not in data
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari, "not in", data, "=", hasil)


print("=================================")
print("2. OPERATOR IDENTITAS")
print("=================================")

# objek1 menggunakan list dari input pengguna
objek1_2014 = data

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2014 = objek1_2014

# objek3 memiliki isi yang sama, tetapi merupakan objek baru
objek3_2014 = data.copy()

print("objek1_2014 =", objek1_2014)
print("objek2_2014 =", objek2_2014)
print("objek3_2014 =", objek3_2014)

# Operator is
hasil = objek1_2014 is objek2_2014
print("\nOperator identitas IS")
print("objek1_2014 is objek2_2014 =", hasil)

# Operator is not
hasil = objek1_2014 is not objek3_2014
print("\nOperator identitas IS NOT")
print("objek1_2014 is not objek3_2014 =", hasil)

# membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_2014 is objek3_2014 =", objek1_2014 is objek3_2014)
print("objek1_2014 == objek3_2014 =", objek1_2014 == objek3_2014)








































