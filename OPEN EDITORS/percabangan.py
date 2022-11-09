#SOAL NOMER.1 Permainan roller coster
#Input
nama = input ("Nama Lengkap = ")
umur = int(input ("Umur = "))
tinggi = int(input ("Tinggi = "))

#Output
print("Nama Lengkap",nama)
print("Umur",umur)
print("Tinggi ",tinggi)
if (tinggi >= 80):
    print("Anda Boleh bermain")
else :
    print("Anda Tidak Boleh Bermain")


#SOAL NO.2 Menghitung nilai
#input
nama = input("Nama Lengkap = ")
kelas = input("Kelas = ")
nilai = int(input("Nilai (max = 100) = "))

#output
print("Nama Lengkap = ", nama)
print("Kelas = ", kelas)
print("Nilai = ", nilai)
if(nilai > 89 and nilai < 101):
    print("Istimewa")
elif(nilai > 69 and nilai< 90):
    print("Sangat Bagus")
elif(nilai >59 and nilai < 70):
    print("Cukup")
else:
    print("Gagal")

#SOAL NO.3 Pratikum
#input
kondisi = input("Masukan kondisi lab (tersedia/penuh/tidak ada) = ")

#output
if(kondisi == "tersedia"):
    print("maka pratikum")
elif(kondisi == "penuh"):
    print("maka pindah jadwal")
elif(kondisi == "tidak ada"):
    print("maka tidak jadi pratikum")
else:
    print("error")