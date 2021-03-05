def zadatak():
    prviBroj = int(input("Unesite prvi broj"))
    drugiBroj = int(input("Unesite drugi broj"))

    if(radSBrojevima(prviBroj, drugiBroj) and radSBrojevima(drugiBroj, prviBroj)):
        print("Sve znamenke prvog broja postoje u drugom i obrnuto")


def postojBroj(broj1, broj2):
    tempbroj2 = 0
    while(broj2 != 0):
        tempbroj2 = broj2 % 10
        if(tempbroj2 == broj1):
            return True
        broj2 = broj2//10


def radSBrojevima(broj1, broj2):
    tempBroj1 = 0
    brojacPostojecihBrojeva = 0
    brojacZnamenkiUBroju = 0

    while(broj1 != 0):
        tempBroj1 = broj1 % 10
        if postojBroj(tempBroj1, broj2):
            brojacPostojecihBrojeva = brojacPostojecihBrojeva+1
        broj1 = broj1 // 10
        brojacZnamenkiUBroju = brojacZnamenkiUBroju+1

    if(brojacPostojecihBrojeva == brojacZnamenkiUBroju):
        return True


if __name__ == "__main__":
    zadatak()
