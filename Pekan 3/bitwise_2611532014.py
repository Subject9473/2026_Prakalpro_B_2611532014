#buat file dengan nama bitwise_nim.py
#nama variabel ditambah 4 digit terakhir contoh angka1_2014
#program ini menggunakan fungsi input()

print("\n=================================")
print("3. OPERATOR BITWISE")
print("=================================")

angka1_2014 = int(input("Masukkan angka bitwise-1: "))
angka2_2014 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalamm bentuk desimal dan biner")
print("angka1_2014 =", angka1_2014, "| biner =", bin(angka1_2014))
print("angka2_2014 =", angka2_2014, "| biner =", bin(angka2_2014))

# Bitwise AND
hasil_2014 = angka1_2014 & angka2_2014
print("\nBitwise AND (&)")
print(angka1_2014, "&", angka2_2014, "=", hasil_2014)
print("Biner hasil =", bin(hasil_2014))
print("Biner hasil (8 bit) =", format(hasil_2014, "08b"))

# Bitwise OR
hasil_2014 = angka1_2014 | angka2_2014
print("\nBitwise OR (|)")
print(angka1_2014, "|", angka2_2014, "=", hasil_2014)
print("Biner hasil =", bin(hasil_2014))
print("Biner hasil (8 bit) =", format(hasil_2014, "08b"))

# Bitwise XOR
hasil_2014 = angka1_2014 ^ angka2_2014
print("\nBitwise XOR (^)")
print(angka1_2014, "^", angka2_2014, "=", hasil_2014)
print("Biner hasil =", bin(hasil_2014))
print("Biner hasil (8 bit) =", format(hasil_2014, "08b"))

# Bitwise NOT
hasil_2014 = ~angka1_2014
print("\nBitwise NOT (~)")
print("~", angka1_2014, "=", hasil_2014)
print("Biner hasil =", bin(hasil_2014))
print("Biner hasil (8 bit) =", format(hasil_2014, "08b"))

# Bitwise geser kiri
jumlah_geser_2014 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2014 = angka1_2014 << jumlah_geser_2014 
print("\nBitwise geser kiri (<<)")
print(angka1_2014, "<<", jumlah_geser_2014, "=", hasil_2014)
print("Biner hasil =", bin(hasil_2014))
print("Biner hasil (8 bit) =", format(hasil_2014, "08b"))

# Bitwise geser kanan
hasil_2014 = angka1_2014 >> jumlah_geser_2014 
print("\nBitwise geser kanan (>>)")
print(angka1_2014, ">>", jumlah_geser_2014, "=", hasil_2014)
print("Biner hasil =", bin(hasil_2014))
print("Biner hasil (8 bit) =", format(hasil_2014, "08b"))









































