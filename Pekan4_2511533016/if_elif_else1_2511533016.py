umur_3016 = int(input("Input umur anda :"))
sim_3016 = input("Apakah anda sudah punya Sim C (y/t) : ")[0]

if umur_3016 >= 17 and sim_3016 == 'y' :
    print("Anda sudah dewasa dan boleh bawa motor")
elif umur_3016 >= 17 and sim_3016 != 'y' :
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_3016 < 17 and sim_3016 == 'y' :
    print("Anda belum cukup umur punya sim")
else :
    print("Anda Belum cukup umur dan tidak boleh bawa motor")
print("Program selesai")

