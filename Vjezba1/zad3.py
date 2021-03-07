import random


def igra():
    randomBroj = 0
    pogadanje = 1001

    randomBroj = random.randrange(0, 1000)
    print(randomBroj)

    while(pogadanje != randomBroj):
        pogadanje = int(input("Unesite broj"))

        if(pogadanje < randomBroj):
            print("Uneseni broj je manji od zamisljenog")

        if(pogadanje > randomBroj):
            print("Uneseni broj je veci od zamisljenog")

    print("Pogodili ste broj")


if __name__ == "__main__":
    igra()
