from random import shuffle
import copy
import random
from typing import KeysView


class Card:

    COLOR_VALUE = {
        "spadi": 0,
        "dinari": 1,
        "kupa": 2,
        "bastoni": 3,
    }

    CARDS_VALUE = {"3": 10, "2": 9, "1": 8, "13": 7, "12": 6,
                   "11": 5, "7": 4, "6": 3, "5": 2, "4": 1}

    def __init__(self, num, col):
        self._num = num
        self._col = col

    def __str__(self):
        return "[" + str(self._num) + self._col + "]"


class Cards:

    def __init__(self, cards):
        self._cards = cards

    def count(self):
        return len(self._cards)

    def __str__(self):
        return '{' + ', '.join(str(c) for c in self._cards) + '}'

    def toString(self):
        return ','.join(str(c) for c in self._cards)


class Deck(Cards):   # Nasljeduje klasu Cards

    def __init__(self):
        cards = [Card(num, col)
                 for col in Card.COLOR_VALUE for num in Card.CARDS_VALUE.keys()]                            # Desna petlja je ujedno i unutarnja
        super().__init__(cards)  # Poziva konstruktor super klase odnosno nad klase

    def shuffle(self):
        shuffle(self._cards)

    def deal(self, n):
        hand, self._cards = self._cards[:n], self._cards[n:]
        return Cards(hand)

    def drawOne(self):
        karta, self._cards = self._cards[:1], self._cards[1:]
        return Cards(karta)  # Zbrojiti sa starim


class Ruka():
    igracOdigranaKarta = ""
    igracDobioRuku = 0
    RacunaloDobiloRuku = 0

    def __init__(self, cards, igrac):
        # Igrac
        if(igrac == "human"):
            print("Moja ruka {0}".format(cards))
            for i in range(0, len(cards)):
                print(" {0} -> {1} ".format(i, cards[i]), end='')
            odigrajKartuIgrac = int(input())
            print("ODIGRANA KARTA IGRACA JE:{0}\n".format(
                cards[odigrajKartuIgrac]))
            Ruka.igracOdigranaKarta = copy.deepcopy(cards[odigrajKartuIgrac])
            cards.remove(cards[odigrajKartuIgrac])
            # Pokušavam maknut empty string ali neuspješno
            cards = [x for x in cards if x != ""]
            self._ruka = cards
        # Racunalo
        if(igrac == "AI"):
            print("Racunalo ruka {0}".format(cards))
            odigrajKartuRacunalo, jeliIstiTip = self.racunaloOdabir(
                cards, Ruka.igracOdigranaKarta)
            print("ODIGRANA KARTA RACUNALA JE:{0}\n".format(
                odigrajKartuRacunalo))
            self.tkoNosiRuku(Ruka.igracOdigranaKarta,
                             odigrajKartuRacunalo, jeliIstiTip)
            cards.remove(odigrajKartuRacunalo)
            # Pokušavam maknut empty string ali neuspješno
            cards[:] = [x for x in cards if x != ""]
            self._ruka = cards

    def changeHandState(self):
        return Cards(self._ruka)

    def racunaloOdabir(self, cards, igracevaKarta):

        for el in cards:
            # Ako su oba jednoznamenkasta broja
            if((el[2] == igracevaKarta[2]) and el[2] not in Card.CARDS_VALUE.keys()):
                return el, 1
            # Ako je igracev broj dvoznamenkasta racunalov jednoznamenkast
            if((el[2] == igracevaKarta[3]) and el[2] not in Card.CARDS_VALUE.keys()):
                return el, 1
            # Ako je racunalunalov broj dvoznamenkast a igracev dvoznamenkast
            if((el[3] == igracevaKarta[2]) and el[3] not in Card.CARDS_VALUE.keys()):
                return el, 1
            # Ako su oba dvoznamenkasta broja
            if((el[3] == igracevaKarta[3]) and el[3] not in Card.CARDS_VALUE.keys()):
                return el, 1

        return random.choice(cards), 0

        # Dodatna return vrijednost oznacava jeli istog tipa, 1 oznacava da je, 0 oznacava da nije

    def tkoNosiRuku(self, igracevaKarta, racunaloKarta, jeliIstiTip):
        igracevaKarta.strip(" ")
        racunaloKarta.strip(" ")
        if((igracevaKarta[1] and igracevaKarta[2]) in Card.CARDS_VALUE.keys()):
            kartaIgrac = Card.CARDS_VALUE[str(
                igracevaKarta[1])+str(igracevaKarta[2])]
        kartaIgrac = Card.CARDS_VALUE[igracevaKarta[1]]

        if((racunaloKarta[1] and racunaloKarta[2]) in Card.CARDS_VALUE.keys()):
            kartaRacunalo = Card.CARDS_VALUE[str(
                racunaloKarta[1])+str(racunaloKarta[2])]
        kartaRacunalo = Card.CARDS_VALUE[racunaloKarta[1]]

        if(kartaIgrac > kartaRacunalo):
            print("Igrac dobio ruku")
            Ruka.igracDobioRuku = Ruka.igracDobioRuku+1
        if((kartaIgrac < kartaRacunalo) and jeliIstiTip == 1):
            print("Racunalo dobilo ruku")
            Ruka.RacunaloDobiloRuku = Ruka.RacunaloDobiloRuku+1
        if(kartaIgrac == kartaRacunalo):
            print("Igrac dobio ruku")
            Ruka.igracDobioRuku = Ruka.igracDobioRuku+1
        if((kartaIgrac < kartaRacunalo) and jeliIstiTip == 0):
            print("Igrac dobio ruku")
            Ruka.igracDobioRuku = Ruka.igracDobioRuku+1


