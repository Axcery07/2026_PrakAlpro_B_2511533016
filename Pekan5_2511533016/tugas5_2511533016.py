print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_3016 = int(input("Masukkan ukuran skala jam pasir (N): "))

print("#", end="")
for garis_3016 in range(4 * n_3016 + 5):
    print("=", end="")
print("#", end="")
print()

for baris_3016 in range(n_3016, 0, -1):
    print("| ", end="")

    for spasi_3016 in range(2 * (n_3016 - baris_3016)):
        print(" ", end="")

    for angka_3016 in range(baris_3016, 0, -1):
        print(angka_3016, end=" ")

    print("<*>", end="")

    for angka_3016 in range(1, baris_3016 + 1):
        print(" ", end="")
        print(angka_3016, end="")

    for spasi_3016 in range(2 * (n_3016 - baris_3016)):
        print(" ", end="")
    print(" |", end="")
    print()

print("|", end="")
for spasi_3016 in range(2 * n_3016 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_3016 in range(2 * n_3016 + 1):
    print(" ", end="")
print("|", end="")
print()

for baris_3016 in range(1, n_3016 + 1):
    print("| ", end="")
    for spasi_3016 in range(2 * (n_3016 - baris_3016)):
        print(" ", end="")
    for angka_3016 in range(baris_3016, 0, -1):
        print(angka_3016, end=" ")
    print("<*>", end="")
    for angka_3016 in range(1, baris_3016 + 1):
        print(" ", end="")
        print(angka_3016, end="")
    for spasi_3016 in range(2 * (n_3016 - baris_3016)):
        print(" ", end="")
    print(" |", end="")
    print()

print("#", end="")
for garis_3016 in range(4 * n_3016 + 5):
    print("=", end="")
print("#", end="")
print()