import timeit
from mod import insertionsort
import random

print(" - jumlahkan_cara_1 - ")
def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya = hasilnya + i
        return hasilnya
        
for i in range(5): # mengulang lima kali
    awal = timeit.timeit() # menandai awal kerja
    h = jumlahkan_cara_1(10000) # menjumlah 1 sampai sepuluh ribu
    akhir = timeit.timeit() # menandai akhir kerja, lalu mencetak
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))

print("==================================================================")
print(" ")
print(" - jumlahkan_cara_2 - ")

def jumlahkan_cara_2(n):
    return ( n*(n + 1) )/2

for i in range(5): # mengulang lima kali
    awal = timeit.timeit() # menandai awal kerja
    h = jumlahkan_cara_2(10000) # menjumlah 1 sampai sepuluh ribu
    akhir = timeit.timeit() # menandai akhir kerja, lalu mencetak
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))

print("==================================================================")
print(" ")
print(" - average case scenario -")

for i in range(5):
    L = list(range(3000))
    random.shuffle(L) # Mengacak posisi elemen di list
    awal = timeit.timeit()
    U = insertionsort(L)
    akhir = timeit.timeit()
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L),akhir-awal))

print("==================================================================")
print(" ")
print(" - worst case scenario - ")


for i in range(5):
    L = list(range(3000))
    L = L[::-1] # Membalik urutan elemen di list
    awal = timeit.timeit()
    U = insertionsort(L)
    akhir = timeit.timeit()
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L),akhir-awal))

print("==================================================================")
print(" ")
print(" - best case scenario - ")

for i in range(5):
    L = list(range(3000))

    awal = timeit.timeit()
    U = insertionsort(L)
    akhir = timeit.timeit()
print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L),akhir-awal))