#multi if

#input dari user
total_belanja_2014 = float(input("masukkan total belanja (Rp): "))

#input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2014 = input("apakah anda member? (y/t): ").strip().lower()
is_member_2014 = input_member_2014 in ["y", "ya"]

#inut status kode romo (mengecek aakah user mengetik 'ya' atau 'y')
input_promo_2014 = input("apakah kode promo valid (y/t): ").strip().lower()
kode_promo_valid_2014 = input_promo_2014 in ["y", "ya"]

total_diskon_persen_2014 = 0

#mult if terpisah: setia kondisi dieriksa secara indeenden
#diskon bisa di tumuk jika

if total_belanja_2014 > 1000000:
    total_diskon_persen_2014 += 10 #diskon belanja besar

if is_member_2014:
    total_diskon_persen_2014 += 5 #diskon member

if kode_promo_valid_2014:
    total_diskon_persen_2014 += 15 #diskon voucher

#menghitung nominal diskon dan total bayar
nominal_diskon_2014 = total_belanja_2014 * (total_diskon_persen_2014 / 100)
total_bayar_2014 = total_belanja_2014 - nominal_diskon_2014

# output hasil
print("\n--- Rincian pembayaran ---")
print(f"total diskon : {total_diskon_persen_2014}% (Rp {nominal_diskon_2014:,.0f})")
print(f"total bayar : Rp {total_bayar_2014:,.0f})")

print(f"total diskon yang anda dapatkan: {total_diskon_persen_2014}%")
#output: total diskon yang anda daatkan: 30% jika belanja > 1 juta, member, dan kode promo valid




































