# buat file dengan nama logika_nim.py
#nama variabel ditambah 4 digit nim terakhir contoh : a1_2014 
#
#

# memasukkan nilai boolean
# input tidak peka terhadap huruf besar dan kecil
a1_2014 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_2014 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_2014)
print("A2 =", a2_2014)

# konjungsi: bernilai True jika keduanya True
hasil = a1_2014 and a2_2014
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil)

# Disjungsi: bernilai True jika salah satu True
hasil = a1_2014 or a2_2014
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil)

# Negasi A1: membalik nilai A1
hasil = not a1_2014
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil)

# Negasi A2: membalik nilai A2
hasil = not a2_2014
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil)

# XOR: bernilai True jika kedua nilai berbeda
hasil = a1_2014 != a2_2014
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil)
















