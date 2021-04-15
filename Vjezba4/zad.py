import copy
import pprint
from random import choice
from collections import deque
# Vuk Koza Kupus ________
# 1. VUK KUPUS _______ KOZA
# 2, Odnosi kupus uzima kozu
# VUK ___KOZA___ KUPUS
# 3. Uzima vuka ostavlja kozu
# 4. Vraca se po kozu


def arePermutation(str1, str2):

    # Get lenghts of both strings
    n1 = len(str1)
    n2 = len(str2)

    # If length of both strings is not same,
    # then they cannot be Permutation
    if (n1 != n2):
        return False

    # Sort both strings
    a = sorted(str1)
    str1 = " ".join(a)
    b = sorted(str2)
    str2 = " ".join(b)

    # Compare sorted strings
    if a == b:
        return True

    return False


class Stanje():

    def __init__(self, pocetnoStanje="VOKB  ||  ----"):
        self.lijevaObala = pocetnoStanje[:4]
        self.desnaObala = pocetnoStanje[-4:]

    def __str__(self):
        return self.lijevaObala + '  ||  ' + self.desnaObala

    def copy(self):
        return copy.deepcopy(self)

    def is_solved(self):
        string = "VKBO"
        obala = list(self.desnaObala)
        postojeLiCharovi = [characters in obala for characters in string]
        if all(postojeLiCharovi):
            return True
        else:
            return False

    def is_terminal(self):
        obalaD = list(self.desnaObala)
        obalaL = list(self.lijevaObala)
        if self.is_solved():
            return True

        if self.lijevaObala == "VOKB":
            return False

        provjeraRjesenjaDesno = [characters in obalaD for characters in "VO"]
        provjeraRjesenjaLijevo = [characters in obalaL for characters in "VO"]
        if all(provjeraRjesenjaDesno) and "B" not in obalaD:
            return True
        if all(provjeraRjesenjaLijevo) and "B" not in obalaL:
            return True

        provjeraRjesenjaDesno = [characters in obalaD for characters in "OK"]
        provjeraRjesenjaLijevo = [characters in obalaL for characters in "OK"]
        if all(provjeraRjesenjaDesno) and "B" not in obalaD:
            return True
        if all(provjeraRjesenjaLijevo) and "B" not in obalaL:
            return True

        return False

    def undo_action(self, action):
        if action in self.lijevaObala:
            if action == "B":
                self.lijevaObala = self.lijevaObala.replace(action, "-", 1)
                self.desnaObala = self.desnaObala.replace("-", action, 1)
            else:
                self.lijevaObala = self.lijevaObala.replace(action, '-', 1)
                self.desnaObala = self.desnaObala.replace("-", action, 1)
                self.lijevaObala = self.lijevaObala.replace("B", "-", 1)
                self.desnaObala = self.desnaObala.replace("-", "B", 1)

        else:
            if action == "B":
                self.desnaObala = self.desnaObala.replace(action, "-", 1)
                self.lijevaObala = self.lijevaObala.replace("-", action, 1)

            else:
                self.desnaObala = self.desnaObala.replace(action, "-", 1)
                self.lijevaObala = self.lijevaObala.replace("-", action, 1)
                self.desnaObala = self.desnaObala.replace("B", "-", 1)
                self.lijevaObala = self.lijevaObala.replace("-", "B", 1)

    def all_actions(self):
        listaAkcija = []

        if "B" in self.lijevaObala:
            for el in self.lijevaObala:
                if el != "-":
                    listaAkcija.append(el)
        else:
            for el in self.desnaObala:
                if el != "-":
                    listaAkcija.append(el)

        return listaAkcija

    def next_states(self):
        listaStanja = []

        for akcija in self.all_actions():
            self.action(akcija)
            # MOzes  self stavit pa posli __str__
            listaStanja.append(self.__str__())
            self.undo_action(akcija)

        return listaStanja

    def action(self, action):

        if action in self.lijevaObala:
            if action == "B":
                self.lijevaObala = self.lijevaObala.replace(action, "-", 1)
                self.desnaObala = self.desnaObala.replace("-", action, 1)
            else:
                self.lijevaObala = self.lijevaObala.replace(action, "-", 1)
                self.desnaObala = self.desnaObala.replace("-", action, 1)
                self.lijevaObala = self.lijevaObala.replace("B", "-", 1)
                self.desnaObala = self.desnaObala.replace("-", "B", 1)

        else:
            if action == "B":
                self.desnaObala = self.desnaObala.replace(action, "-", 1)
                self.lijevaObala = self.lijevaObala.replace("-", action, 1)
            else:
                self.desnaObala = self.desnaObala.replace(action, "-", 1)
                self.lijevaObala = self.lijevaObala.replace("-", action, 1)
                self.desnaObala = self.desnaObala.replace("B", "-", 1)
                self.lijevaObala = self.lijevaObala.replace("-", "B", 1)


def generate(d, igra):
    if igra.is_terminal():
        return True
    for akcija in igra.all_actions():
        igra.action(akcija)
        for el in d:
            if arePermutation(el, igra.__str__()) == True:
                continue
            else:
                d[igra.__str__()] = igra
        if not d:
            d[igra.__str__()] = igra
        rezultat = generate(d, igra)
        igra.undo_action(akcija)
        if rezultat:
            return True
    return False


if __name__ == '__main__':
    # Deklariranje i inicijaliziranje varijabli
    d = {}
    # Pozivanje funkcija
    igra = Stanje("VOB- || -K--")
    print("Pocetno stanje: ", igra)
    print(igra.is_terminal())
    #stanjaMoguca, akcijeMoguce = igra.next_states()
    # pprint.pprint(stanjaMoguca)
    #print("Jeli igra rijesena: {0}".format(igra.is_solved()))
    #print("Jeli stanje konacno: ", igra.is_terminal())
    #kopiranoStanje = igra.copy()
    print(igra.next_states())
    akcije = igra.all_actions()
    igra.action(akcije[0])

    print(igra)
    print(igra.is_terminal())
    igra.undo_action(akcije[0])
    print(igra)
    print(igra.is_terminal())
    generate(d, igra)
    pprint.pprint(d)
    #akcija = igra.action(choice(stanjaMoguca))
    # igra.undo_action(akcija)
