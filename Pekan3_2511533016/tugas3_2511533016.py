nama_3016 = input("Nama Pelanggan : ")
status_3016 = input("Masukkan Status Pelanggan (member/nonmember) : ").strip().lower()
total_3016 = int(input("Masukkan Total Belanja : "))
jumlah_3016 = int(input("Masukkan jumlah barang : "))
promo_3016 = input("Masukkan Kode Promo : ").strip().upper()

print("=== SISTEM TRANSAKSI TOKO ===\n")
print("Masukkan Nama Pelanggan : ", nama_3016)
print("Masukkan Stats Pelanggann : ", status_3016)
print("Masukkan Total Belanja : ", total_3016)
print("Masukkan Jumlah Barang : ", jumlah_3016)
print("Masukkan kode Promo : ", promo_3016)

syaratDiskon_3016 = total_3016 >= 200000
syaratJumlah_3016 = jumlah_3016 >= 3

daftarPromo_3016 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
promoTersedia_3016 = promo_3016 in daftarPromo_3016
promoTidakTersedia_3016 = promo_3016 not in daftarPromo_3016 
statusMember_3016 = status_3016 == "member"
bukanMember_3016 = not statusMember_3016
diskonKhusus_3016 = (syaratJumlah_3016 or syaratDiskon_3016) and statusMember_3016
diskonPromo_3016 = (syaratJumlah_3016 or syaratDiskon_3016) and promoTersedia_3016 

diskon_3016 = total_3016 * 0.15 if diskonKhusus_3016 else 0
rata_3016 = total_3016 / jumlah_3016 

totalPembayaran_3016 = total_3016
totalPembayaran_3016 -= diskon_3016

dataPelanggan_3016 = [nama_3016, status_3016, total_3016]
dataPelanggan2_3016 = dataPelanggan_3016
dataPelanggan3_3016 = dataPelanggan_3016.copy()

identitasSama_3016 = dataPelanggan_3016 is dataPelanggan2_3016
identitasBerbeda_3016 = dataPelanggan_3016 is not dataPelanggan3_3016
nilaiSama_3016 = dataPelanggan_3016 == dataPelanggan3_3016     

bitMember_3016 = 0b0001 if statusMember_3016 else 0b0000
bitBelanja_3016 = 0b0010 if syaratDiskon_3016 else 0b0000
bitJumlah_3016 = 0b0100 if syaratJumlah_3016 else 0b0000
bitPromo_3016 = 0b1000 if promoTersedia_3016 else 0b0000

kodeStatus_3016 = bitMember_3016 | bitBelanja_3016 | bitJumlah_3016 | bitPromo_3016
cekMember_3016 = kodeStatus_3016 & 0b0001
cekPromo_3016 = kodeStatus_3016 & 0b1000
kodeReferensi_3016 = 0b1011
hasilXor_3016 = kodeStatus_3016 ^ kodeReferensi_3016
hasilShift_3016 = kodeStatus_3016 << 1

memberAccess_3016 = bool(kodeStatus_3016 & 0b0001)
promoAccess_3016 = bool(kodeStatus_3016 & 0b1000)
freeShippingAccess_3016 = promo_3016 == "GRATISONGKIR" and promoTersedia_3016

print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000        :", syaratDiskon_3016)
print("Jumlah Barang >= 3         :", syaratJumlah_3016)
print("Status Member              :", statusMember_3016)
print("Kode Promo Tersedia        :", promoTersedia_3016)
print("Mendapatkan Diskon         :", diskonKhusus_3016)
print("Mendapatkan Promo          :", promoTersedia_3016)

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon                     : Rp", int(diskon_3016))
print("Total Pembayaran           : Rp", int(totalPembayaran_3016))
print("Rata-rata Harga Barang     : Rp", round(rata_3016, 2))

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses             :", format(kodeStatus_3016, "04b"))
print("Member Access              :", memberAccess_3016)
print("Promo Access               :", promoAccess_3016)
print("Free Shipping Access       :", freeShippingAccess_3016)

print("\n=== OPERASI BITWISE ===")
print("Kode Status Transaksi")
print("0001 | 0010 | 0100 | 1000")
print("Kode Biner   :", format(kodeStatus_3016, "04b"))
print("Kode Desimal :", kodeStatus_3016)

print("\nCek Member")
print(format(kodeStatus_3016, "04b"), "& 0001")
print("Hasil Biner   :", format(cekMember_3016, "04b"))
print("Hasil Desimal :", cekMember_3016)

print("\nCek Promo")
print(format(kodeStatus_3016, "04b"), "& 1000")
print("Hasil Biner   :", format(cekPromo_3016, "04b"))
print("Hasil Desimal :", cekPromo_3016)

print("\nPerbandingan Status")
print("Kode Transaksi :", format(kodeStatus_3016, "04b"))
print("Kode Referensi :", format(kodeReferensi_3016, "04b"))
print(format(kodeStatus_3016, "04b"), "^", format(kodeReferensi_3016, "04b"))
print("Hasil Biner   :", format(hasilXor_3016, "04b"))
print("Hasil Desimal :", hasilXor_3016)

print("\nGeser Kiri (Shift)")
print(format(kodeStatus_3016, "04b"), "<< 1")
print("Hasil Biner   :", format(hasilShift_3016, "05b"))
print("Hasil Desimal :", hasilShift_3016)

print("\n=== OPERATOR KEANGGOTAAN & IDENTITAS ===")
print("Promo tersedia (in)        :", promoTersedia_3016)
print("Promo tidak tersedia (not in) :", promoTidakTersedia_3016)
print("data_pelanggan is data_pelanggan2 :", identitasSama_3016)
print("data_pelanggan is not data_pelanggan3 :", identitasBerbeda_3016)
print("data_pelanggan == data_pelanggan3 :", nilaiSama_3016)

print("\n=== SELESAI ===")