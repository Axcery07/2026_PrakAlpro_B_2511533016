print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

nama_3016         = input("Masukkan Nama Pengunjung        : ")
umur_3016         = int(input("Input umur anda                 : "))
sim_3016          = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()

print()
print("Pilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_3016        = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_3016 = int(input("Masukkan jumlah tiket           : "))
is_member_3016    = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_3016   = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

if jumlah_tiket_3016 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")

match paket_3016:
    case 1:
        nama_wahana_3016  = "Wahana Safari Rimba"
        harga_satuan_3016 = 50_000
    case 2:
        nama_wahana_3016  = "Wahana Arung Jeram"
        harga_satuan_3016 = 75_000
    case 3:
        nama_wahana_3016  = "Wahana Motor ATV Ekstrim"
        harga_satuan_3016 = 120_000
    case 4:
        nama_wahana_3016  = "Wahana Roller Coaster Kilat"
        harga_satuan_3016 = 100_000
    case 5:
        nama_wahana_3016  = "Wahana All-Access VIP"
        harga_satuan_3016 = 220_000
    case _:
        print("Paket wahana tidak valid!")
        exit()

print()
print("--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_3016 == 3:
    if umur_3016 >= 17 and sim_3016 == 'y':
        status_akses_3016 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
    elif umur_3016 >= 17 and sim_3016 != 'y':
        status_akses_3016 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."
    elif umur_3016 < 17 and sim_3016 == 'y':
        status_akses_3016 = "Identitas tidak valid: Belum cukup umur memiliki SIM."
    else:
        status_akses_3016 = "Anda belum cukup umur dan tidak boleh bawa motor ATV."
else:
    if umur_3016 >= 10:
        status_akses_3016 = "Anda memenuhi syarat usia minimum untuk wahana ini."
    else:
        status_akses_3016 = "Maaf, usia Anda belum memenuhi syarat minimum (10 tahun)."

print(f"Status Akses: {status_akses_3016}")

subtotal_3016          = harga_satuan_3016 * jumlah_tiket_3016
total_diskon_persen_3016 = 0

if subtotal_3016 >= 200_000:
    total_diskon_persen_3016 += 10    # Diskon Belanja Besar

if is_member_3016 in ['y', 'ya']:
    total_diskon_persen_3016 += 5     # Diskon Member

if kode_promo_3016 in ['y', 'ya']:
    total_diskon_persen_3016 += 15    # Diskon Voucher Promo

if jumlah_tiket_3016 >= 5:
    total_diskon_persen_3016 += 5     # Diskon Tambahan Rombongan

nominal_diskon_3016 = subtotal_3016 * (total_diskon_persen_3016 / 100)
total_bayar_3016    = subtotal_3016 - nominal_diskon_3016

if total_bayar_3016 > 300_000:
    catatan_3016 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_3016 = "Terima kasih telah berkunjung."

print()
print("--- Rincian Pembayaran ---")
print(f"Nama Pengunjung  : {nama_3016}")
print(f"Wahana Dipilih   : {nama_wahana_3016}")
print(f"Subtotal Belanja : Rp {subtotal_3016:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_3016}% (Rp {nominal_diskon_3016:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_3016:,.0f}")
print(f"Catatan Layanan  : {catatan_3016}")
print("Program Selesai")