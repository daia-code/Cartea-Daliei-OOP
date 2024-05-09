class Activitate:
    def __init__(self,nume_activitate): 
        #self face referire la atributul din clasa (self.nume_activitate)
        #nume_activitate este parametrul care va fi dat in momentul instantierii adica actv=Activitate("fotbal")
        self.nume_activitate=nume_activitate
    
    def ce_fac(self):
        ''''
        la fiecare functie se scrie self. (atributul nostru) deoarece asa il recunoaste clasa noastra,
          self.nume_activitate ia valoarea lui nume_activitate(doar in init este utilizat)

          ***orice variabila daca nu este globala sau nu este trimisa ca parametru in functie nu este vizibila din exterior***
        '''
        return f'La primul antrenament de {self.nume_activitate} am dat primul gol'
        '''
        oricand folosim return doar ceva se returneaza, pentru a putea vedea ce s-a returnat
        Avem 2 metode:
        1. print(actv.ce_fac())
        2. mesaj=actv.ce_fac()
           print(mesaj)
        '''

actv = Activitate('fotbal')
print(actv.ce_fac())
