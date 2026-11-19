# Buat file denhgan nama assigment_2511533016.py
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()
# Nilai yang di masukkan akan di konversi menjadi tipe data integer
# Program operator assigment dalam python

angka1_3016 = int(input("Input angka-1: "))
angka2_3016 = int(input("Input angka-2: "))

print("\nNilai awal angkat1 =", angka1_3016)
print("Nilai angka2 =", angka2_3016)

# Assigment biasa 
hasil_3016 = angka1_3016
print("\nAssigment biasa(=)")
print("hasil =", hasil_3016)

# Assigment Penambahan
hasil_3016 = angka1_3016
hasil_3016 += angka2_3016
print("\nAssigment penambahan(+=)")
print("hasil =", hasil_3016)

# Assigment Pengurangan
hasil_3016 = angka1_3016
hasil_3016 -= angka2_3016
print("\nAssigment pengurangan(-=)")
print("hasil =", hasil_3016) 

# Assigment Perkalian
hasil_3016 = angka1_3016
hasil_3016 *= angka2_3016
print("\nAssigment perkalian(*=)")
print("hasil =", hasil_3016)

# Assigment pembagian, pembagian bulat dan sisa bagi
if angka2_3016 !=0:
    hasil_3016 = angka1_3016
    hasil_3016 /= angka2_3016
    print("\nAssigment pembagian(/=)")
    print("hasil =", hasil_3016)
    # Operator tambahan
    hasil_3016 = angka1_3016
    hasil_3016 //= angka2_3016
    print("\nAssigment pembagian bulat(//=)")
    print("hasil =", hasil_3016)
    hasil_3016 = angka1_3016
    hasil_3016 %= angka2_3016
    print("\nAssigment sisa bagi (%=)")
    print("Hasi =", hasil_3016)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0")

# Operator tambahan: assigment perpankatan
hasil_3016 = angka1_3016
hasil_3016 **= angka2_3016
print("\nAssigment perpangkatan(**=)")
print("hasil =", hasil_3016)