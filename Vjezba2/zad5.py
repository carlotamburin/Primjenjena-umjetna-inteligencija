from zad4 import merge


def zadatak():
    lista = [1, 6, 23, 2, 3, 55, 32]
    print(mergesort(lista))


def mergesort(lista):
    if len(lista) < 2:
        return lista

    mid = len(lista)//2

    left = lista[:mid]
    right = lista[mid:]

    leftList = mergesort(left)  #Rekurzivno se rijesava prva polovica polovice left->1,6,23 left->1 return: right->6,23 left->6 return: right->26 return: merge(6,23) <- merge(1,[6,23])
    rightList = mergesort(right) # Rekurzivno se rijesava druga polovica polovice

    return merge(leftList, rightList)


if __name__ == "__main__":
    zadatak()

""" 
    Prvi ulazak dili na 1,6,23 ==== 2,3,55,32 i ulazi u leftList
    Drugi ulazak dili na 1 ==6,23 i ulazi u left list
    Left list ima samo 1 i vraca ga
    sad smo na left= 1 i right = 6,23 i ulazi u desni
    Dili na 6 === 23 i ulazi u 6 (livi)
    vraca 6
    Ulazi u desni 23
    vraca 23
    livi i desni su definirani zovi merge (6,23)
    vrati nazad korak
    livi=1 desni= 6,23 i zovi merge(1,[6,23]) jer smo se vratili iz righta pa odma slijedi opet merge
    vrati se nazad
    sad smo na desnom 2,3,55,32
    Ulazi tri puta za prvu polovicuu """

