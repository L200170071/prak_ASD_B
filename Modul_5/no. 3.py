from time import time as detak
from random import shuffle as kocok

def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

def bubbleSort(L):
    n = len(L)
    for i in range (n-1):
        for j in range (n-i-1):
            if L[j] > L[j+1]:
                swap(L,j,j+1)
    return L

def selectionSort(L):
    n = len(L)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(L, i, n)
        if indexKecil != i:
            swap(L, i, indexKecil)
    return L

def insertionSort(L):
    n = len(L)
    for i in range(1, n):
        nilai = L[i]
        pos = i
        while pos > 0 and nilai < L[pos -1]:
            L[pos] = L[pos-1]
            pos = pos - 1
        L[pos] = nilai
    return L
        
daftar = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

print (bubbleSort(daftar))
print (selectionSort(daftar))
print (insertionSort(daftar))


k =  [[i] for i in range(1, 6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw=detak();bubbleSort(u_bub);ak=detak();print("bubble: %g detik" %(ak-aw));
aw=detak();selectionSort(u_sel);ak=detak();print("selection: %g detik" %(ak-aw));
aw=detak();insertionSort(u_ins);ak=detak();print("insertion: %g detik" %(ak-aw));


