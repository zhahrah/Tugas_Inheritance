class Ibu(object):
    def __init__(self, nama, umur, tinggi, berat):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
        self.berat = berat 
  
    def memotong(self):
        print("memotong wortel dengan hati-hati")
      
    def menyapu(self):
        print("menyapu dengan hati yang gembira")
      
# class Anak turunan dari class Ibu
class Anak(Ibu):
    pass
  
I = Ibu("Ayu", 35, 165, 60)
print()
print("Nama:", I.nama)
print("Umur:", I.umur, "th")
print("Tinggi:", I.tinggi, "cm")
print("Berat:", I.berat, "kg")
I.memotong()
I.menyapu()

# objek dari class Anak memiliki seluruh yang dimiliki class Ibu
a = Anak("Fiqah", 19, 155, 50)
print()
print("Nama:", a.nama)
print("Umur:", a.umur, "th")
print("Tinggi:", a.tinggi, "cm")
print("Berat:", a.berat, "kg")
a.memotong()
a.menyapu()
