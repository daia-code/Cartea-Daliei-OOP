# EXEMPLU COD :

# importam un modul

import json

# cream un obiect json

data = {

    "nume":"Alex",

    "varsta":13,

    "pasiuni":["jocuri video","citit","bicicleta"]

}

# deschidem fisierul in modul scriere (w)

with open("./Sapt2_3/example2.json", "w") as file:

# scriem în fișier

  json.dump(data, file)
