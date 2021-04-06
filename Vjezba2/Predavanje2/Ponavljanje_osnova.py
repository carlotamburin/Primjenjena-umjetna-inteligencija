## Stringovi vecinom

s="abc"
s=list(s)

s="".join(s)  # Pretvaranje nazad u string
print(s)

prazan_skup=set(['a','b'])
print(prazan_skup)

rijecnik={('a',1):[1,2]}       #Kljuc moze biti samo nepromjenjiv tip podatka (tuple,string itd..)


## skupovi

skup1=[3,5,6,7,8,9]
skup2={1,2,5,3,1,2,5} ##Brze zbog hash tablice

def presjek():
    rez=[]
    for b1 in skup1:
        if b1 in skup2:
            rez.append(b1)
    return rez

print(presjek)


## funkcije

def dodaj1(lst,b):
    lst=lst+[b]

def dodaj2(lst,b):
    lst.append(b)

def dodaj3(lst,b):
    lst+=[b]

def dodaj4(lst,b):
    lst.append([b])

lista=[3,4,5,6,7,8]

dodaj1(lista,3)
print(lista)

dodaj2(lista,3)
print(lista)

dodaj3(lista,3)
print(lista)

dodaj4(lista,3)
print(lista)


## list comprenhension

# lista kvadrata brojeva do 10

lst=[]
for i in range(10):
    lst.append(i*i)

lst=[i*i for i in range(10)]

print(lst)

#Lista kvadrata brojeva do 100, samo brojevi kojio zavrsavaju na 3 sa comprenhensionom sa else dodaj 0
lst=[i*i if i%10==3 else 0 for i in range(100)]
print(lst)
## sa elsom

lst=[i*i for i in range(100) if i%10==3] ## samo if
print(lst)

# string od 10 x ova
s="x"*10
# vektor od 10 nula
v=[0]*10

# Parametri za funkciju
def zbroj(a=3,b=4,c=5):
    return a+b+c

print(zbroj(3,4,5))

def zbroj2(*args):  ## vraca sve primljene argumente
    print(args)

zbroj(1,2,3)

def zbroj22(**args):  ## vraca rijecnik
    print(args)


# Python prima funkcije kao parametre

def zbroj55(a,b):
    return a+b

def operacija(a,b,op):
    return op(a,b)

operacija(2,1,zbroj)

## min i max
m=max([2,3,5,1,55])
print(m)

# lista parova po drugom elementu nadi max inace je default prvi
n=max([(2,5),(3,5)],key=lambda x:x[1])
print(n)

## soritrati po umnosku
n=sorted([(2,5),(3,5)],key=lambda x:x[0]*x[1])
n=sorted([(2,5),(3,5)],key=lambda x:-x[0]*x[1]) #Sortira silazno, po defaultu ulazno
print(n)

## zipanje
print(list(zip([2,3,4],[5,6,7,8])))

lst=[(2,5),(3,4),(5,6)]
m=max(zip(range(len(lst)),lst),key=lambda x :x[0]*x[1])
print(m)

m=max(zip(range(len(lst)),lst),key=lambda x :x[1][0]*x[1][1])
print(m)

# moze i enumerate
for a,b in lst:
    print(a,b)

for (i,(a,b)) in lst:  # TU NEGDJE IDE ENUMARATE
    print(a,b)

## REKURZIJE#############

def ispis_do_n(N):
    while i<N:
        print(i)

def ispis_do_N_rek(N):
    if N==0:
        print(0)
        return
    print(N)
    ispis_do_N_rek(N-1)

print(ispis_do_N_rek(10))


def ispis_do_N_rekObrnuto(N):
    if N==0:
        print(0)
        return
    ispis_do_N_rek(N-1)
    print(N)

def zbroj_do_N(N):
    if N==0:
        return 0
    N + zbroj_do_N(N-1)

## Binarna pretraga

lista=[4,6,7,8,10,11,15 ]

def binpret_rek(lista,broj):
    if(lista==[]):
        return False
    pola=len(lista)//2
    if(lista[pola]==broj):
        return True
    if(lista[pola]>broj):
        return binpret_rek(lista[0:pola],broj)  ## od nula do pola
    if(lista[pola]<broj):
        return binpret_rek(lista[pola+1:],broj)  # od pola do kraja
    return True

print(binpret_rek(lista,6))

#quicksort

lista=[4,6,645,8,32,11111,215 ]
# [ sortirani manji] + pivot + [soritrani veci]

def quicksortZaSiromasne(lista):
    if(len(lista)<2):
        return lista
    pivot,lista=lista[0],lista[1:]
    manji=[e for e in lista if e<pivot]
    veci=[e for e in lista if e>pivot]
    return quicksortZaSiromasne(manji)+[pivot]+quicksortZaSiromasne(veci)

print(quicksortZaSiromasne(lista))

# Funckija generira matricu nula N*N

def matrica(N):
    return [[0]*N for r in range(N)]
    mat=[]
    for r in range(N):
        redak=[0]*N
        mat.append(redak)
    return mat

m=matrica(4)
m[1][1]=6
m[2][2]=3
for r in m:
    print(r)
        






