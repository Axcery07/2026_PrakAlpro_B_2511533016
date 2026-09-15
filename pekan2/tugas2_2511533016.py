from typing import Final

BATAS_LULUS: Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_3016 = input("Masukkan Nama Mahasiswa : ")

jk_3016 = input("Masukkan Jenis Kelamin (L/P): ")

alamat_3016 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""

umur_3016 = int(input("Masukkan Umur : "))

skor_3016 = float(input("Masukkan Skor Tes Awal : "))

token_3016 = 100 + 3j

lulus_3016 = skor_3016 >= BATAS_LULUS

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa : {nama_3016} | Tipe: {type(nama_3016)}")
print(f"Jenis Kelamin : {jk_3016} | Tipe: {type(jk_3016)}")
print(f"Alamat Domisili:\n{alamat_3016} | Tipe: {type(alamat_3016)}")
print(f"Umur : {umur_3016} tahun | Tipe: {type(umur_3016)}")
print(f"Skor Tes Awal : {skor_3016} | Tipe: {type(skor_3016)}")
print(f"ID Token Sinyal: {token_3016} | Tipe: {type(token_3016)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai: {BATAS_LULUS}")
print(f"Apakah Dinyatakan Lulus?: {lulus_3016} | Tipe: {type(lulus_3016)}")