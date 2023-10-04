class Student:

    def __init__(self, namn, efternamn, personnr):
        self.förnamn = namn
        self.efternamn = efternamn
        self.personnr = personnr
        self.id = 1
        
    def __str__(self):
        return f"Namn: {self.förnamn} {self.efternamn} Personnr: {self.personnr}"
    
    def skapa_student(self): 
        förnamn = input("Vad är studentens förnamn? ")
        efternamn = input("Vad är personens efternamn? ")
        while True:
            try:
                personnr = int(input("Vad är studentens personnummer? "))
                if len(str(personnr)) != 12:
                    print("Personnr ska vara 12 siffror")
                else: 
                    break
            except ValueError:
                print("Fel datatyp, använd endast siffror i heltal")
            
        print("Student skapad!")
        return  Student(förnamn, efternamn, personnr)
    
    #def öka_id(id): #funkar inte heller
        id += 1
    
    def lista_införing(self, u_lista, id):
        self.id += 1
        print(f"Studenten ha ID: {id}")
        u_lista[id] = Student(self.förnamn, self.efternamn, self.personnr) #tilldelar unik ID till nya elever 
        
    def söka_elev(u_lista): #funkar
        while True:
            try:
                välj_elev = int(input("Skriv in studentens ID-nummer: "))
                print(u_lista[välj_elev])
                break
            except KeyError:
                print(f"Student med ID-nummer {välj_elev} finns inte")
            except ValueError:
                print("Fel datatyp, använd endast siffror i heltal")
        
    def ta_bort_student(u_lista): #används inte än
        while True:
            try:
                skriv_nummer = int(input("Skriv ID-nummer för den student du vill ta bort: "))
                print(f"Studenten, {u_lista[skriv_nummer]}, togs bort")
                u_lista.pop(skriv_nummer)
            except KeyError:
                print(f"Student med ID-nummer {skriv_nummer} finns inte")
            except ValueError:
                print("Fel datatyp, använd endast siffror i heltal")
    
    def visa_studenter(u_lista):
        print("Här är alla studenter:")
        for id in u_lista:
            print(u_lista[id])

#gör att man kan starta om
def tillbaka():
    while True:
        val = input("Tillbaka till huvudmenyn? (ja/nej) ")
        if val == "ja":
            return True #ger upphov till continue i main()
        elif val == "nej": #behöver nästan 2 break efter varandra, för att koden ger samma sak som ja
            print("Tack, vi ses nästa gång.")
            return False #ger upphov till break i main()
        else:
            print("svara med ja eller nej") 

def meny():
        print("Välkommen till skolans databas")
        print("1. Skapa en ny student")
        print("2. Sök efter en student")
        print("3. Se alla studenter")
        print("4. Ta bort en student")
        while True:
            try:
                val = float(input("Vad vill du göra? "))
                return val
            except ValueError:
                print("Fel datatyp, skriv ett av siffrorna i menyn")
                
