def zadatak():
    # Z >= x+y
    # Y >= z+x
    # X >= z+y
    listaPredenih = []
    x = 1
    y = 1
    z = 1
    jednadzba = z/(x+y) + y/(z+x) + x/(z+y)
    rjesenja = ()
    rangeMin = -1
    rangeMax = 1
    brojac = 0

    while(brojac <= 10):
        for i in range(rangeMin, rangeMax):
            for j in range(rangeMin, rangeMax):
                for k in range(rangeMin, rangeMax):
                    x = k
                    y = j
                    z = i
                    if(x+y == 0 or z+x == 0 or z+y == 0):
                        continue

                    jednadzba = z/(x+y) + y/(z+x) + x/(z+y)
                    try:
                        if(jednadzba == 4):
                            if((x, y, z) not in listaPredenih):
                                listaPredenih.append((x, y, z))
                                print(
                                    "Nadeno je rjesenje: {0} {1} {2}".format(x, y, z))
                                print("zbroj je:{0}".format(
                                    abs(x)+abs(y)+abs(z)))
                                brojac = brojac+1
                    except ZeroDivisionError:
                        pass

        rangeMin = rangeMin-1
        rangeMax = rangeMax+1
    print("Ukupno ima :{0} rjesenja".format(brojac))


if __name__ == "__main__":
    zadatak()
