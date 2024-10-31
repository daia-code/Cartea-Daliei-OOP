import json

# Funcția noastră creativă și magică pentru a genera un fișier JSON
def creeaza_json():
    # Informații speciale despre persoană
    date_persoana = {
        "nume": "Maria",
        "varsta": 11,
        "clasa": "a 5-a",
        "hobby-uri": ["citit", "pictură", "baschet"]
    }
    
    # Salvăm datele într-un fișier JSON super-organizat!
    with open("date_persoana.json", "w") as fisier:
        json.dump(date_persoana, fisier, indent=4)
    print("Fișierul JSON a fost creat cu succes! 🎉")

# Apelăm funcția pentru a crea JSON-ul
creeaza_json()
