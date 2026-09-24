# Input dari user
total_belanja_3016 = float(input("Masukkan total belanja (Rp) :"))

# Input stsatus member (Mengecek apakah user mengetik 'y' atau 'ya')
input_member_3016 = input("Apakah Anda Member? (y/t) : ").strip().lower()
is_member_3016 = input_member_3016 in ["y", "ya"]

# Input status kode promo (Mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3016 = input("Apakah kode promo valid (y/t) : ").strip().lower()
kode_promo_valid_3016 = input_promo_3016 in ["y", "ya"]

total_diskon_persen_3016 = 0

# Multi if terpisah : setiap kodisi diperiksa secara independen
# Diskon bisa ditumpuk (Akumulasi) jika memenuhi beberap syarat sekaligus

if total_belanja_3016 > 1000000 :
    total_diskon_persen_3016 += 10 #Diskon belanja besar

if is_member_3016 :
    total_diskon_persen_3016 += 5 # Diskon member

if kode_promo_valid_3016 :
    total_diskon_persen_3016 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_3016 = total_belanja_3016 * (total_diskon_persen_3016 / 100)
total_bayar_3016 = total_belanja_3016 - nominal_diskon_3016

# output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total diskon : {total_diskon_persen_3016}% (Rp{nominal_diskon_3016:,.0f})")
print(f"Total bayar  : Rp {total_bayar_3016:,.0f}")

print(f"Total diskon yang anda dapatkan : {total_diskon_persen_3016}%")
# Ouput : Total  diskon yang anda dapatkan 305 jika belanja > 1 juta, member, dan kode promo valid