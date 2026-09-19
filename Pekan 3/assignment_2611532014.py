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
hasil_2014 = angka1_2014
print("\nAssignment biasa (=)")
print("Hasil =", hasil_2014)

# Assignment penambahan 
hasil_2014 = angka1_2014
hasil_2014 += angka2_2014
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_2014)

# Assignment pengurangan
hasil_2014 = angka1_2014
hasil_2014 -= angka2_2014
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_2014)

# Assignment perkalian
hasil_2014 = angka1_2014
hasil_2014 *= angka2_2014
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_2014)

# Assignment pembagian, pembagian bulat, dan sisa pembagian
if angka2_2014 != 0:
    hasil_2014 = angka1_2014
    hasil_2014 /= angka2_2014
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_2014)
    # Operator tambahan
    hasil_2014 = angka1_2014
    hasil_2014 //= angka2_2014
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_2014)
    hasil_2014 = angka1_2014
    hasil_2014 %= angka2_2014
    print("\nAssignment sisa pembagian (%=)")
    print("Hasil =", hasil_2014)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_2014 = angka1_2014
hasil_2014 **= angka2_2014
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_2014)












