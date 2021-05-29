# U redu, napravite onda trešetu za dvoje (sa uzimanjem karte). Za algoritam ćete onda dodati jednostavni FlatMC (jučer smo ga vidjeli na predavanju).
# Krenite pa ćemo se čuti oko detalja.
''' Ideja
Najbolja akcija je s najslabijom kartom dobit turn '''
import copy
from random import choice, shuffle
import copy
import random
from typing import KeysView
from collections import OrderedDict, defaultdict


class Card:

    COLOR_VALUE = {
        "spadi": 0,
        "dinari": 1,
        "kupa": 2,
        "bastoni": 3,
    }

    CARDS_VALUE = OrderedDict()
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
    flag = 0
    igracOdigranaKarta = ""
    racunaloOdigranaKarta = ""
    igracDobioRuku = 0
    RacunaloDobiloRuku = 0
    TkoJeDobioRuku = ""
    j = 0

    def __init__(self, cards, igrac, najboljaKartaRac):
        if(Ruka.flag == 0):
            # Ruka.TkoJeDobioRuku = igrac
            Ruka.flag += 1
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
            Ruka.j += 1
        # Racunalo
        if(igrac == "AI"):
            flagJeliOdigraoSto = 0
            sorted_dict = {}
            print("Racunalo ruka {0}".format(cards))

            # Sortiranje dictionarya
            sorted_tuples = sorted(najboljaKartaRac.items(
            ), key=lambda item: item[1], reverse=True)
            sorted_dict = {k: v for k, v in sorted_tuples}

            for key, value in sorted_dict.items():
                if Ruka.TkoJeDobioRuku == "human":
                    if self.jeli_isti_tip(key, Ruka.igracOdigranaKarta) == 1:
                        odigrajKartuRacunalo = "["+str(key)+"]"
                        flagJeliOdigraoSto = 1
                        break

                else:
                    odigrajKartuRacunalo = "["+str(key)+"]"
                    flagJeliOdigraoSto = 1
                    break

            if(flagJeliOdigraoSto == 0):
                odigrajKartuRacunalo = min(
                    sorted_dict, key=sorted_dict.get)
                odigrajKartuRacunalo = "["+str(key)+"]"

            # Karta odabrana sortiranje gotovo

            Ruka.racunaloOdigranaKarta = odigrajKartuRacunalo
            print("ODIGRANA KARTA RACUNALA JE:{0}\n".format(
                odigrajKartuRacunalo))
            cards.remove(odigrajKartuRacunalo)
            # Pokušavam maknut empty string ali neuspješno
            cards[:] = [x for x in cards if x != ""]
            self._ruka = cards
            Ruka.j += 1
            flagJeliOdigraoSto = 0

        if Ruka.j == 2:
            jeliIstiTip = self.jeli_isti_tip(
                Ruka.racunaloOdigranaKarta, Ruka.igracOdigranaKarta)
            self.tkoNosiRuku(Ruka.igracOdigranaKarta,
                             Ruka.racunaloOdigranaKarta, jeliIstiTip)
            Ruka.j = 0

    def changeHandState(self):
        return Cards(self._ruka)

    def racunaloOdabir(self, cards, igracevaKarta):

        for el in cards:
            # Ako su oba jednoznamenkasta broja
            if((el[2] == igracevaKarta[2]) and el[2] not in Card.CARDS_VALUE.keys()):
                return 1
            # Ako je igracev broj dvoznamenkasta racunalov jednoznamenkast
            if((el[2] == igracevaKarta[3]) and el[2] not in Card.CARDS_VALUE.keys()):
                return 1
            # Ako je racunalunalov broj dvoznamenkast a igracev dvoznamenkast
            if((el[3] == igracevaKarta[2]) and el[3] not in Card.CARDS_VALUE.keys()):
                return 1
            # Ako su oba dvoznamenkasta broja
            if((el[3] == igracevaKarta[3]) and el[3] not in Card.CARDS_VALUE.keys()):
                return 1

        return 0
        # Dodatna return vrijednost oznacava jeli istog tipa, 1 oznacava da je, 0 oznacava da nije

    def igranjeIgre(self, tkoIgraPrvi, IgracRuka, racunaloRuka, igra, najboljaKartaRac):
        jeliIgracRukaPrazna = 0
        jeliRacunaloRukaPrazna = 0
        print("PRVI IGRA", end=" ")
        print("\033[1m" + tkoIgraPrvi + "\033[0m")

        if tkoIgraPrvi == "human":
          # Igrac prvi
            if (type(IgracRuka) != list):
                IgracRuka = Ruka(IgracRuka.toString().split(
                    ","), "human", najboljaKartaRac).changeHandState()
                IgracRuka = IgracRuka.toString().split(
                    ",")+igra.drawOne().toString().split(",")

            else:
                # Igrac
                IgracRuka = Ruka(
                    IgracRuka, "human", najboljaKartaRac).changeHandState()
                if(IgracRuka.count() == 0):
                    jeliIgracRukaPrazna = 1
                if(igra.count() != 0):
                    IgracRuka = IgracRuka.toString().split(
                        ",")+igra.drawOne().toString().split(",")
                else:
                    IgracRuka = IgracRuka.toString().split(
                        ",")

                IgracRuka = [x.strip(' ') for x in IgracRuka]

            # Racunalo
            if (type(racunaloRuka) != list):
                racunaloRuka = Ruka(racunaloRuka.toString().split(
                    ","), "AI", najboljaKartaRac).changeHandState()
                racunaloRuka = racunaloRuka.toString().split(
                    ",")+igra.drawOne().toString().split(",")

            else:
                # Racunalo
                racunaloRuka = Ruka(
                    racunaloRuka, "AI", najboljaKartaRac).changeHandState()
                if(racunaloRuka.count() == 0):
                    jeliRacunaloRukaPrazna = 1
                if(igra.count() != 0):  # Ako je deck prazan ne vuci nego samo ucitaj proslo stanje
                    racunaloRuka = racunaloRuka.toString().split(
                        ",")+igra.drawOne().toString().split(",")
                else:
                    racunaloRuka = racunaloRuka.toString().split(
                        ",")
                racunaloRuka = [x.strip(' ') for x in racunaloRuka]

        elif (tkoIgraPrvi == "AI"):

            # Racunalo
            if (type(racunaloRuka) != list):
                racunaloRuka = Ruka(racunaloRuka.toString().split(
                    ","), "AI", najboljaKartaRac).changeHandState()
                racunaloRuka = racunaloRuka.toString().split(
                    ",")+igra.drawOne().toString().split(",")

            else:
                # Racunalo
                racunaloRuka = Ruka(
                    racunaloRuka, "AI", najboljaKartaRac).changeHandState()
                if(racunaloRuka.count() == 0):
                    jeliRacunaloRukaPrazna = 1
                if(igra.count() != 0):  # Ako je deck prazan ne vuci nego samo ucitaj proslo stanje
                    racunaloRuka = racunaloRuka.toString().split(
                        ",")+igra.drawOne().toString().split(",")
                else:
                    racunaloRuka = racunaloRuka.toString().split(
                        ",")
                racunaloRuka = [x.strip(' ') for x in racunaloRuka]

            if (type(IgracRuka) != list):
                IgracRuka = Ruka(IgracRuka.toString().split(
                    ","), "human", najboljaKartaRac).changeHandState()
                IgracRuka = IgracRuka.toString().split(
                    ",")+igra.drawOne().toString().split(",")

            else:
                # Igrac
                IgracRuka = Ruka(
                    IgracRuka, "human", najboljaKartaRac).changeHandState()
                if(IgracRuka.count() == 0):
                    jeliIgracRukaPrazna = 1
                if(igra.count() != 0):
                    IgracRuka = IgracRuka.toString().split(
                        ",")+igra.drawOne().toString().split(",")
                else:
                    IgracRuka = IgracRuka.toString().split(
                        ",")

                IgracRuka = [x.strip(' ') for x in IgracRuka]

               # Kada ruka bude prazna
           # return IgracRuka, racunaloRuka, 1
        if((jeliIgracRukaPrazna and jeliRacunaloRukaPrazna) == 1):
            return IgracRuka, racunaloRuka, 1
        print("Ostalo je: {0} karata u deku".format(igra.count()))
        print("///////////////////////\n///////////////////////\n")
        return IgracRuka, racunaloRuka, 0

    def best_action(self):  # FLAT mc
        odigraneKarteINagrada = defaultdict()
        karteCopy = copy.deepcopy(self)

        if (type(self.racunaloRuka) != list):
            karteRacunalo = copy.deepcopy(
                self.racunaloRuka.toString().split(","))
        else:
            karteRacunalo = copy.deepcopy(self.racunaloRuka)

        if (type(self.IgracRuka) != list):
            IgracRuka = copy.deepcopy(
                self.IgracRuka.toString().split(","))
        else:
            IgracRuka = copy.deepcopy(self.IgracRuka)

        # Pocetak algoritma
        for racunaloKarta in karteRacunalo:
            v = 0
            flagMin = 0
            flagAs = 0
            for karta in IgracRuka:
                jeliIstiTip = karteCopy.do(
                    racunaloKarta, karta)  # Jeli isti tip
                # Vrati nagradu ovisno koja je karta
                addToV, flagMin, flagAs = karteCopy.reward(
                    karta, racunaloKarta, jeliIstiTip, flagMin, flagAs)
                v += addToV

                konacnaKarta = str(racunaloKarta)[1:-1]
                odigraneKarteINagrada[konacnaKarta] = v
        print(odigraneKarteINagrada)
        # bestRacunaloKarta = max(odigraneKarteINagrada.keys(), key=(
        # lambda k: odigraneKarteINagrada[k]))
        return odigraneKarteINagrada

    def reward(self, kartarac1, kartarac2, jeliIstiTip, flagMin, flagAs):
        nagrada = 0
        flagMinn = 0
        flagAss = 0
        # Pobjeduje li trenutna karta
        if self.tkoNosiRukuSim(kartarac1, kartarac2, jeliIstiTip) == "AI":
            if(flagMin == 0):
                v, flagMinn = self.jeliKartaMinimalnaIstogTipa(kartarac2)
                if(v) == 4:
                    nagrada += 4
            nagrada += 1
        if(flagAs == 0):
            nagradaAs, flagAss = self.bacamLiAsa(
                kartarac2, Ruka.TkoJeDobioRuku)
            nagrada += nagradaAs
        return nagrada, flagMinn, flagAss

    def jeliKartaMinimalnaIstogTipa(self, karta):
        listaIstih = []
        jacinaKarte = ""
        if (type(self.racunaloRuka) != list):
            karteRacunalo = copy.deepcopy(
                self.racunaloRuka.toString().split(","))
        else:
            karteRacunalo = copy.deepcopy(self.racunaloRuka)

        for el in karteRacunalo:
            if self.jeli_isti_tip(el, karta) == 1:
                listaIstih.append(el)
                # Dodati iako nije isti a bacio najmanju "lisinu" daj 0.5 boda?
        if not listaIstih:
            return 0, 0
        jacinaIKartaLista = []
        for el in listaIstih:
            if((el[1] and el[2]) in Card.CARDS_VALUE.keys()):
                jacinaKarte = Card.CARDS_VALUE[str(
                    el[1])+str(el[2])]
            else:
                jacinaKarte = int(Card.CARDS_VALUE[el[1]])

            jacinaIKartaLista.append((jacinaKarte, el))
        minClan = min(jacinaIKartaLista, key=lambda t: t[0])
        if karta == minClan[1]:
            return 4, 1
        return 0, 0

    def bacamLiAsa(self, karta, jeliRacunalaRed):
        if((karta[1]) == "1") and (karta[2] not in Card.CARDS_VALUE.keys()):
            if(jeliRacunalaRed == "AI"):
                return 10, 1
            BrojKarataKojeKupeAs = 0
        else:
            return 0, 0

        if (type(self.IgracRuka) != list):
            IgracRuka = copy.deepcopy(
                self.IgracRuka.toString().split(","))
        else:
            IgracRuka = copy.deepcopy(self.IgracRuka)

        for el in IgracRuka:
            if((el[1] and el[2]) in Card.CARDS_VALUE.keys()):
                jacinaKarte = Card.CARDS_VALUE[str(
                    el[1])+str(el[2])]
            else:
                jacinaKarte = int(Card.CARDS_VALUE[el[1]])

            if jacinaKarte > 8:
                BrojKarataKojeKupeAs += 2

            return -BrojKarataKojeKupeAs, 1

    def jeli_isti_tip(self, kartaRacunala, kartaRacunala2):
        # Ako su oba jednoznamenkasta broja
        if((kartaRacunala[2] == kartaRacunala2[2]) and kartaRacunala[2] not in Card.CARDS_VALUE.keys()):
            return 1
        # Ako je igracev broj dvoznamenkasta racunalov jednoznamenkast
        if((kartaRacunala[2] == kartaRacunala2[3]) and kartaRacunala[2] not in Card.CARDS_VALUE.keys()):
            return 1
        # Ako je racunalunalov broj dvoznamenkast a igracev dvoznamenkast
        if((kartaRacunala[3] == kartaRacunala2[2]) and kartaRacunala[3] not in Card.CARDS_VALUE.keys()):
            return 1
        # Ako su oba dvoznamenkasta broja
        if((kartaRacunala[3] == kartaRacunala2[3]) and kartaRacunala[3] not in Card.CARDS_VALUE.keys()):
            return 1

        return 0

    def do(self, kartaRac1, kartaRac2):
        # Igrac
        cards = self.IgracRuka
        odigrajKartuIgrac = kartaRac1

        # Racunalo
        cards = self.racunaloRuka
        odigrajKartuRacunalo = kartaRac2

        if self.jeli_isti_tip(odigrajKartuIgrac, odigrajKartuRacunalo) == 1:
            return 1
        else:
            return 0

    def tkoNosiRukuSim(self, igracevaKarta, racunaloKarta, jeliIstiTip):
        if((type(igracevaKarta) and type(racunaloKarta)) != list):
            igracevaKarta.strip(" ")
            racunaloKarta.strip(" ")

        if((igracevaKarta[1] and igracevaKarta[2]) in Card.CARDS_VALUE.keys()):
            kartaIgrac = Card.CARDS_VALUE[str(
                igracevaKarta[1])+str(igracevaKarta[2])]
        else:
            kartaIgrac = Card.CARDS_VALUE[igracevaKarta[1]]

        if((racunaloKarta[1] and racunaloKarta[2]) in Card.CARDS_VALUE.keys()):
            kartaRacunalo = Card.CARDS_VALUE[str(
                racunaloKarta[1])+str(racunaloKarta[2])]
        else:
            kartaRacunalo = Card.CARDS_VALUE[racunaloKarta[1]]

        if(jeliIstiTip == 1):
            if(kartaIgrac > kartaRacunalo):
                if(Ruka.TkoJeDobioRuku == "human"):
                    # print("Igrac dobio ruku")
                    return "igrac"
                elif(Ruka.TkoJeDobioRuku == "AI"):
                    # print("Igrac dobio ruku")
                    return "igrac"

            elif(kartaIgrac < kartaRacunalo):
                if(Ruka.TkoJeDobioRuku == "human"):
                    # print("Racunalo dobilo ruku")
                    return "AI"
                elif(Ruka.TkoJeDobioRuku == "AI"):
                    # print("Racunalo dobilo ruku")
                    return "AI"
        else:
            if(kartaIgrac > kartaRacunalo):
                if(Ruka.TkoJeDobioRuku == "human"):
                    # print("Igrac dobio ruku")
                    return "igrac"
                elif(Ruka.TkoJeDobioRuku == "AI"):
                    # print("Racunalo dobilo ruku")
                    return "AI"

            elif(kartaIgrac < kartaRacunalo):
                if(Ruka.TkoJeDobioRuku == "human"):
                    # print("Igrac dobio ruku")
                    return "igrac"
                elif(Ruka.TkoJeDobioRuku == "AI"):
                    # print("Racunalo dobilo ruku")
                    return "AI"

            if(kartaIgrac == kartaRacunalo):
                if(Ruka.TkoJeDobioRuku == "human"):
                    # print("Igrac dobio ruku")
                    return"igrac"
                else:
                    # print("Racunalo dobilo ruku")
                    return "AI"

    def tkoNosiRuku(self, igracevaKarta, racunaloKarta, jeliIstiTip):
        igracevaKarta.strip(" ")
        racunaloKarta.strip(" ")
        if((igracevaKarta[1] and igracevaKarta[2]) in Card.CARDS_VALUE.keys()):
            kartaIgrac = Card.CARDS_VALUE[str(
                igracevaKarta[1])+str(igracevaKarta[2])]
        else:
            kartaIgrac = Card.CARDS_VALUE[igracevaKarta[1]]

        if((racunaloKarta[1] and racunaloKarta[2]) in Card.CARDS_VALUE.keys()):
            kartaRacunalo = Card.CARDS_VALUE[str(
                racunaloKarta[1])+str(racunaloKarta[2])]
        else:
            kartaRacunalo = Card.CARDS_VALUE[racunaloKarta[1]]

        if(jeliIstiTip == 1):
            if(kartaIgrac > kartaRacunalo):
                if(Ruka.TkoJeDobioRuku == "human"):
                    print("Igrac dobio ruku")
                    Ruka.igracDobioRuku = Ruka.igracDobioRuku+1
                    Ruka.TkoJeDobioRuku = "human"
                elif(Ruka.TkoJeDobioRuku == "AI"):
                    print("Igrac dobio ruku")
                    Ruka.igracDobioRuku = Ruka.igracDobioRuku+1
                    Ruka.TkoJeDobioRuku = "human"

            elif(kartaIgrac < kartaRacunalo):
                if(Ruka.TkoJeDobioRuku == "human"):
                    print("Racunalo dobilo ruku")
                    Ruka.RacunaloDobiloRuku = Ruka.RacunaloDobiloRuku+1
                    Ruka.TkoJeDobioRuku = "AI"
                elif(Ruka.TkoJeDobioRuku == "AI"):
                    print("Racunalo dobilo ruku")
                    Ruka.RacunaloDobiloRuku = Ruka.RacunaloDobiloRuku+1
                    Ruka.TkoJeDobioRuku = "AI"
        else:
            if(kartaIgrac > kartaRacunalo):
                if(Ruka.TkoJeDobioRuku == "human"):
                    print("Igrac dobio ruku")
                    Ruka.igracDobioRuku = Ruka.igracDobioRuku+1
                    Ruka.TkoJeDobioRuku = "human"
                elif(Ruka.TkoJeDobioRuku == "AI"):
                    print("Racunalo dobilo ruku")
                    Ruka.RacunaloDobiloRuku = Ruka.RacunaloDobiloRuku+1
                    Ruka.TkoJeDobioRuku = "AI"

            elif(kartaIgrac < kartaRacunalo):
                if(Ruka.TkoJeDobioRuku == "human"):
                    print("Igrac dobio ruku")
                    Ruka.igracDobioRuku = Ruka.igracDobioRuku+1
                    Ruka.TkoJeDobioRuku = "human"
                elif(Ruka.TkoJeDobioRuku == "AI"):
                    print("Racunalo dobilo ruku")
                    Ruka.RacunaloDobiloRuku = Ruka.RacunaloDobiloRuku+1
                    Ruka.TkoJeDobioRuku = "AI"

            if(kartaIgrac == kartaRacunalo):
                if(Ruka.TkoJeDobioRuku == "human"):
                    print("Igrac dobio ruku")
                    Ruka.igracDobioRuku = Ruka.igracDobioRuku+1
                    Ruka.TkoJeDobioRuku = "human"
                else:
                    print("Racunalo dobilo ruku")
                    Ruka.RacunaloDobiloRuku = Ruka.RacunaloDobiloRuku+1
                    Ruka.TkoJeDobioRuku = "AI"


class Treseta(Ruka):
    def __init__(self):
        print("Dobrodosli u tresetu \n")
        self.igra = Deck()
        self.igra.shuffle()
        self.IgracRuka = self.igra.deal(10)
        self.racunaloRuka = self.igra.deal(10)
        self.igraci = ["AI", "human"]
        self.tkoPrviIgra = choice(self.igraci)
        Ruka.TkoJeDobioRuku = self.tkoPrviIgra

        while(True):
            # Pregledaj ko je zadnju  ruku dobiu (napisi funkciju)
            bestRacunaloODabir = self.best_action()
            self.IgracRuka, self.racunaloRuka, igra = self.igranjeIgre(
                self.tkoPrviIgra, self.IgracRuka, self.racunaloRuka, self.igra, bestRacunaloODabir)
            if igra == 1:
                break
            self.tkoPrviIgra = Ruka.TkoJeDobioRuku

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
