print("==================================================")
print("3. OPERATOR BITSIWE")
print("==================================================")

angka1_3016 = int(input("Masukkan angkat bitwise 1: "))
angka2_3016 = int(input("Masukkan angkat bitwise 2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 = ", angka1_3016, "| biner = ", bin(angka1_3016))
print("angka2 = ", angka2_3016, "| biner = ", bin(angka2_3016))

# Bitwise AND
hasil_3016 = angka1_3016 & angka2_3016
print("\nBitwise AND(&)")
print(angka1_3016, "&", angka2_3016, "=", hasil_3016)
print("Biner hasil =", bin(hasil_3016))
print("Biner hasil (8 bit) = ", format(hasil_3016, "08b"))

# Bitwise OR
hasil_3016 = angka1_3016 | angka2_3016
print("\nBitwise OR(|)")
print(angka1_3016, "|", angka2_3016, "=", hasil_3016)
print("Biner hasil =", bin(hasil_3016))
print("Biner hasil (8 bit) = ", format(hasil_3016, "08b"))

# Bitwise XOR
hasil_3016 = angka1_3016 ^ angka2_3016
print("\nBitwise XOR(^)")
print(angka1_3016, "^", angka2_3016, "=", hasil_3016)
print("Biner hasil =", bin(hasil_3016))
print("Biner hasil (8 bit) = ", format(hasil_3016, "08b"))

# Bitwise NOT
hasil_3016 = ~angka1_3016
print("\nBitwise NOT(~)")
print("~", angka1_3016, "=", hasil_3016)
print("Biner hasil =", bin(hasil_3016))
print("Biner hasil (8 bit) = ", format(hasil_3016, "08b"))

# Bitwise geser kiri
jumlah_geser_3016 = int(input("\nMasukkan jumlah pergeseran bit : "))

hasil_3016 = angka1_3016 << jumlah_geser_3016
print("\nBitwise geser kiri(<<)")
print(angka1_3016, "<<", jumlah_geser_3016, "=", hasil_3016)
print("Biner hasil =", bin(hasil_3016))
print("Biner hasil (8 bit) = ", format(hasil_3016, "08b"))

# Bitwise geser kanan
jumlah_geser_3016 = int(input("\nMasukkan jumlah pergeseran bit : "))

hasil_3016 = angka1_3016 << jumlah_geser_3016
print("\nBitwise geser kanan(>>)")
print(angka1_3016, ">>", angka2_3016, "=", hasil_3016)
print("Biner hasil =", bin(hasil_3016))
print("Biner hasil (8 bit) = ", format(hasil_3016, "08b"))