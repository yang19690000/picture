import os
from PIL import Image
list=os.listdir()
for i in list:
    if '.py' in i:
	    continue
    if 'jfif' in i:   
     img = Image.open(i)
     img.save(i.replace('jfif','jpg'))
