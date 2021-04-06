def zadatak():
    lista1 = [3, 3, 3, 5, 7, 9, 22, 55, 160, 180, 700]
    lista2 = [6, 7, 7, 8, 10, 21, 66, 100, 180, 200, 543]

    print(merge(lista1, lista2))


def merge(lista1, lista2):
    if lista1 == []:
        return lista2+[]
    if(lista2 == []):
        return lista1+[]

    if(lista1[0] > lista2[0]):
        # print(lista2[0])
        # Svaki put uzima prvi element u svakoj iteraciji
        return [lista2[0]] + merge(lista1, lista2[1:])

    if(lista1[0] < lista2[0]):
        # print(lista1[0])
        return [lista1[0]] + merge(lista1[1:], lista2)

    if(lista1[0] == lista2[0]):
        return [lista1[0]] + merge(lista1[1:], lista2)


if __name__ == "__main__":
    zadatak()
