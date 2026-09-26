print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

nama_2014 = input("Masukkan Nama Pengunjung: ")
umur_2014 = int(input("Input umur anda: "))
sim_2014 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()[0]

print("\nPilihan Paket Wahana (1-5):")
print("1. Safari Rimba         (Rp 50,000)")
print("2. Arung Jeram          (Rp 75,000)")
print("3. Motor ATV Ekstrim    (Rp 120,000)")
print("4. Roller Coaster Kilat (Rp 100,000)")
print("5. All-Access VIP       (Rp 220,000)")

paket_2014 = int(input("\nMasukkan nomor paket (1-5): "))
jumlah_tiket_2014 = int(input("Masukkan jumlah tiket: "))

# If tunggal untuk validasi jumlah tiket
if jumlah_tiket_2014 <= 0:
    print("Peringatan: Kuota tiket tidak valid.")

# Match-case untuk memilih wahana
match paket_2014:
    case 1:
        nama_wahana_2014 = "Wahana Safari Rimba"
        harga_satuan_2014 = 50000
    case 2:
        nama_wahana_2014 = "Wahana Arung Jeram"
        harga_satuan_2014 = 75000
    case 3:
        nama_wahana_2014 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2014 = 120000
    case 4:
        nama_wahana_2014 = "Wahana Roller Coaster Kilat"
        harga_satuan_2014 = 100000
    case 5:
        nama_wahana_2014 = "Wahana All-Access VIP"
        harga_satuan_2014 = 220000
    case _:
        print("Paket wahana tidak valid!")
        raise SystemExit

print(f"\nWahana yang dipilih: {nama_wahana_2014}")
print(f"Harga satuan Rp {harga_satuan_2014:,.0f}")

# Validasi izin kendali wahana
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_2014 == 3:
    if umur_2014 >= 17 and sim_2014 == "y":
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_2014 >= 17 and sim_2014 != "y":
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_2014 < 17 and sim_2014 == "y":
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_2014 >= 10:
        print("Status Akses: Anda memenuhi batas usia untuk wahana ini.")
    else:
        print("Status Akses: Anda belum memenuhi batas usia untuk wahana ini.")

is_member_2014 = input("\nApakah Anda member? (y/t): ").strip().lower()
kode_promo_valid_2014 = input("Apakah kode promo valid? (y/t): ").strip().lower()

# Perhitungan subtotal
subtotal_2014 = harga_satuan_2014 * jumlah_tiket_2014
total_diskon_persen_2014 = 0

# Multi-if terpisah untuk akumulasi diskon
if subtotal_2014 >= 200000:
    total_diskon_persen_2014 += 10

if is_member_2014 in ["y", "ya"]:
    total_diskon_persen_2014 += 5

if kode_promo_valid_2014 in ["y", "ya"]:
    total_diskon_persen_2014 += 15

if jumlah_tiket_2014 >= 5:
    total_diskon_persen_2014 += 5

# Perhitungan diskon dan total pembayaran
nominal_diskon_2014 = subtotal_2014 * (total_diskon_persen_2014 / 100)
total_bayar_2014 = subtotal_2014 - nominal_diskon_2014

print("\n--- RINCIAN PEMBAYARAN ---")
print(f"Nama Pengunjung: {nama_2014}")
print(f"Wahana: {nama_wahana_2014}")
print(f"Jumlah Tiket: {jumlah_tiket_2014}")
print(f"Subtotal Belanja: Rp {subtotal_2014:,.0f}")
print(f"Total Diskon: {total_diskon_persen_2014}% (Rp {nominal_diskon_2014:,.0f})")
print(f"Total Bayar: Rp {total_bayar_2014:,.0f}")

# Evaluasi bonus menggunakan if-else
if total_bayar_2014 > 300000:
    print("Catatan Layanan: Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else:
    print("Catatan Layanan: Terima kasih telah berkunjung.")

print("\nProgram Selesai")
