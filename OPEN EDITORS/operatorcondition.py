#Luas dan keliling Jajar Genjang
print ("Program menghitung keliling dan Jajargenjang")
a =int(input("Masukan Alasnya    ="))
t =int(input("Masukan Tingginya  ="))
sa =int(input("Masukan Sisi 1    ="))
sb =int(input("Masukan Sisi 2    ="))

luas = a*t
keliling =2* (sa+sb)

print("Luas Jajargenjang adalah    =", luas)
print("Keliling Jajargenjang adalah    =", keliling)

#Mengubah sudu dari Fahreinheit ke Celcius dan Reamur
f =int(input("Fahreinheit ="))
c = (f - 32) * 5/9
r = (f - 32) * 4/9

print("Celcius =", c)
print("Reamur=", r)

#Hitung tinggi dan berat badan ideal
t = int(input("tinggi badan ="))
b = t - 110

print("berat badan ideal kamu adalah", b)