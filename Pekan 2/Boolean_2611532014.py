#buat file dengan nama boolean_nim.py
#nama variabel ditambah 4 digit nim terakhir contoh: nilai_2014
#deklarasi variable dengan tipe data boolean
is_lulus =true
is_cumlaude = true

#menggunakan boolean
nilai_2014 = 85
batas_lulus = 75

#menentukan nilai bolean dari kondisi
status_kelulusan = nilai_2014 >= batas_lulus #hasilnya akan true

print("=== check kelulusan ===")
print("Nilai:", nilai_2014)
print("apakah lulus?:", status_kelulusan)
if is_lulus and is_cumlaude:
print("Selamat, anda lulus dengan predikat Cum Laude")
