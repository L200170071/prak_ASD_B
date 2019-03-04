"""1"""
def sikusiku(x):
    i=1
    while i<=x:
        print("*"*i)
        i+=1
sikusiku(3)

"""2"""
def gambarlahpersegi(a,b):
    i=1
    print("@"*b)
    while(i<a):
       print("@"+" "*(b-2)+"@")
       i+=1
    print("@"*b)
gambarlahpersegi(5,5)

"""3"""
def jumlahvokal(a):
    v="aiueoAIUEO"
    vokal=0
    jumlahhuruf=0
    for i in a:
        jumlahhuruf+=1
        if i in v:
            vokal+=1
    return (vokal,jumlahhuruf)
print(jumlahvokal("afgi"))
def jumlahhurufkonsonan(a):
    v="bcdfghjklmnpqrstvwxyz"
    konsonan=0
    jumlahhuruf=0
    for i in a:
        jumlahhuruf+=1
        if i in v:
            konsonan+=1
    return (konsonan,jumlahhuruf)
print(jumlahhurufkonsonan("afgiii"))

"""4"""
def ratarata(b=[]):
    x=0
    n=0
    if b != []:
        for i in b:
            x+=i
            n+=1
        return x/n
    return "illegal"
print(ratarata([2,2]))

"""5"""
from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primakecil=[2, 3, 5, 7, 11]
    bukanprima=[0, 1, 4, 6, 8, 9, 10]
    if n in primakecil:
        return True
    elif n in bukanprima:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
    return True
print(apakahPrima(71))

""""6"""
def cetakbilanganprima():
    prima=list()
    for i in range(2,100):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if(a):
            print(i)
            prima.append(i)
cetakbilanganprima()

"""7"""
def faktorprima(n):
    prima=list()
    for i in range(2,n):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if a and n%i==0:
            prima.append(i)
    return prima
print(faktorprima(143))

"""8"""
def apakahTerkandiung(a,b):
    return a in b
print(apakahTerkandiung("db","abcdcdsqwedb"))
print(apakahTerkandiung("abd","abc"))

"""9"""
def iterasi():
    for i in range(1,100):
        if (i%3)!=0 and (i%5)!=0:
            print(i)
        else:
            if (i%15)==0:
                print("pyton UMS")
            elif (i%3)==0:
                print("python")
            elif (i%5)==0:
                print("UMS")
iterasi()

"""10"""
def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2)-(4*a*c)
    if D<0:
        return "determinan negatif"
    return  "determinan positif"
print(selesaikanABC(1,1,2))

"""11"""
def apakahkabisat(a):
    if(a%400==0):
        return True
    if(a%100==0):
        return False
    if(a%4==0):
        return True
    return False
print(apakahkabisat(100))

"""12"""
import random
def permainan():
    a=random.randrange(0, 100)
    while(True):
        b=int(input("masukan angka: "))
        if(b>a):
            print("terlalu besar, coba lagi")
        elif(b<a):
            print("terlalu kecil, coba lagi")
        else:
            print("benar")
            break
permainan()

"""13"""
def katakan(a):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",6:"ratus ",7:"juta ",8:"puluhjuta "}
    b=str(a)
    c=""
    i=-1
    while i>= -len(b):
        c=x[b[i]]+y[i]+c
        i-=1
    return c
print(katakan(11))

"""14"""
def formatRupiah(a):
    b=str(a)
    c=""
    i = -1
    while i>= -len(b):
        if((i+1)%3==0 and (i+1)!=0):
            c="."+c
        c=b[i]+c
        i-=1
    return "Rp "+c
print(formatRupiah(30000000))
