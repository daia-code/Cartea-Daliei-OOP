class Persoana:

  # constructor
  

  def __init__(self, nume, varsta, inaltime):

    # atribute

    self.nume = nume

    self.varsta = varsta

    self.inaltime = inaltime

  def afisare(self):
    print('Ma numesc ' +self.nume+' am '+ str(self.varsta) +' ani si inaltimea de '+str(self.inaltime)+' m.')
    print(f'{self.nume}')
    

baiat = Persoana("Alex", 12, 1.34)

fata = Persoana("Diana", 13, 1.2)


# Str="hello wolrd"
# json={
#     "persoane":{
#         0:{
#             "name":"John", "age":30, "car":"Mercedes"
#         }
#     }
# }
# print(json["name"])

# class Familie:

#     def __init__(self, nume_tata, nume_mama, lista_copii):

#         self.nume_tata = nume_tata

#         self.nume_mama = nume_mama

#         self.lista_copii = lista_copii


#     def afiseaza_copii(self):

#         copii = ', '.join(self.lista_copii)

#         print(f"Copiii lui {self.nume_mama} și {self.nume_tata} sunt {copii}")



# # Exemplu de utilizare a clasei Familie

# familia_popescu = Familie("George", "Daniela", ["Dan", "George", "Ștefan"])

# familia_popescu.afiseaza_copii()  # Afișează "Copii lui Daniela și George sunt Dan, George, Ștefan"

# class Familie:
#     def __init__(self,mama,tata,copii):
#         self.mama = mama
#         self.tata = tata
#         self.copii = copii

#     def afisare(self):
#         print('Mama este' + self.mama +',tata este'+ self.tata + ',iar copii sunt' + self.copii)
 
# familiaC = Familie('Daniela',"George",["Stefan","Stefan"])
# familiaC.afisare()

class Fructe:

    def __init__(self, nume, dimensiune):

        self.nume = nume

        self.dimensiune = dimensiune



lista_fructe_mici = []

lista_fructe_mijlocii = []

lista_fructe_mari = []

while True:

    # Citirea atributelor de la tastatura

    nume = input("Introduceti numele fructului: ")

    dimensiune = input("Introduceti dimensiunea fructului (mic, mijlociu, mare): ")


    # Crearea unei instante a clasei Fructe

    fruct = Fructe(nume, dimensiune)

    # Adaugarea fructului in lista corespunzatoare dimensiunii

    if fruct.dimensiune == 'mic':

        lista_fructe_mici.append(fruct)

    elif fruct.dimensiune == 'mijlociu':

        lista_fructe_mijlocii.append(fruct)

    elif fruct.dimensiune == 'mare':

        lista_fructe_mari.append(fruct)

    else:

        print("Dimensiunea introdusa nu este valida. Fructul nu a fost adaugat în lista.")

    raspuns = input("Doriti sa continuati citirea fructelor? (da/nu) ")

    if raspuns.lower() == 'nu':

        break
      
