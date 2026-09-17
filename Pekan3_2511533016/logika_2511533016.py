# Buat file dengan nama logika_2511533016.py
# Nama variabel diambah 4 digit nim terakhit
# Program ini menggunakan fungsi input()
# Program operator logika dalam python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_3016 = input("Input nilai boolean 1 (True/False): ").strip().lower() == "true" 
a2_3016 = input("Input nilai boolean 2 (True/False): ").strip().lower() == "true"

print("\nA1 = ", a1_3016)
print("A2 = ", a2_3016)

# Konjungsi : bernilai true jika kedunya true
hasil_3016 = a1_3016 and a2_3016
print("\nOperator Konjungsi (AND)")
print("Hasil = ", hasil_3016)

# Disjungsi : bernilai true jika salah satu true
hasil_3016 = a1_3016 or a2_3016
print("\nOperator Disjungsi (OR)")
print("Hasil = ", hasil_3016)

# Negasi A1: membalik nilai A1
hasil_3016 = not a1_3016
print("\nNegasi A! (NOT) : ", hasil_3016)
print("not A! = ", hasil_3016)

# Negasi A2 : membalik nilai A2
hasil_3016 = not a2_3016
print("\nNegasi A2 (NOT)")
print("not A2 = ", hasil_3016)

# XOR : bernilai trus jika kedua nilai berbeda
hasil_3016 = a1_3016 != a2_3016
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =" , hasil_3016)