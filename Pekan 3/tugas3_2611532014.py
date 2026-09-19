# PROGRAM KASIR SEDERHANA
# 1. DATA PELANGGAN DAN TRANSAKSI

nama_2014 = input("Masukkan Nama Pelanggan : ")
status_2014 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_2014 = float(input("Masukkan Total Belanja : "))
jumlah_barang_2014 = int(input("Masukkan Jumlah Barang : "))
kode_promo_2014 = input("Masukkan Kode Promo : ").upper()

# 2. DAFTAR KODE PROMO

promo_2014 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# 3. OPERATOR PERBANDINGAN

syarat_belanja_2014 = total_belanja_2014 >= 200000
syarat_barang_2014 = jumlah_barang_2014 >= 3
promo_tersedia_2014 = kode_promo_2014 in promo_2014

# 4. MENENTUKAN BESAR DISKON

diskon_2014 = 0
if status_2014 == "member" and syarat_belanja_2014:
    diskon_2014 = total_belanja_2014 * 0.10
elif syarat_belanja_2014:
    diskon_2014 = total_belanja_2014 * 0.05
total_pembayaran_2014 = total_belanja_2014 - diskon_2014

harga_rata_2014 = total_belanja_2014 / jumlah_barang_2014

sisa_pembagian_2014 = total_belanja_2014 % 1000


# 6. OPERATOR PENUGASAN / AUGMENTED ASSIGNMENT

poin_2014 = 0
poin_2014 += jumlah_barang_2014

if status_2014 == "member":
    poin_2014 += 10

# Contoh augmented assignment lainnya
total_pembayaran_2014 *= 1.00


# 7. OPERATOR LOGIKA

diskon_member_2014 = (
    status_2014 == "member" and
    syarat_belanja_2014
)

promo_kelayakan_2014 = (
    syarat_belanja_2014 and
    syarat_barang_2014 and
    promo_tersedia_2014
)

akses_pelanggan_2014 = (
    status_2014 == "member" or
    promo_tersedia_2014
)

tidak_memenuhi_promo_2014 = not promo_tersedia_2014


# 8. OPERATOR KEANGGOTAAN

promo_tersedia_2014 = kode_promo_2014 in promo_2014
promo_tidak_tersedia_2014 = kode_promo_2014 not in promo_2014


# 9. OPERATOR IDENTITAS

objek_a_2014 = ["member"]
objek_b_2014 = ["member"]

identitas_sama_2014 = objek_a_2014 is objek_b_2014
identitas_berbeda_2014 = objek_a_2014 is not objek_b_2014
nilai_sama_2014 = objek_a_2014 == objek_b_2014


# 10. OPERATOR BITWISE

# Nilai bit:
# 0001 = member
# 0010 = belanja >= 200000
# 0100 = jumlah barang >= 3
# 1000 = promo tersedia

kode_status_2014 = 0

if status_2014 == "member":
    kode_status_2014 |= 1

if syarat_belanja_2014:
    kode_status_2014 |= 2

if syarat_barang_2014:
    kode_status_2014 |= 4

if promo_tersedia_2014:
    kode_status_2014 |= 8


# AND (&) untuk memeriksa kondisi member
cek_member_bit_2014 = kode_status_2014 & 1

# OR (|) untuk menggabungkan kondisi
gabungan_bit_2014 = kode_status_2014 | 8

# XOR (^) untuk membandingkan dua kode status
kode_pembanding_2014 = 3
perbedaan_bit_2014 = kode_status_2014 ^ kode_pembanding_2014


# 11. MENENTUKAN STATUS PROMO

if promo_kelayakan_2014:
    status_promo_2014 = "Mendapatkan promo"
else:
    status_promo_2014 = "Tidak mendapatkan promo"


# 12. MENENTUKAN HAK AKSES PELANGGAN

if status_2014 == "member" and promo_tersedia_2014:
    hak_akses_2014 = "Memiliki hak akses promo member"
elif promo_tersedia_2014:
    hak_akses_2014 = "Memiliki hak akses promo umum"
else:
    hak_akses_2014 = "Tidak memiliki hak akses promo"


# ==========================================
# HASIL PROGRAM
# ==========================================

print("\n==========================================")
print("           DATA PELANGGAN")
print("==========================================")

print("Nama Pelanggan :", nama_2014)
print("Status Pelanggan :", status_2014)
print("Total Belanja :", total_belanja_2014)
print("Jumlah Barang :", jumlah_barang_2014)
print("Kode Promo :", kode_promo_2014)


print("\n==========================================")
print("          HASIL PERHITUNGAN")
print("==========================================")

print("Besarnya Diskon :", diskon_2014)
print("Total Pembayaran :", total_pembayaran_2014)
print("Harga Rata-rata Barang :", harga_rata_2014)
print("Sisa Pembagian :", sisa_pembagian_2014)
print("Poin Pelanggan :", poin_2014)


print("\n==========================================")
print("           HASIL VALIDASI")
print("==========================================")

print("Memenuhi minimum belanja? :", syarat_belanja_2014)
print("Jumlah barang memenuhi syarat? :", syarat_barang_2014)
print("Mendapatkan diskon member? :", diskon_member_2014)
print("Kode promo tersedia? :", promo_tersedia_2014)
print("Mendapatkan promo? :", status_promo_2014)
print("Hak Akses :", hak_akses_2014)


print("\n==========================================")
print("            HASIL OPERATOR")
print("==========================================")

# Operator aritmatika
print("\n[Operator Aritmatika]")
print("Diskon = Total Belanja x Persentase Diskon :", diskon_2014)
print("Total Pembayaran = Total Belanja - Diskon :", total_pembayaran_2014)
print("Rata-rata = Total Belanja / Jumlah Barang :", harga_rata_2014)
print("Sisa Pembagian (%) :", sisa_pembagian_2014)

# Operator perbandingan
print("\n[Operator Perbandingan]")
print("Total Belanja >= 200000 :", syarat_belanja_2014)
print("Jumlah Barang >= 3 :", syarat_barang_2014)

# Operator logika
print("\n[Operator Logika]")
print("Member AND Belanja Minimum :", diskon_member_2014)
print("Belanja AND Barang AND Promo :", promo_kelayakan_2014)
print("Member OR Promo Tersedia :", akses_pelanggan_2014)
print("NOT Promo Tersedia :", tidak_memenuhi_promo_2014)

# Operator penugasan
print("\n[Operator Penugasan]")
print("Poin setelah += :", poin_2014)
print("Total setelah *= :", total_pembayaran_2014)

# Operator keanggotaan
print("\n[Operator Keanggotaan]")
print("Kode promo IN daftar :", promo_tersedia_2014)
print("Kode promo NOT IN daftar :", promo_tidak_tersedia_2014)

# Operator identitas
print("\n[Operator Identitas]")
print("objek_a IS objek_b :", identitas_sama_2014)
print("objek_a IS NOT objek_b :", identitas_berbeda_2014)
print("objek_a == objek_b :", nilai_sama_2014)

# Operator bitwise
print("\n[Operator Bitwise]")
print("Kode Status :", kode_status_2014)
print("AND (&) :", cek_member_bit_2014)
print("OR (|) :", gabungan_bit_2014)
print("XOR (^) :", perbedaan_bit_2014)