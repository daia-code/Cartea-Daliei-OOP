from PIL import Image # Image apartine de PIL

# print(open("../PY_OOP/Sapt5/imagine_modificata.jpg"))
image=Image.open("../PY_OOP/Sapt5/gaming.jpg")
# image.show()
image2=image.convert("L") # convertire imagine si salvare in image2
image2.show() # afisare image2
