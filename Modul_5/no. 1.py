class MhsTIF():
    def __init__(self, nim):
        self.nim = nim

    def __str__(self):
        return str(self.nim)
    
c0 = MhsTIF(10)
c1 = MhsTIF(51)
c2 = MhsTIF(2)
c3 = MhsTIF(18)
c4 = MhsTIF(4)
c5 = MhsTIF(31)
c6 = MhsTIF(13)
c7 = MhsTIF(5)
c8 = MhsTIF(23)
c9 = MhsTIF(64)
c10 = MhsTIF(29)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp


#No. 1
def bubbleSort():
    n = len(Daftar)
    for i in range (n-1):
        for j in range (n-i-1):
            if Daftar[j].nim > Daftar[j+1].nim:
                swap(Daftar,j,j+1)
    Daftar2 = [Daftar[0].nim, Daftar[1].nim, Daftar[2].nim, Daftar[3].nim, Daftar[4].nim, Daftar[5].nim, Daftar[6].nim, Daftar[7].nim, Daftar[8].nim, Daftar[9].nim, Daftar[10].nim]
    print (Daftar2)


#No. 2
A = [1, 3, 5, 7, 9]
B = [2, 4, 6, 8, 10]
C = []

def gabung():
    C.extend(A)
    C.extend(B)
    n = len(C)
    for i in range (n-1):
        for j in range (n-i-1):
            if C[j] > C[j+1]:
                swap(C,j,j+1)
    print (C)


