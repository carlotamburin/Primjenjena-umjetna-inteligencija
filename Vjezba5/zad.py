from random import choice


class igra():
    def __init__(self):
        self.pod = 11
        self.trenutniIgrac = "player"

    def __str__(self):
        return "Stapici na podu: " + str(self.pod) + "\nTrenutni igrac: " + self.trenutniIgrac

    def action(self, act):
        self.pod = self.pod-act

    def undoAction(self, act):
        self.pod = self.pod+act

    def all_actions(self):
        listaStanja = [1, 2]
        return listaStanja

    def isOver(self):
        if self.pod == 0:
            return True

        elif self.pod == 1:
            return False

        elif self.pod < 0:
            return False

        return 2

    def changePlayer(self):
        if self.trenutniIgrac == "computer":
            self.trenutniIgrac = "player"
        else:
            self.trenutniIgrac = "computer"


def miniMax(igra, d):
    result = igra.isOver()
    igrac = igra.trenutniIgrac
    if result != 2:
        if result == True:
            return(-100+d, None)
        elif result == False:
            return(100-d, None)
    if igrac == "player":
        maxv, best_act = -1000, None
        for a in igra.all_actions():
            igra.action(a)
            igra.changePlayer()
            v, _ = miniMax(igra, d+1)
            igra.undoAction(a)
            if v > maxv:
                maxv = v
                best_act = a
        return (maxv, best_act)
    else:
        minv, best_act = 1000, None
        for a in igra.all_actions():
            igra.action(a)
            igra.changePlayer()
            v, _ = miniMax(igra, d+1)
            igra.undoAction(a)
            if v < minv:
                minv = v
                best_act = a
        return (minv, best_act)


if __name__ == '__main__':
    igra = igra()

    while True:
        print(igra)
        akcija = int(input("Odaberi broj stapica za podic: "))
        igra.action(akcija)
        print("odabrano:", akcija)
        if igra.isOver() == True:
            print(igra.trenutniIgrac+" Je pobjednik")
            break
        elif igra.isOver() == False:
            print(igra.trenutniIgrac+" Je izgubio")
            break
        igra.changePlayer()
        print(igra)
        print("------------------------------")
        value, akcijaPC = miniMax(igra, 0)
        igra.action(akcijaPC)
        print("Racunalo igra {0}".format(akcijaPC))
        if igra.isOver() == True:
            print(igra.trenutniIgrac+" Je pobjednik")
            break
        elif igra.isOver() == False:
            print(igra.trenutniIgrac+" Je izgubilo")
            break
        igra.changePlayer()
        print(igra)
        print("------------------------------")
