#program untuk kondisional if

umur_2014 = int(input("Input Umur Anda: "))
sim_2014 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_2014 >= 17 and sim_2014 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_2014 >= 17 and sim_2014 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")
  
if umur_2014 < 17 and sim_2014 == 'y':
    print("Anda belum cukup umur punya sim")

if umur_2014 < 17 and sim_2014 != 'y':
    print("Anda belum cukup umur bawa motor")

     


















































