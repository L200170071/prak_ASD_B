#Nomor 1
class stack():
    def __init__(self):
        self.list = []
    def empty(self):
        return len (self.list) == 0
    def __len__ (self):
        return len (self.list)
    def push (self, data):
        self.list.append(data)
    def pop(self):
        assert not self.empty()
        return self.list.pop()

def cetakHeksa(angka):
    x = stack()

    if angka == 0:
        x.push(0)
    while angka != 0:
        sisa = angka % 16
        angka = angka // 16
        x.push(sisa)
    heksa = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    hasil = ''
    for i in range(len(x)):
        hasil += str(heksa[x.pop()])
    return hasil

#Nomor 2
class stuck():
    def __init__(self): #membuat stack kosong
        self.item = []
    def empty(self): #mengembalikan nilai boolean yang menunjukkan apakah stack itu kosong
        return len(self) == 0
    def __len__(self): #mengembalikan banyaknya item di stack
        return (self.item)
    def peek(self): #mengembalikan nilai posisi atas tanpa menghapus dan mengembalikan nilai dari item yang paling atas tanpa menghapus
        assert not self.empty()
        return self.item[-1]
    def pop(self): #mengembalikan nilai posisi atas lalu menghapus, stack kosong tidak dapat kosong
        assert not self.empty()
        return self.item.pop()
    def push(self, data): #mendorong item ke stack, menambah item ke puncak stack
        self.item.append(data)

a = stack()
a.push(3)
a.push(9)
a.push(5)
a.push(1)

print (a.pop())
print (a.pop())
print (a.pop())

#Nomor 3
class stuck():
    def __init__(self): #membuat stack kosong
        self.item = []
    def empty(self): #mengembalikan nilai boolean yang menunjukkan apakah stack itu kosong
        return len(self) == 0
    def __len__(self): #mengembalikan banyaknya item di stack
        return (self.item)
    def peek(self):  #mengembalikan nilai posisi atas tanpa menghapus dan mengembalikan nilai dari item yang paling atas tanpa menghapus
        assert not self.empty()
        return self.item[-1]
    def pop(self): #mengembalikan nilai posisi atas lalu menghapus, stack kosong tidak dapat kosong
        assert not self.empty()
        return self.item.pop()
    def push(self, data): #mendorong item ke stack, menambah item ke puncak stack
        self.item.append(data)

nilai = stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
st = " "
for i in range (len(nilai)):
    st = st + " " + str(nilai.pop())
    print (st)
