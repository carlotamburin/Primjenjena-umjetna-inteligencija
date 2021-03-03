def zadatak():
    prviBroj=int(input("Unesite prvi broj"))
    drugiBroj=int(input("Unesite drugi broj"))
    broj1=prviBroj
    broj2=drugiBroj
    tempPrviBroj=0
    tempDrugiBroj=0
    flag=0

    radSBrojevima(prviBroj,drugiBroj)

    

zadatak()

def postojBroj(broj1,broj2):
    while(broj2!=0):
        
        if(broj2==broj1):
            return True

def radSBrojevima(broj1,broj2):
    tempBroj2=0
    tempBroj1=0

    while(broj1!=0):
        tempBroj1=broj1%10

        while(broj2!=0):
            tempBroj2=broj2%10
            postojBroj(tempBroj1,tempBroj2)
            broj2=broj2 //10

        broj1=broj1 //10


