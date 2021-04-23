import copy
import pprint
from random import choice
from collections import defaultdict, deque
from collections import OrderedDict
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

    def __init__(self, pocetnoStanje):
        self.lijevaObala = pocetnoStanje[:4]
        self.desnaObala = pocetnoStanje[-4:]

    def __str__(self):
        return self.lijevaObala + '  ||  ' + self.desnaObala

    def copy(self):
        return copy.deepcopy(self)

    def changeState(self, stanje):
        self.lijevaObala = stanje[:4]
        self.desnaObala = stanje[-4:]

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
            listaStanja.append(self.copy())
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
    if postojiLiUDictu(d, igra.__str__()):
        return False
    d[igra.__str__()] = igra
    if igra.is_terminal():
        return True
    for akcija in igra.all_actions():
        igra.action(akcija)
        generate(d, igra)
        igra.undo_action(akcija)
    return False


def postojiLiUDictu(d, element):
    lijevaStranaEl, desnaStranaEl = element[:4], element[-4:]
    if "B" in lijevaStranaEl:
        for el in d:
            if arePermutation(lijevaStranaEl, el[:4]) == True:
                return True
            else:
                continue
    else:
        for el in d:
            if arePermutation(desnaStranaEl, el[-4:]) == True:
                return True
            else:
                continue
    return False


def Dfs(igra, lista):
    ck = igra.copy()
    q = []
    visited = {}
    q.append((None, ck))
    while q:
        k = q.pop()
        ck = k[1].copy()
        if ck.is_solved():
            lista.append(k)
            return False
        if ck.is_terminal():
            continue
        if ck.__str__() not in visited:
            lista.append(k)
            visited[ck.__str__()] = ck
            igra.changeState(ck.__str__())
            for stanje in igra.next_states():
                q.append((ck, stanje.copy()))
    return visited


def Bfs(igra, lista):
    ck = igra.copy()
    q = []
    visited = {}
    q.append((None, ck))
    while q:
        k = q.pop(0)
        ck = k[1].copy()
        if ck.is_solved():
            lista.append(k)
            return False
        if ck.is_terminal():
            continue
        if ck.__str__() not in visited:
            lista.append(k)
            visited[ck.__str__()] = ck
            igra.changeState(ck.__str__())
            for stanje in igra.next_states():
                q.append((ck, stanje.copy()))
    return visited


def listaUdictNova(lista, dict):
    for el in lista:
        dict[el[0].__str__()].append(el[1].__str__())


def ispisPuta(d, zadnjiEl):
    put = []
    put.append(zadnjiEl)
    while arePermutation("".join(zadnjiEl[:4]), "VOKB") == False:
        for keys, values in d.items():
            if "B" in "".join(zadnjiEl[-4:]):
                if arePermutation("".join(choice(values)[-4:]), "".join(zadnjiEl)[-4:]):
                    zadnjiEl = keys
                    put.append(copy.deepcopy(zadnjiEl))
                    break
            else:
                if arePermutation("".join(choice(values)[:4]), "".join(zadnjiEl[:4])):
                    zadnjiEl = keys
                    put.append(copy.deepcopy(zadnjiEl))
                    break
    return put


def Bestfs(igra, lista, heuristic):
    ck = igra.copy()
    q = []
    visited = {}
    q.append((None, ck))
    while q:
        k = q.pop(0)
        ck = k[1].copy()
        if ck.is_solved():
            lista.append(k)
            return False
        if ck.is_terminal():
            continue
        if ck.__str__() not in visited:
            lista.append(k)
            visited[ck.__str__()] = ck
            igra.changeState(ck.__str__())
            for stanje in igra.next_states():
                q.append((ck, stanje.copy()))
            q = sorted(q, key=heuristic)
    return visited


def heuristic_1(state):
    h = state[1].__str__()
    h = h[-4:]
    brojac = 0
    for el in h:
        if el != "-":
            brojac = brojac+1
    return brojac


if __name__ == '__main__':
    # Deklariranje i inicijaliziranje varijabli
    d = {}
    d2 = defaultdict(list)
    d3 = defaultdict(list)
    d4 = OrderedDict()
    experimentDict = defaultdict(list)
    ListaStanja = []
    listaParentChild = []
    listaParentChildBfs = []
    experimentList = []
    # Pozivanje funkcija
    igra = Stanje("VOKB  ||  ----")
    print("Pocetno stanje: ", igra)
    print(igra.is_terminal())
    # stanjaMoguca, akcijeMoguce = igra.next_states()
    # pprint.pprint(stanjaMoguca)
    # print("Jeli igra rijesena: {0}".format(igra.is_solved()))
    # print("Jeli stanje konacno: ", igra.is_terminal())
    # kopiranoStanje = igra.copy()
    # print(igra.next_states())
    #akcije = igra.all_actions()
    # igra.action(akcije[0])

    # print(igra)
    # print(igra.is_terminal())
    # igra.undo_action(akcije[0])
    # print(igra)
    # print(igra.is_terminal())
    # generate(d, igra) ##
    # pprint.pprint(d)
    # print(len(d))

    igra = Stanje("VOKB  ||  ----")
    print("---------------------------------------------------")
    Dfs(igra, listaParentChild)
    listaUdictNova(listaParentChild, d2)
    pprint.pprint(d2)
    temp = list(d2)[-1:]
    temp = "".join(temp)
    put = ispisPuta(d2, d2[temp])
    put.reverse()
    pprint.pprint("THE REAL PUT FOR DFS IS:{0}".format(put))
    print("---------------------------------------------------")

    igra = Stanje("VOKB  ||  ----")
    Bfs(igra, listaParentChildBfs)
    listaUdictNova(listaParentChildBfs, d3)
    temp = list(d3)[-1:]
    temp = "".join(temp)
    #put = ispisPutaNovo(d3, d3[temp])
    put = ispisPuta(d3, d3[temp])
    pprint.pprint(d3)
    put.reverse()
    pprint.pprint("THE REAL PUT FOR BFS IS:{0}".format(put))
    print("---------------------------------------------------")

    igra = Stanje("VOKB  ||  ----")
    Bestfs(igra, experimentList, heuristic_1)
    listaUdictNova(experimentList, experimentDict)
    pprint.pprint(experimentDict)
    temp = list(experimentDict)[-1:]
    temp = "".join(temp)
    put = ispisPuta(experimentDict, experimentDict[temp])
    put.reverse()
    pprint.pprint("THE REAL PUT FOR BESTFS IS:{0}".format(put))
