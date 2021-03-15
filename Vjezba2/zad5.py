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

    leftList = mergesort(left)
    rightList = mergesort(right)

    return merge(leftList, rightList)


if __name__ == "__main__":
    zadatak()
