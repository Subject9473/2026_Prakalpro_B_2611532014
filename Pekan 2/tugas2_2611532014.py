from typing import Final

BATAS_LULUS: Final = 75.0
print("\n=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_2014 = input("Masukkan Nama Mahasiswa: ")

jenis_kelamin_2014 = input("Masukkan Jenis Kelamin (L/P): ")

umur_2014 = int(input("Masukkan Umur: "))

nilai_2014 = float(input("Masukkan Skor Tes Awal: "))

alamat_2014 = """
Kampus Unand
Kec. Pauh
Kota Padang
"""

token_2014 = 143 + 6j

status_lulus_2014 = nilai_2014 >= BATAS_LULUS

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa: ", nama_2014, "| Tipe:", type(nama_2014))
print("Jenis Kelamin: ", jenis_kelamin_2014, "| Tipe:", type(jenis_kelamin_2014))
print("Alamat Domisili: ", alamat_2014, "| Tipe:", type(alamat_2014))
print("Umur: ", umur_2014, "| Tipe:", type(umur_2014))
print("Skor Tes Awal: ", nilai_2014, "| Tipe:", type(nilai_2014))
print("ID Token Sinyal: ", token_2014, "| Tipe:", type(token_2014))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?: ", status_lulus_2014, "| Tipe:", type(status_lulus_2014))

if status_lulus_2014:
    print("Selamat,", nama_2014, "dinyatakan LULUS praktikum.")
else:
    print("Maaf,", nama_2014, "dinyatakan BELUM LULUS praktikum.")