class Treseta():
    def __init__(self):
        print("Dobrodosli u tresetu \n")
        self.igra = Deck()
        self.igra.shuffle()

        self.IgracRuka = self.igra.deal(4)
        self.racunaloRuka = self.igra.deal(4)

        while(True):
            # Igrac
            if (type(self.IgracRuka) != list):
                self.IgracRuka = Ruka(self.IgracRuka.toString().split(
                    ","), "human").changeHandState()
                self.IgracRuka = self.IgracRuka.toString().split(
                    ",")+self.igra.drawOne().toString().split(",")

            # Racunalo
                self.racunaloRuka = Ruka(self.racunaloRuka.toString().split(
                    ","), "AI").changeHandState()
                self.racunaloRuka = self.racunaloRuka.toString().split(
                    ",")+self.igra.drawOne().toString().split(",")

            else:
                # Igrac
                self.IgracRuka = Ruka(
                    self.IgracRuka, "human").changeHandState()
                if(self.igra.count() != 0):
                    self.IgracRuka = self.IgracRuka.toString().split(
                        ",")+self.igra.drawOne().toString().split(",")
                else:
                    self.IgracRuka = self.IgracRuka.toString().split(
                        ",")
                self.IgracRuka = [x.strip(' ') for x in self.IgracRuka]
                # Racunalo
                self.racunaloRuka = Ruka(
                    self.racunaloRuka, "AI").changeHandState()
                if(self.racunaloRuka.count() == 0):       # Kada ruka bude prazna
                    break
                if(self.igra.count() != 0):  # Ako je deck prazan ne vuci nego samo ucitaj proslo stanje
                    self.racunaloRuka = self.racunaloRuka.toString().split(
                        ",")+self.igra.drawOne().toString().split(",")
                else:
                    self.racunaloRuka = self.racunaloRuka.toString().split(
                        ",")
                self.racunaloRuka = [x.strip(' ') for x in self.racunaloRuka]

            print("Ostalo je: {0} karata u deku".format(self.igra.count()))
            print("///////////////////////\n///////////////////////\n")

        if(Ruka.igracDobioRuku > Ruka.RacunaloDobiloRuku):
            print("Igrac je dobio partiju s dobivenih: {0} ruku \n racunalo ima: {1} dobivenih".format(
                Ruka.igracDobioRuku, Ruka.RacunaloDobiloRuku))
        else:
            print("Racunalo je dobilo partiju s dobivenih: {0} ruku \n igrac ima: {1} dobivenih".format(
                Ruka.RacunaloDobiloRuku, Ruka.igracDobioRuku))

    def pogledajuku(self):
        return print("Moja ruka je:{0} \nRuka od racunala je: {1}".format(self.IgracRuka, self.racunaloRuka))


if __name__ == '__main__':

    igra = Treseta()
