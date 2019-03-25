#no.1

class MhsTIF(object):
    def __init__(self, nama, no, kota, us):
        self.nama = nama
        self.no = no
        self.kota = kota
        self.uangSaku = us

c0 = MhsTIF('Ika', 10, 'Sukoharjo', 2400000)
c1 = MhsTIF('Budi', 51, 'Sragen', 2300000)
c2 = MhsTIF('Ahmad', 2, 'Surakarta', 2500000)
c3 = MhsTIF('Chandra', 18, 'Surakarta', 235000)
c4 = MhsTIF('Eka', 4, 'Boyolali', 2400000)
c5 = MhsTIF('Fandi', 31, 'Salatiga', 2500000)
c6 = MhsTIF('Deni', 13, 'Klaten', 2450000)
c7 = MhsTIF('Galuh', 5, 'Wonogiri', 2450000)
c8 = MhsTIF('Janto', 23, 'Klaten', 2450000)
c9 = MhsTIF('Hasan', 64, 'Karanganyar', 2700000)
c10 = MhsTIF('Khalid', 29, 'Purwodadi', 2650000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def cari(list, target):
    a = []
    for i in list :
        if i.kota == target:
            a.append(list.index(i))
    return a
