
#!/usr/bin/env python3
from PIL import Image, ImageFile
import os
import subprocess


src = os.listdir('{your images directory}')
for file in src:
    outfile = os.path.splitext(file)[0] 
    source = "{your image directory}"+outfile
    print(source)
    try:
      with Image.open(source) as im :
       step1 = im.resize((x,y)) # x and y 
       step2 = step1.rotate(z) # z 
       rgb_im = step2.convert('RGB')
       rgb_im.save(source,'JPEG')
       subprocess.call(['cp',source,'{destination}'])
    except IOError:
      print("cannot create ", file)

