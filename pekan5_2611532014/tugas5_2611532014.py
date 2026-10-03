print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK ===")

n_2014 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Border atas
print()
print("#", end="")
for baris_2014 in range(4 * n_2014 + 5):
    print("=", end="")
print("#")

# Fase 1: Jam pasir atas
for baris_2014 in range(n_2014, 0, -1):
    print("|", end="")
    print(" ", end="")

    # Spasi kiri
    for spasi_2014 in range(2 * (n_2014 - baris_2014)):
        print(" ", end="")

    # Angka menurun
    for angka_2014 in range(baris_2014, 0, -1):
        print(angka_2014, end=" ")
    
    # Poros kristal
    print("<*>", end="")

    # Angka menaik
    for angka_2014 in range(1, baris_2014 + 1):
        print(" ", end="")
        print(angka_2014, end="")
    
    # Spasi kanan
    for spasi_2014 in range(2 * (n_2014 - baris_2014)):
        print(" ", end="")
    
    print(" |")

# Fase 2: Poros titik pusat
print("|", end="")

for spasi_2014 in range(2 * n_2014 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_2014 in range(2 * n_2014 + 1):
    print(" ", end="")

print("|")

# Fase 3: Jam pasir bawah
for baris_2014 in range(1, n_2014 + 1):
    print("|", end="")
    print(" ", end="")

    # Spasi kiri
    for spasi_2014 in range(2 * (n_2014 - baris_2014)):
        print(" ", end="")

    # Angka menurun
    for angka_2014 in range(baris_2014, 0, -1):
        print(angka_2014, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Angka menaik
    for angka_2014 in range(1, baris_2014 + 1):
        print(" ", end="")
        print(angka_2014, end="")

    # Spasi kanan
    for spasi_2014 in range(2 * (n_2014 - baris_2014)):
        print(" ", end="")

    print(" |")

# Border bawah
print("#", end="")
for baris_2014 in range(4 * n_2014 + 5):
    print("=", end="")
print("#")