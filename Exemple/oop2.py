class Familie:
    def __init__(self, mama, tata, copiii):
        self._mama = mama
        self.tata = tata
        self.copiii = copiii

    @property
    def mama(self):
        return self._mama
    
    @mama.setter
    def mama(self, value):
        self._mama = value

    def informatii(self):
        print(f'Familia mea este formata din: mama {self.mama}, tata {self.tata} si copiii {", ".join(self.copiii)}.')

def main():
    familie1 = Familie("Maria", "Andrei", ["Mihai", "Adela"])
    print(f'Pe mama mea o cheama {familie1.mama}')
    familie1.mama = "Elena"
    print(f'Acum pe mama mea o cheama {familie1.mama}')
    familie1.informatii()

main()
