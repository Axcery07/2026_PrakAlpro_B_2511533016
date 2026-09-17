# Buat file dengan nama aritmatika_2511533016.py
# Buat program untuk operator aritmatika dala, python
# Nama variabel ditambah 4 digit nim terakhit 
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_3016 = int(input("Input angka 1: "))
angka2_3016 = int(input("Input angka 2: "))

# Penjumlahan
hasil_3016 = angka1_3016 + angka2_3016
print("\nOperator Penjumlahan")
print("Hasil = ", hasil_3016)

# Pengurangan
hasil_3016 = angka1_3016 - angka2_3016
print("\nOperator Pengurangan")
print("Hasil = ", hasil_3016) 

# Perkalian
hasil_3016 = angka1_3016 * angka2_3016
print("\nOperator Perkalian")
print("Hasil = ", hasil_3016)

# Pembagian pembagian bulat, dan sisa bagi
if angka2_3016 != 0:
    hasil_3016 = angka1_3016 / angka2_3016
    print("\nOperator Pembagian")
    print("Hasil = ", hasil_3016)

    hasil_3016 = angka1_3016 // angka2_3016
    print("\nOperator Pembagian Bulat")
    print("Hasil = ", hasil_3016)

    hasil_3016 = angka1_3016 % angka2_3016
    print("\nOperator Sisa Bagi")
    print("Hasil = ", hasil_3016)
else:
    print("Angka kedua tidak boleh bernilai 0")

# Pangkat   
hasil_3016 = angka1_3016 ** angka2_3016
print("\nOperator Pangkat")
print("Hasil = ", hasil_3016)
