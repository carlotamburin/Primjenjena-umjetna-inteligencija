def zadatak():
    lista=[4,5,6,7,8,9,10,11,12]

    print(count(lista,jeliParan))
    print(iterativno(lista,jeliParan))




def count(lst,p):
    if lst==[]:
        return 0

    if p(lst[0]):
        return 1+count(lst[1:],p)
    if p(lst[0]==False):
       return 0+count(lst[1:],p)





def jeliParan(el):
    if el%2==0:
        return True

def iterativno(lst,p):
    brojac=0
    for el in lst:
        if p(el):
            brojac=brojac+1
    return brojac











if __name__ == "__main__":
    zadatak()
