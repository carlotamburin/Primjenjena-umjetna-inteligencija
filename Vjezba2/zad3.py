def zadatak():

    lista=[1,2,20,55,600,700]

    broj = int(input("Unesite broj za pretragu"))

    print("Element je na: {0} indexu".format(pretragaListe(0,len(lista),lista,broj)))










def pretragaListe(min,max,lista,el):

    zbroj=(min+max)//2

    if(min==zbroj):
        return
 
   

    if(lista[zbroj]>el):
       return pretragaListe(min,zbroj,lista,el)
  
    
    if (lista[zbroj]<el):
       return pretragaListe(zbroj,max,lista,el)

    

    if(lista[zbroj]==el):
        return zbroj

    

   

    


if __name__ == "__main__":
    zadatak()
