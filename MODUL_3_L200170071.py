m1 = [[2,3],[4,5]]
m2 = [[10,20],[5,6]]
#NOMER 1A#
def cekMat(matrix):
    """memastikan type data Integer"""
    jum = len(matrix)
    hasil = ""
    for x in matrix:
        for i in x:
            assert isinstance(i, int),"Harus Integer"
        return True
    
#NOMER 1B#
def Ukuran(matrix):
    """Mengambil ukuran matriks"""
    return("Ukuran Matrix = "+str(len(matrix))+" x "+str(len(matrix[0])))

#NOMER 1C#
def Jumlah(matrix1,matrix2):
    """Penjumlahan 2 Matrix"""
    if Ukuran(matrix1) == Ukuran(matrix2):
        for x in range(0, len(matrix1)):
            for y in range(0, len(matrix1[0])):
                print(matrix1[x][y] + matrix2[x][y], end=' '),
            print()
    else:
        print("Matriks Tidak Sesuai")
        
#NOMER 1D#
def Kali(matrix1,matrix2):
    """Perkalian 2 Matrix"""
    mat3 = []
    if Ukuran(matrix1) == Ukuran(matrix2):
        for x in range(0, len(matrix1)):
            row = []
            for y in range(0, len(matrix1[0])):
                total = 0
                for z in range(0, len(matrix1)):
                    total = total + (matrix1[x][z] * matrix2[z][y])
                row.append(total)
            mat3.append(row)

        for x in range(0, len(mat3)):
            for y in range(0, len(mat3[0])):
                print(mat3[x][y], end=' ')
            print()
    else:
        print("Matriks Tidak Sesuai")
def determinan(matrix):
    """Menghitung Determinan Matrix"""
    if len(matrix) == len(matrix[0]):
        bil = [x for x in range(len(matrix))]
        jum = 0
        for i in range(len(matrix)):
            total = 1
            for x in range(len(matrix)):
                total *= matrix[x][bil[x]]
            bil += [bil.pop(0)]
            jum += total
        bil2 = [x for x in range(len(matrix))]
        bil.reverse()
        jum2 = 0
        for i in range(len(matrix)):
            total2 = 1
            for x in range(len(matrix)):
                total2 *= matrix[x][bil2[x]]
            bil2 += [bil2.pop()]
            jum2 += total2
        print(total-total2)
        return ""
    else:
        print("Matriks Harus Bujursangkar")

#CEK NOMER 1#
print(cekMat(m1))
print(Ukuran(m1))
Jumlah(m1,m2)
Kali(m1,m2)
print(determinan(m1))

#NOMER 2A#
def buatNol(m, n):
    """Menggunakan dua input"""
    matrix = [[0 for x in range(m)] for i in range(n)]
    print(matrix)

def buatNol2(m):
    """Menggunakan satu input"""
    n = m
    matrix = [[0 for x in range(m)] for i in range(n)]
    print(matrix)

#NOMER 2B#
def buatIdentitas(m):
    n = m
    matrix = [[1 if j == i else 0 for j in range(m)]for i in range(n)]
    print(matrix)

#CEK NOMER 2#
buatNol(3,3)
buatNol2(3)
buatIdentitas(4)

#NOMER 3#
class Node():
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode
    def cetak(head):
        curr = head
        while curr != None:
            print(curr.data)
            curr = curr.nextNode

    def cari(head, cari):
        curr = head
        while curr != None:
            if curr.data == cari:
                print("Data ditemukan!")
            else:
                print("Check data!")
            curr = curr.nextNode
    def tambahDepan(head):
        newNode = Node(1)
        newNode.nextNode = head
        head = newNode
        return head
    def tambahAkhir(head):
        curr = head
        while curr is not None:
            if curr.nextNode == None:
                newNode = Node(25)
                curr.nextNode = newNode
                return curr
            else:
                pass
            curr = curr.nextNode
        return curr
    def tambah(head, posisi):
        newNode = Node(8)
        newNode.nextNode = posisi.nextNode
        posisi.nextNode = newNode
        head.head = posisi
        return head
    def hapus(head, posisi):
        curr = head
        while curr != None:
            if curr.nextNode.data == posisi:
                curr.nextNode = curr.nextNode.nextNode
                return curr
            else:
                pass
            curr = curr.nextNode
        return curr

#NOMER 4#
class doubly_linked():
    def __init__(self, Data, Next=None, Prev=None):
        self.Data = Data
        self.Next = Next
        self.Prev = Prev

    def mencetak():
        curr = head
        while curr != None:
            print(curr.Data)
            if curr.Next == None:
                curr = curr
                break
            else:
                curr = curr.Next
        print("\n")
        while curr != None:
            print(curr.Data)
            curr = curr.Prev
    def simpulAwal(head):
        newNode = doubly_linked(25)
        newNode.Next = head
        head.Prev = newNode
        head =newNode
        return head

    def simpulAkhir(head):
        curr = head
        while curr != None:
            if curr.Next == None:
                newNode = doubly_linked(365)
                curr.Next = newNode
                newNode.Prev = curr
                return curr
            else:
                pass
            curr = curr.Next
        return curr
