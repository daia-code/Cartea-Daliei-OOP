class Familie:
    def __init__(self, mama, tata, copiii):
        # Inițializează membrii familiei
        self._mama = mama  # Utilizează un atribut privat pentru mama
        self.tata = tata
        self.copiii = copiii

    @property
    def mama(self):
        # Metodă getter pentru mama
        return self._mama
    
    @mama.setter
    def mama(self, value):
        # Metodă setter pentru mama
        self._mama = value

    def informatii(self):
        # Metodă pentru a afișa informațiile despre familie
        print(f'Familia mea este formată din: mama {self.mama}, tata {self.tata} și copiii {", ".join(self.copiii)}.')

def main():
    # Creează o instanță a clasei Familie
    familie1 = Familie("Maria", "Andrei", ["Mihai", "Adela"])
    # Afișează numele mamei
    print(f'Pe mama mea o cheamă {familie1.mama}')
    # Schimbă numele mamei
    familie1.mama = "Elena"
    # Afișează noul nume al mamei
    print(f'Acum pe mama mea o cheamă {familie1.mama}')
    # Afișează informațiile despre familie
    familie1.informatii()

# Apelează funcția main pentru a executa codul
main()

