#no.2

class MhsTIF(object):
    """docstring for MhsTIF"""
    def __init__(self, nama, nim, kota, uangS):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = uangS

class my_Array(object):
    """docstring for bikinArray"""
    def __init__(self):
        self.index = 11*[None]
    def __getitem__(self, item):
        getData = self.index[item]
        return getData
    def __setitem__(self, key, value):
        self.index[key] = value

c = my_Array()

c[0] = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c[1] = MhsTIF("Budi", 51, "Sragen", 230000)
c[2] = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c[3] = MhsTIF("Candra", 18, "Surakarta", 235000)
c[4] = MhsTIF("Eka", 4, "Boyolali", 240000)
c[5] = MhsTIF("Fandi", 31, "Salatiga", 250000)
c[6] = MhsTIF("Deni", 13, "Klaten", 245000)
c[7] = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c[8] = MhsTIF("Janto", 23, "Klaten", 245000)
c[9] = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c[10] = MhsTIF("Khalid", 29, "Purwodadi", 210000)

def cariUangKecil():
    final = [None,None]
    sebelum = 0
    x = 0
    l = len(c.index) - 1
    while x <= l:
        try:
            sebelum = c[x]
            nexta = x + 1
            if sebelum.uangSaku <= c[nexta].uangSaku:
                sebelum = c[x]
                final[0] = c[x].nama
                final[1] = c[x].uangSaku
            x += 1
        except IndexError:
            break	
    return final
