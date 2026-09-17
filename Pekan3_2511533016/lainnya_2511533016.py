print("=========================================")
print("1. OPERATOR KEANGGOTAAN")
print("=========================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3016 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3016 = [int(angka.strip()) for angka in input_data_3016.split]

nilai_dicari_3016 = int(input("Masukkan angka yang ingin dicari : "))

# Operator in
hasil_3016 = nilai_dicari_3016 in data_3016
print ("\nOperator keanggotaan IN")
print (nilai_dicari_3016, "in", data_3016, "=", hasil_3016)

# Operator not in
hasil_3016 = nilai_dicari_3016 not in data_3016
print ("\nOperator keanggotaan NOT IN")
print (nilai_dicari_3016, "not in", data_3016, "=", hasil_3016)

print("=========================================")
print("2. OPERATOR IDENTITAS")
print("=========================================")

# objek1 menggunakan list dari input pengguna
objek1_3016 = data_3016

# objek2 merujuk pada objek yabg sama dengan objek1
objek2_3016 = objek1_3016

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3016 = data_3016.copy()

print("objek1 = ", objek1_3016)
print("objek1 = ", objek2_3016)
print("objek1 = ", objek3_3016)

# Operator is
hasil_3016 = objek1_3016 is objek2_3016
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_3016)

# Membadingkan identitas dan nilai 
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_3016 is objek3_3016)
print("objek1 == objek3 =", objek1_3016 == objek3_3016)