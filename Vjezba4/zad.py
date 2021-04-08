import copy
import pprint
from random import choice
# Vuk koza kupus
# Vuk Koza Kupus ________
# 1. VUK KUPUS _______ KOZA
# 2, Odnosi kupus uzima kozu
# VUK ___KOZA___ KUPUS
# 3. Uzima vuka ostavlja kozu
# 4. Vraca se po kozu

def provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala):
    if "B" not in lijevaObala:
        if "B" in desnaObala:
            tempLijevaObala = tempLijevaObala.replace('-', "B", 1)
            tempDesnaObala = tempDesnaObala.replace("B", "-", 1)

    elif "B" not in desnaObala:
        if "B" in lijevaObala:
            tempDesnaObala = tempDesnaObala.replace('-', "B", 1)
            tempLijevaObala = tempLijevaObala.replace("B", "-", 1)
    

class Stanje():
    _lijevaObala = ""
    _desnaObala = ""

    def __init__(self):
        self.stanjeIgre = "----  ||  VOBK"
        self.brojacLijeveStane = 3
        self.brojadDesneStrane = 0

    def __str__(self):
        return self.stanjeIgre

    def vrati_odvojene_obale(self):
        lijevaObala = self.stanjeIgre.split("|", 1)[0]
        desnaObala = self.stanjeIgre.split("|", 1)[1]
        desnaObala = desnaObala[1:]
        desnaObala = desnaObala.strip()
        Stanje._desnaObala = desnaObala
        Stanje._lijevaObala = lijevaObala

        return lijevaObala, desnaObala

    def is_solved(self):
        string = "VKBO"
        obala = list(Stanje._desnaObala)
        postojeLiCharovi = [characters in obala for characters in string]
        if all(postojeLiCharovi):
            return True
        else:
            return False

    def is_terminal(self):
        lijevObala, desnaObala = self.vrati_odvojene_obale()
        obalaD = list(desnaObala)
        obalaL = list(lijevObala)
        if self.is_solved():
            return True

        provjeraRjesenjaDesno = [characters in obalaD for characters in "VO"]
        provjeraRjesenjaLijevo = [characters in obalaL for characters in "VO"]
        if all(provjeraRjesenjaDesno) or all(provjeraRjesenjaLijevo):
            return True

        provjeraRjesenjaDesno = [characters in obalaD for characters in "OK"]
        provjeraRjesenjaLijevo = [characters in obalaL for characters in "OK"]
        if all(provjeraRjesenjaDesno) or all(provjeraRjesenjaLijevo):
            return True
        return False

    def action(self, stanje):
        self.stanjeIgre = choice(stanje)

    def copy(self):
        kopijaStanja = copy.deepcopy(self.stanjeIgre)
        return kopijaStanja

    def undo_action(self, kopija):
        self.stanjeIgre = kopija

    def next_states(self):
        brojacL = 0
        brojacD = 0
        strana = "lijeva"
        mogucaStanja = []

        tempLijevaObala = ""
        tempDesnaObala = ""

        for el in self.stanjeIgre:
            if el == "|":
                strana = "desna"
                continue
            if(strana == "lijeva"):
                if el == "V" or el == "O" or el == "K":
                    brojacL = brojacL+1
            elif(strana == "desna"):
                if el == "V" or el == "O" or el == "K":
                    brojacD = brojacD+1

        if(brojacL == 3):  # uvjet 3-0
            mogucaStanja.append("VO-- ||  BK--")
            mogucaStanja.append("VK-- ||  BO--")
            mogucaStanja.append("OK-- ||  BV--")
        if(brojacD == 3):  # uvjet 0-3
            mogucaStanja.append("--VB || --OK")
            mogucaStanja.append("--OB || --VK")
            mogucaStanja.append("--KB || --OV")

        lijevaObala = self.stanjeIgre.split("|", 1)[0]
        desnaObala = self.stanjeIgre.split("|", 1)[1]
        desnaObala = desnaObala[1:]
        desnaObala = desnaObala.strip()

        Stanje._desnaObala = desnaObala
        Stanje._lijevaObala = lijevaObala
        # print(desnaObala)

        # uvjet 2-1 i 1-2 dodavanje s jedne na drugu (s lijeve na desnu)
        if((brojacL == 2 and brojacD == 1) or (brojacL == 1 and brojacD == 2)):
            if "V" in lijevaObala:
                tempLijevaObala = lijevaObala.replace("V", "-", 1)
                tempDesnaObala = desnaObala.replace("-", "V", 1)
                provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if "O" in lijevaObala:
                tempLijevaObala = lijevaObala.replace("O", "-", 1)
                tempDesnaObala = desnaObala.replace("-", "O", 1)
                provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if "K" in lijevaObala:
                tempLijevaObala = lijevaObala.replace("K", "-", 1)
                tempDesnaObala = desnaObala.replace("-", "K", 1)
                provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            # Dodajemo s desne na lijevu
            if "V" in desnaObala:
                tempDesnaObala = desnaObala.replace("V", "-", 1)
                tempLijevaObala = lijevaObala.replace("-", "V", 1)
                provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if "O" in desnaObala:
                tempDesnaObala = desnaObala.replace("O", "-", 1)
                tempLijevaObala = lijevaObala.replace("-", "O", 1)
                provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if "K" in desnaObala:
                tempDesnaObala = desnaObala.replace("K", "-", 1)
                tempLijevaObala = lijevaObala.replace("-", "K", 1)
                provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            # Napravi sad zamjene elemenata, prvo gledamo 2-1
            if (("V" in lijevaObala) and ("O" in lijevaObala)) and ("K" in desnaObala):
                tempDesnaObala = desnaObala.replace("K", "V")
                tempLijevaObala = lijevaObala.replace("V", "K")
                #provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

                tempDesnaObala = desnaObala.replace("K", "O")
                tempLijevaObala = lijevaObala.replace("O", "K")
                #provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if (("V" in lijevaObala) and ("K" in lijevaObala)) and ("O" in desnaObala):
                tempDesnaObala = desnaObala.replace("O", "V")
                tempLijevaObala = lijevaObala.replace("V", "O")
                #provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

                tempDesnaObala = desnaObala.replace("O", "K")
                tempLijevaObala = lijevaObala.replace("K", "O")
                #provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if (("O" in lijevaObala) and ("K" in lijevaObala)) and ("V" in desnaObala):
                tempDesnaObala = desnaObala.replace("V", "O")
                tempLijevaObala = lijevaObala.replace("O", "V")
                #provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

                tempDesnaObala = desnaObala.replace("V", "K")
                tempLijevaObala = lijevaObala.replace("K", "V")
                #provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            # gledamo 1-2
            if ("K" in lijevaObala) and (("V" in desnaObala) and ("O" in desnaObala)):
                tempDesnaObala = desnaObala.replace("V", "K")
                tempLijevaObala = lijevaObala.replace("K", "V")
                #provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

                tempDesnaObala = desnaObala.replace("O", "K")
                tempLijevaObala = lijevaObala.replace("K", "O")
                #provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if ("O" in lijevaObala) and (("V" in desnaObala) and ("K" in desnaObala)):
                tempDesnaObala = desnaObala.replace("V", "O")
                tempLijevaObala = lijevaObala.replace("O", "V")
                #provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

                tempDesnaObala = desnaObala.replace("K", "O")
                tempLijevaObala = lijevaObala.replace("O", "K")
                #provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if ("V" in lijevaObala) and (("O" in desnaObala) and ("K" in desnaObala)):
                tempDesnaObala = desnaObala.replace("O", "V")
                tempLijevaObala = lijevaObala.replace("V", "O")
                #provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

                tempDesnaObala = desnaObala.replace("K", "V")
                tempLijevaObala = lijevaObala.replace("V", "K")
                #provjeraBroda(lijevaObala,desnaObala,tempLijevaObala,tempDesnaObala)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)
        return mogucaStanja


def generate(d, visited):
    for stanje in igra.next_states():
        igra.action([stanje])
        d[stanje] = igra
        if stanje not in visited:
            visited.append(stanje)
        else:
            return
        generate(d, visited)
        igra.undo_action(igra.copy())




if __name__ == '__main__':
    # Deklariranje i inicijaliziranje varijabli
    brojac = 10
    d = {}
    visited = []

    # Pozivanje funkcija
    igra = Stanje()
    print("Pocetno stanje: ", igra)
    stanjaMoguca = igra.next_states()
    pprint.pprint(stanjaMoguca)
    print("Jeli igra rijesena: {0}".format(igra.is_solved()))
    print("Jeli stanje konacno: ", igra.is_terminal())
    kopiranoStanje = igra.copy()
    igra.action(stanjaMoguca)
    print("Promjenjeno stanje: ", igra)
    igra.undo_action(kopiranoStanje)
    print("Promjenjeno stanje nazad s undo-om: ", igra)
    generate(d, visited)
    pprint.pprint(visited)
    print(len(visited))
