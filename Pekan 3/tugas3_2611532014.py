# SIMULASI TRANSAKSI DAN VALIDASI AKSES TOKO
print("=== SISTEM TRANSAKSI TOKO ===")

# INPUT DATA
nama_2014 = input("Masukkan Nama Pelanggan : ")
status_2014 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_2014 = int(input("Masukkan Total Belanja : "))
jumlah_barang_2014 = int(input("Masukkan Jumlah Barang : "))
kode_promo_2014 = input("Masukkan Kode Promo : ").upper()

# DAFTAR PROMO
promo_2014 = ["HEMAT10", "HEMAT20", "MAHASISWAFTI"]

# OPERATOR PERBANDINGAN
syarat_belanja_2014 = total_belanja_2014 >= 200000
syarat_barang_2014 = jumlah_barang_2014 >= 3
status_member_2014 = status_2014 == "member"

# OPERATOR KEANGGOTAAN
promo_tersedia_2014 = kode_promo_2014 in promo_2014
promo_tidak_tersedia_2014 = kode_promo_2014 not in promo_2014

# OPERATOR LOGIKA
diskon_member_2014 = status_member_2014 and syarat_belanja_2014
promo_kelayakan_2014 = (
    syarat_belanja_2014
    and syarat_barang_2014
    and promo_tersedia_2014
)
akses_pelanggan_2014 = status_member_2014 or promo_tersedia_2014
tidak_memenuhi_promo_2014 = not promo_tersedia_2014

# OPERATOR ARITMATIKA
diskon_2014 = 0

if diskon_member_2014:
    diskon_2014 = total_belanja_2014 * 0.10
elif syarat_belanja_2014:
    diskon_2014 = total_belanja_2014 * 0.05
total_pembayaran_2014 = total_belanja_2014 - diskon_2014

harga_rata_2014 = total_belanja_2014 / jumlah_barang_2014

# OPERATOR PENUGASAN
poin_2014 = 0
poin_2014 += jumlah_barang_2014

if status_member_2014:
    poin_2014 += 10

saldo_poin_2014 = poin_2014

if promo_kelayakan_2014:
    saldo_poin_2014 -= 1

faktor_pembayaran_2014 = 1
faktor_pembayaran_2014 *= 1

nilai_per_item_2014 = total_belanja_2014
nilai_per_item_2014 /= jumlah_barang_2014

# OPERATOR IDENTITAS
objek_a_2014 = ["member"]
objek_b_2014 = ["member"]

identitas_sama_2014 = objek_a_2014 is objek_b_2014
identitas_berbeda_2014 = objek_a_2014 is not objek_b_2014
nilai_sama_2014 = objek_a_2014 == objek_b_2014

# OPERATOR BITWISE
# 0001 = Member
# 0010 = Belanja >= Rp200.000
# 0100 = Jumlah barang >= 3
# 1000 = Promo tersedia

kode_status_2014 = 0

if status_member_2014:
    kode_status_2014 |= 1

if syarat_belanja_2014:
    kode_status_2014 |= 2

if syarat_barang_2014:
    kode_status_2014 |= 4

if promo_tersedia_2014:
    kode_status_2014 |= 8

cek_member_bit_2014 = kode_status_2014 & 1
cek_promo_bit_2014 = kode_status_2014 & 8
gabungan_bit_2014 = kode_status_2014 | 8

kode_referensi_2014 = 11
perbedaan_bit_2014 = kode_status_2014 ^ kode_referensi_2014
hasil_shift_2014 = kode_status_2014 << 1

# ==========================================================
# OUTPUT
# ==========================================================

print("\n=== DATA PELANGGAN ===")
print("Nama Pelanggan   :", nama_2014)
print("Status Pelanggan :", status_2014)
print("Total Belanja    : Rp", total_belanja_2014)
print("Jumlah Barang    :", jumlah_barang_2014)
print("Kode Promo       :", kode_promo_2014)

print("\n=== HASIL VALIDASI ===")
print("Belanja >= 200000       :", syarat_belanja_2014)
print("Jumlah Barang >= 3      :", syarat_barang_2014)
print("Status Member            :", status_member_2014)
print("Kode Promo Tersedia      :", promo_tersedia_2014)
print("Mendapatkan Diskon       :", diskon_member_2014)
print("Mendapatkan Promo        :", promo_kelayakan_2014)

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon           : Rp", diskon_2014)
print("Total Pembayaran : Rp", total_pembayaran_2014)
print("Rata-rata Barang  : Rp", harga_rata_2014)

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses           :", kode_status_2014)
print("Member Access            :", status_member_2014)
print("Promo Access             :", promo_kelayakan_2014)
print("Free Shipping Access     :", promo_tersedia_2014)

print("\n=== HASIL OPERATOR ===")

print("\nOperator Perbandingan")
print("Total >= 200000          :", syarat_belanja_2014)
print("Jumlah Barang >= 3       :", syarat_barang_2014)
print("Status == member         :", status_member_2014)

print("\nOperator Logika")
print("Member AND Belanja       :", diskon_member_2014)
print("Member OR Promo          :", akses_pelanggan_2014)
print("NOT Promo                :", tidak_memenuhi_promo_2014)

print("\nOperator Penugasan")
print("Poin setelah +=          :", poin_2014)
print("Poin setelah -=          :", saldo_poin_2014)
print("Faktor setelah *=        :", faktor_pembayaran_2014)
print("Nilai per item setelah /=:", nilai_per_item_2014)

print("\nOperator Keanggotaan")
print("Kode Promo IN daftar     :", promo_tersedia_2014)
print("Kode Promo NOT IN daftar :", promo_tidak_tersedia_2014)

print("\nOperator Identitas")
print("objek_a IS objek_b       :", identitas_sama_2014)
print("objek_a IS NOT objek_b   :", identitas_berbeda_2014)
print("objek_a == objek_b       :", nilai_sama_2014)

print("\nOperator Bitwise")
print("Kode Status Biner        :", format(kode_status_2014, "04b"))
print("Kode Status Desimal      :", kode_status_2014)
print("Cek Member (& 0001)      :", cek_member_bit_2014)
print("Cek Promo (& 1000)       :", cek_promo_bit_2014)
print("Hasil OR (| 1000)        :", gabungan_bit_2014)
print("Hasil XOR (^ 1011)       :", perbedaan_bit_2014)
print("Hasil Shift (<< 1)       :", hasil_shift_2014)

print("\n=== SELESAI ===")

