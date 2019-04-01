L = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

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

def bubbleSort():
    n = len(L)
    for i in range (n-1):
        for j in range (n-i-1):
            if L[j] > L[j+1]:
                swap(L,j,j+1)

def selectionSort():
    n = len(L)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(L, i, n)
        if indexKecil != i:
            swap(L, i, indexKecil)

def insertionSort():
    n = len(L)
    for i in range(1, n):
        nilai = L[i]
        pos = i
        while pos > 0 and nilai L[pos -1]:
            L[pos] = L[pos-1]
            pos = pos - 1
        L[pos] = nilai
