tinggi_3016 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3016 % 2 != 0:
    print("Tinggi pola harus bilangan genap.")
else :
    a_3016 = tinggi_3016 
    c_3016 = a_3016 
    lebar_3016 = (2 * tinggi_3016) - 2

    for i_3016 in range(1, tinggi_3016 + 1):
        b_3016 = c_3016 + 1

        for j_3016 in range(1, lebar_3016 + 1):

            # Baris atas dan bawah
            if i_3016 == 1 or i_3016 == tinggi_3016:
                if j_3016 == 1 or j_3016 == lebar_3016:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_3016 == 1 or j_3016 == lebar_3016:
                    print("|", end="")
                else :
                    if j_3016 == c_3016:
                        print("<", end="")
                    elif j_3016 == b_3016:
                        print(">", end="")
                    elif j_3016 == (lebar_3016 - c_3016):
                        print("<", end="")
                    elif j_3016 == (lebar_3016 - c_3016 + 1):
                        print(">", end="")
                    elif j_3016 > b_3016 and j_3016 < (lebar_3016 - c_3016):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_3016 -= 2

        if a_3016 <= 0:
            c_3016 = (-a_3016) + 2
        else:
            c_3016 = a_3016