# EXEMPLU COD :

# importam un modul pentru a putea utiliza functia de parsare load

import json

# deschidem fisierul

with open("./Sapt2_3/example.json") as  file:

  # incarcam datele din fisier in variabila data

  data=json.load(file)
  print(data["person"])
