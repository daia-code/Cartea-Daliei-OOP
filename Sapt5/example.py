from PIL import Image,ImageOps

image=Image.open('../PY_OOP/Sapt5/imagine_modificata.jpg')
#image.show()
mod_img=image.convert('L') #convertire imagine alb-negru
#mod_img.show
#img=Image.blend(image,mod_img,alpha=0.5) 
# alpha ar fi procentajul din imagine combiant cred

image2=ImageOps.expand(image,border=10,fill='blue')
image2.show()
