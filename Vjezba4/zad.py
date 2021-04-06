import copy
import pprint
# Vuk koza kupus
# Vuk Koza Kupus ________
# 1. VUK KUPUS _______ KOZA
# 2, Odnosi kupus uzima kozu
# VUK ___KOZA___ KUPUS
# 3. Uzima vuka ostavlja kozu
# 4. Vraca se po kozu


class Stanje():
    _lijevaObala = ""
    _desnaObala = ""

    def __init__(self):
        self.stanjeIgre = "---O  ||  KBV"
        self.brojacLijeveStane = 3
        self.brojadDesneStrane = 0

    def __str__(self):
        return self.stanjeIgre

    def is_solved(self):
        string="VKBO"
        obala=list(Stanje._desnaObala)
        postojeLiCharovi = [characters in obala for characters in string]
        if all(postojeLiCharovi):
            return True
        else:
            return False

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
            mogucaStanja.append("VO-- ||  BK---")
            mogucaStanja.append("VK-- ||  BO---")
            mogucaStanja.append("OK-- ||  BV---")
        if(brojacD == 3):  # uvjet 0-3
            mogucaStanja.append("--VB || OK")
            mogucaStanja.append("--OB || VK")
            mogucaStanja.append("--KB || OV")

        lijevaObala = self.stanjeIgre.split("|", 1)[0]
        desnaObala = self.stanjeIgre.split("|", 1)[1]
        desnaObala = desnaObala[1:]
        desnaObala = desnaObala.strip()
        Stanje._desnaObala=desnaObala
        Stanje._lijevaObala=lijevaObala
        # print(desnaObala)

        # uvjet 2-1 i 1-2 dodavanje s jedne na drugu (s lijeve na desnu)
        if((brojacL == 2 and brojacD == 1) or (brojacL == 1 and brojacD == 2)):
            if "V" in lijevaObala:
                tempLijevaObala = lijevaObala.replace("V", "-",1)
                tempDesnaObala=desnaObala.replace("-","V",1)
                if "B" not in desnaObala:
                    tempDesnaObala=tempDesnaObala.replace('-',"B",1)
                tempLijevaObala=tempLijevaObala.replace("B","-",1)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if "O" in lijevaObala:
                tempLijevaObala = lijevaObala.replace("O", "-",1)
                tempDesnaObala=desnaObala.replace("-","O",1)
                if "B" not in desnaObala:
                    tempDesnaObala=tempDesnaObala.replace('-',"B",1)
                    tempLijevaObala=tempLijevaObala.replace("B","-",1)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if "K" in lijevaObala:
                tempLijevaObala = lijevaObala.replace("K", "-",1)
                tempDesnaObala=desnaObala.replace("-","K",1)
                if "B" not in desnaObala:
                    tempDesnaObala=tempDesnaObala.replace('-',"B",1)
                    tempLijevaObala=tempLijevaObala.replace("B","-",1)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            # Dodajemo s desne na lijevu
            if "V" in desnaObala:
                tempDesnaObala = desnaObala.replace("V", "-",1)
                tempLijevaObala=lijevaObala.replace("-","V",1)
                if "B" not in lijevaObala:
                    tempLijevaObala=tempLijevaObala.replace('-',"B",1)
                    tempDesnaObala=tempDesnaObala.replace("B","-",1)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if "O" in desnaObala:
                tempDesnaObala = desnaObala.replace("O", "-",1)
                tempLijevaObala=lijevaObala.replace("-","O",1)
                if "B" not in lijevaObala:
                    tempLijevaObala=tempLijevaObala.replace('-',"B",1)
                    tempDesnaObala=tempDesnaObala.replace("B","-",1)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if "K" in desnaObala:
                tempDesnaObala = desnaObala.replace("K", "-",1)
                tempLijevaObala=lijevaObala.replace("-","K",1)
                if "B" not in lijevaObala:
                    tempLijevaObala=tempLijevaObala.replace('-',"B",1)
                    tempDesnaObala=tempDesnaObala.replace("B","-",1)
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            # Napravi sad zamjene elemenata, prvo gledamo 2-1
            if (("V" in lijevaObala) and ("O" in lijevaObala)) and ("K" in desnaObala):
                tempDesnaObala = desnaObala.replace("K", "V")
                tempLijevaObala = lijevaObala.replace("V", "K")
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

                tempDesnaObala = desnaObala.replace("K", "O")
                tempLijevaObala = lijevaObala.replace("O", "K")
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if (("V" in lijevaObala) and ("K" in lijevaObala)) and ("O" in desnaObala):
                tempDesnaObala = desnaObala.replace("O", "V")
                tempLijevaObala = lijevaObala.replace("V", "O")
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

                tempDesnaObala = desnaObala.replace("O", "K")
                tempLijevaObala = lijevaObala.replace("K", "O")
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if (("O" in lijevaObala) and ("K" in lijevaObala)) and ("V" in desnaObala):
                tempDesnaObala = desnaObala.replace("V", "O")
                tempLijevaObala = lijevaObala.replace("O", "V")
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

                tempDesnaObala = desnaObala.replace("V", "K")
                tempLijevaObala = lijevaObala.replace("K", "V")
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            # gledamo 1-2
            if ("K" in lijevaObala) and (("V" in desnaObala) and ("O" in desnaObala)):
                tempDesnaObala = desnaObala.replace("V", "K")
                tempLijevaObala = lijevaObala.replace("K", "V")
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

                tempDesnaObala = desnaObala.replace("O", "K")
                tempLijevaObala = lijevaObala.replace("K", "O")
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if ("O" in lijevaObala) and (("V" in desnaObala) and ("K" in desnaObala)):
                tempDesnaObala = desnaObala.replace("V", "O")
                tempLijevaObala = lijevaObala.replace("O", "V")
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

                tempDesnaObala = desnaObala.replace("K", "O")
                tempLijevaObala = lijevaObala.replace("O", "K")
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

            if ("V" in lijevaObala) and (("O" in desnaObala) and ("K" in desnaObala)):
                tempDesnaObala = desnaObala.replace("O", "V")
                tempLijevaObala = lijevaObala.replace("V", "O")
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)

                tempDesnaObala = desnaObala.replace("K", "V")
                tempLijevaObala = lijevaObala.replace("V", "K")
                mogucaStanja.append(tempLijevaObala+"||"+"  "+tempDesnaObala)
        print(self.stanjeIgre)
        return mogucaStanja


if __name__ == '__main__':
    igra = Stanje()
    pprint.pprint(igra.next_states())
    print(igra.is_solved())
