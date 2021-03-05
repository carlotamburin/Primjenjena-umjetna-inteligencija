import random


def igra():

    pogadanje = 1001
    zamisljeniBroj = 0
    brojPodagadanja = 0
    maxGranica = 1000
    minGranica = 0

    zamisljeniBroj = int(input("Unesite broj u intervalu 0 do 1000 "))
    pogadanje = random.randrange(minGranica, maxGranica)

    while(zamisljeniBroj != pogadanje):

        if(pogadanje < zamisljeniBroj):
            print("Zamisljeni broj je veci od pogadanja")
            minGranica = pogadanje
            pogadanje = random.randrange(minGranica+1, maxGranica)
            brojPodagadanja = brojPodagadanja+1
            continue

        if(pogadanje > zamisljeniBroj):
            print("Zamisljeni broj je manji od pogadanja")
            maxGranica = pogadanje
            pogadanje = random.randrange(minGranica, maxGranica)
            brojPodagadanja = brojPodagadanja+1
            continue

        brojPodagadanja = brojPodagadanja+11

    print("Pogodili ste broj u: {0} pogadanja".format(brojPodagadanja))


if __name__ == "__main__":
    igra()
