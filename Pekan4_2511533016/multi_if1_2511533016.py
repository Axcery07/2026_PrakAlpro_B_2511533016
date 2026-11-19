umur_3016 = int(input("Input umur anda :"))
sim_3016 = input("Apakah anda sudah punya Sim C (y/t) : ")[0]

if umur_3016 >= 17 and sim_3016 == 'y' :
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_3016 >= 17 and sim_3016 != 'y' :
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_3016 < 17 and sim_3016 == 'y' :
    print("Anda belum cukup umur punya sim")

if umur_3016 < 17 and sim_3016 != 'y' :
    print("Anda belum cukup umur bawa motor")

