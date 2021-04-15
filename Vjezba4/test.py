def provjeriRazliciteElemente(staroStanje, novoStanje):
    # usporeduj samo jednu obalu
    prebaceniElementi = ""
    a = sorted(staroStanje)
    str1 = "".join(a)
    b = sorted(novoStanje)
    str2 = "".join(b)

    s1 = set(str1)
    s2 = set(str2)
    prebaceniElementi = s1 & s2
    prebaceniElementi = "".join(prebaceniElementi)
    return prebaceniElementi


rezultat = provjeriRazliciteElemente("VK", "KOB")
print(rezultat)
