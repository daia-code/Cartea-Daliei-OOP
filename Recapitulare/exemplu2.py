class Joc:
    def __init__(self,nume,categorie,producator):
        self.nume=nume
        self.categorie=categorie
        self.producator=producator
    
    def info_joc(self):
        print(f'Azi am terminat un nou nivel din {self.nume} , categorie - {self.categorie} si este produs de {self.producator}')


nume=input("Introduceti un nume Jocului")
categorie=input("Introduceti un nume Jocului")
producator=input("Introduceti un nume Jocului")
joc1 = Joc(nume, categorie, producator)
print (joc1.info_joc())
