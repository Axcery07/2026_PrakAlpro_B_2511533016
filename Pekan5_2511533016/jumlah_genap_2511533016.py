ulang_3016 = int(input("Masukkan jumlah perulangan: "))

jumlah_3016 = 0
for i_3016 in range(ulang_3016 + 1):
    if i_3016 % 2 == 0:
        print(i_3016, end=" ")
        jumlah_3016 = jumlah_3016 + i_3016

        if i_3016 < ulang_3016:
            print("+", end=" ")
        else:
            print("=", jumlah_3016, end=" ")
print()
print("Jumlah =", jumlah_3016)