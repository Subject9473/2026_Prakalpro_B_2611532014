#
#
#
#
#

angka1_2014 = int(input("Input angka-1: "))
angka2_2014 = int(input("Input angka-2: "))

print("\nNilai awal angka1_2014 =", angka1_2014)
print("Nilai angka2_2014 =", angka2_2014)

# Assignment biasa
hasil = angka1_2014
print("\nAssignment biasa (=)")
print("Hasil =", hasil)

# Assignment penambahan 
hasil = angka1_2014
hasil += angka2_2014
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil)

# Assignment pengurangan
hasil = angka1_2014
hasil -= angka2_2014
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil)

# Assignment perkalian
hasil = angka1_2014
hasil *= angka2_2014
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil)

# Assignment pembagian, pembagian bulat, dan sisa pembagian
if angka2_2014 != 0:
    hasil = angka1_2014
    hasil /= angka2_2014
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil)
    # Operator tambahan
    hasil = angka1_2014
    hasil //= angka2_2014
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil)
    hasil = angka1_2014
    hasil %= angka2_2014
    print("\nAssignment sisa pembagian (%=)")
    print("Hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil = angka1_2014
hasil **= angka2_2014
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil)












