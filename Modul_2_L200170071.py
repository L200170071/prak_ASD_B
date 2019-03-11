#1
class Pesan(object):

    #a
    def __init__(self, kata):
        self.kata = kata

    def apakahTerkandung(self, yo):
        if yo in self.kata:
            return True
        else:
            return False

    #b
    def hitungKonsonan(self):
        vokal = 'AIUEOaiueo'
        v = 0
        for x in self.kata:
            if x in vokal:
                v+=1
        kon = len(self.kata) - v
        return kon

    #c 
    def hitungVokal(self):
        vokal = 'AIUEOaiueo'
        v = 0
        for x in self.kata:
            if x in vokal:
                v+=1
        return v

#2
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan nasi', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan Sepak Bola', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


class Mahasiswa(Manusia):
    """Class yang dibangun dari class Mahasiswa"""

    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nim = NIM
        self.kota = kota
        self.us = us
    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.us
    def tambahUangSaku(self, tambahUang):
        self.us = self.us + tambahUang
    def ambilKotaTinggal(self):
        return self.kota
    def perbaruiKotaTinggal(self, kotabaru):
        self.kota = kotabaru
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau sambil belajar ."""
        print("Saya baru saja makan",s,"sambil belajar")
        self.keadaan = 'kenyang'

m1 = Mahasiswa('Jamil', 234, 'Surakarta', 250000)
m2 = Mahasiswa('Andi', 365, 'Magelang', 275000)
m3 = Mahasiswa('Sri', 676, 'Yogyakarta', 240000)

#3
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan nasi', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan sSepak Bola', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


class Mahasiswa(Manusia):
    """Class yang dibangun dari class Mahasiswa"""

    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nim = NIM
        self.kota = kota
        self.us = us
        
    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s
    
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.us
    def tambahUangSaku(self, tambahUang):
        self.us = self.us + tambahUang
    def ambilKotaTinggal(self):
        return self.kota
    def perbaruiKotaTinggal(self, kotabaru):
        self.kota = kotabaru
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau sambil belajar ."""
        print("Saya baru saja makan",s,"sambil belajar")
        self.keadaan = 'kenyang'

a = input("Masukkan nama: ")
b = input("Masukkan nim: ")
c = input("Masukkan kota tinggal: ")
d = input("Masukkan uang saku: ")

x = Mahasiswa(a,b,c,d)
print (x)

#4
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan nasi', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan sepak bola', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


class Mahasiswa(Manusia):
    """Class yang dibangun dari class Mahasiswa"""

    def __init__(self, nama, NIM, kota, us, lk = []):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nim = NIM
        self.kota = kota
        self.us = us
        self.listkuliah = lk

    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s
    
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.us
    def tambahUangSaku(self, tambahUang):
        self.us = self.us + tambahUang
    def ambilKotaTinggal(self):
        return self.kota
    def perbaruiKotaTinggal(self, kotabaru):
        self.kota = kotabaru
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau sambil belajar ."""
        print("Saya baru saja makan",s,"sambil belajar")
        self.keadaan = 'kenyang'
    def ambilKuliah(self, ambil):
        self.listkuliah.append(ambil)

m1 = Mahasiswa('Jamil', 234, 'Surakarta', 250000)
m2 = Mahasiswa('Andi', 365, 'Magelang', 275000)
m3 = Mahasiswa('Sri', 676, 'Yogyakarta', 240000)

#5
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan nasi', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan sepak bola', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


class Mahasiswa(Manusia):
    """Class yang dibangun dari class Mahasiswa"""

    def __init__(self, nama, NIM, kota, us, lk = []):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nim = NIM
        self.kota = kota
        self.us = us
        self.listkuliah = lk

    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s
    
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.us
    def tambahUangSaku(self, tambahUang):
        self.us = self.us + tambahUang
    def ambilKotaTinggal(self):
        return self.kota
    def perbaruiKotaTinggal(self, kotabaru):
        self.kota = kotabaru
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau sambil belajar ."""
        print("Saya baru saja makan",s,"sambil belajar")
        self.keadaan = 'kenyang'
    def ambilKuliah(self, ambil):
        self.listkuliah.append(ambil)
    def hapusListKuliah(self, hapus):
        for x in self.listkuliah:
            if hapus in self.listkuliah:
                self.listkuliah.remove(hapus)
            else:
                print("Maaf mata kuliah tidak ada dalam list mata kuliah yang diambil")

m1 = Mahasiswa('Jamil', 234, 'Surakarta', 250000)
m2 = Mahasiswa('Andi', 365, 'Magelang', 275000)
m3 = Mahasiswa('Sri', 676, 'Yogyakarta', 240000)

#6
from datetime import date
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2

class SiswaSMA(Manusia):
    def __init__(self, nama, NIS, umur, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nis = NIS
        self.umur = umur
        self.us = us
        
    def __str__(self):
        s = self.nama +', NIS '+str(self.nis)\
            +'. Berumur '+ str(self.umur) \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap harinya.'
        return s

    def tahunlahir(self):
        thnskr = date.today().year
        tl = thnskr - self.umur
        return tl
