from class_uppslagslista import Student as s
from class_uppslagslista import *
#problem: när man går tillbaks till menyn stannar allt annat 
#gör felhantering en definiion som rerturnerar break

    
def main():
    id_nummer = 0
    id_lista = {}
    
    while True:
        val0 = meny()
        if val0 == 1:
            person = s.skapa_student()
            #s.öka_id(id_nummer)
            s.lista_införing(person, id_lista, id_nummer)
            
            while True:
                val1 = input("Vill du lägga till en student (ja/nej) ")
                if val1 == "ja":
                    person2 = s.skapa_student()
                    #s.öka_id(id_nummer)
                    s.lista_införing(person2, id_lista, id_nummer)
                elif val1 == "nej":
                    break
                else:
                    print("Svara med ja eller nej")
            
            val2 = tillbaka()
            if val2 == True:
                continue
            else:
                break
        
        elif val0 == 2:
            s.söka_elev(id_lista)
            
            val3 = tillbaka()
            if val3 == True:
                continue
            else:
                break
            
        elif val0 == 3:
            s.visa_studenter(id_lista)
            
            val5 = tillbaka()
            if val5 == True:
                continue
            else:
                break

        elif val0 == 4:
            s.ta_bort_student(id_lista)
            
            val4 = tillbaka()
            if val4 == True:
                continue
            else:
                break
                
        elif val0 == 10: #test för att se vilka om allt sparas på rätt sätt, vilket det för tillfället inte gör
            s.studenter(id_lista)
            
        else:
            print("svara med siffror mellan 0 och 4")

    print(f"-[{id_nummer}]-") #lite info för programmeraren hur långt id_nummer räkningen har gått om det går bra

main()