# CODE EXAMPLE :


# importam clasa Image din modulul PIL

from PIL import Image

# deschidem fisierul pentru modificare prin functia open()

im = Image.open('image.jpg')


# accesarea atributului size

dim = im.size 

print(dim) 


# redimensionare

im_resized = im.resize((100,200))

# salvarea imaginii redimensionate

im_resized.save('resized_image.png')


# redimensionare de trei ori mai mare

factor = 3

im_scale = im.resize((factor*dim[0], factor*dim[1]))

im_scale.save('scaled_image.png')


# rotirea imaginii

angle = 20

im_rot_right = im.rotate(angle)

im_rot_right.save('rotated_image_right.png')

im_rot_left = im.rotate(-angle)

# optiune mai jos pentru rotire fara pierdere de informatie

# im_rot_left = im.rotate(-angle, expand=True)

im_rot_left.save('rotated_image_left.png')


# convertire in RGBA pentru a obtine un fundal transparent

im_rgba = im.convert("RGBA")


# decuparea imaginii

im_cropped = im.crop((10, 10, 100, 100))

im_cropped.save('cropped_image.png')


# transformare in image alb negru

image_gray = im.convert('L')

image_gray.save('image_gray.jpg')


