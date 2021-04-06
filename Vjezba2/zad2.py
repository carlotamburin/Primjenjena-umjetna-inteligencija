def zadatak():
    prviBroj = int(input("Unesite prvi broj"))
    drugiBroj = int(input("Unesite drugi broj"))

    if(radSBrojevima(prviBroj, drugiBroj) and radSBrojevima(drugiBroj, prviBroj)):
        print("Sve znamenke prvog broja postoje u drugom i obrnuto")
    



def radSBrojevima(broj1,broj2):

    if(broj1==0):
        return True

    if jeliZnamenkaUBroju(broj1%10,broj2):
       return radSBrojevima(broj1//10,broj2)


    # Ako igdje ne nade i ne ude u gornji if (ne zadovolji ga) izaci ce sa return false a ako je dosao do kraja broj==0 i vraca true, nasa je sve
    return False







def jeliZnamenkaUBroju(broj1,broj2):
    if broj2==0:
        return False

    if broj1==broj2%10:
        return True

    
    return jeliZnamenkaUBroju(broj1,broj2//10)

    













if __name__ == "__main__":
    zadatak()
