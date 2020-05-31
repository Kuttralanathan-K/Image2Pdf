
import os,os.path
from PIL import Image

valid_images = [".jpg",".gif",".png",".tga"]
img_dir = input("Enter image folder path: ")
pdf_name = input("Enter pdf name: ")
pdf_path = os.path.join(img_dir,pdf_name+".pdf")
imagelist=[]
path=[]
i=0
for f in os.listdir(img_dir):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    if i==0:
        im1=Image.open(os.path.join(img_dir,f))
        path.append(os.path.join(img_dir,f))
        if im1.mode == 'RGBA':
            im1 = im1.convert('RGB')
        i=i+1
    else:
        im=Image.open(os.path.join(img_dir,f))
        path.append(os.path.join(img_dir,f))
        if im.mode == 'RGBA':
            im = im.convert('RGB')
        imagelist.append(im)
print(path)
im1.save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=imagelist)


'''
Convert each image to pdf

import os
from PIL import Image

page = 1
folder = input("Enter image folder path: ")
for pic in os.listdir(folder):
    if pic.endswith('.png') or pic.endswith('.jpg'):
        img = Image.open(os.path.join(folder,pic))
        pdfTitle = os.path.join(folder,'pdfs','{}.pdf'.format(page))
        img.save(pdfTitle)
        page += 1
'''

