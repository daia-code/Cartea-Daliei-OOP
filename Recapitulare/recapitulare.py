def afisaj():
 print("Recapitulare modul 1")
 print("Exercitiu calculator\n")

def adunare(a, b):
    return a + b

def scadere(a, b):
    return a - b

def inmultire(a, b):
    return a * b

def impartire(a, b):
    if b == 0:
        return "Eroare: nu se poate împărți la zero!"
    else:
        return a / b

while True:
    afisaj()
    print("Selectați operația:")
    print("1. Adunare")
    print("2. Scădere")
    print("3. Înmulțire")
    print("4. Împărțire")
    print("5. Ieșire")

    operatie = input("Introduceți numărul corespunzător operației: ")

    if operatie == '5':
        print("La revedere!")
        break

    if operatie not in ('1', '2', '3', '4'):
        print("Opțiune invalidă! Vă rugăm să selectați o opțiune validă.")
        continue

    numar1 = float(input("Introduceți primul număr: "))
    numar2 = float(input("Introduceți al doilea număr: "))

    if operatie == '1':
        rezultat = adunare(numar1, numar2)
    elif operatie == '2':
        rezultat = scadere(numar1, numar2)
    elif operatie == '3':
        rezultat = inmultire(numar1, numar2)
    elif operatie == '4':
        rezultat = impartire(numar1, numar2)

    print("Rezultatul este:", rezultat)
    print("\n")
