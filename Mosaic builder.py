from PIL import Image
import glob
import random
import datetime
import math

hoje = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

origin_folder="D:\\Wantanee farewell\\Small pictures\\*"
destination_path = 'D:\\Wantanee farewell\\'
background=Image.open("D:\\Wantanee farewell\\coloseo.jpg")
files_list=glob.glob(origin_folder)

#here is to analyze the images
#it prints the name of the images to be pasted on background, width, height, h/w ratio
hmaior=0
wmaior=0
images_orientation=[]
for i in files_list:
    im=Image.open(i)
    h1=im.size[1]
    w1=im.size[0]
    if h1>=w1:
        hmaior+=1
        images_orientation.append((i,'a'))
        print(i[-8:],w1,h1,str(h1/w1)[:5])
        if h1/w1 >=0.75:
            pass
    else:
        wmaior+=1
        images_orientation.append((i,'b'))
        print(i[-8:],h1,w1,str(h1/w1)[:5])
        
print(f'heigth is bigger {hmaior} times')
print(f'wide is bigger {wmaior} times')
images_orientation.sort(key=lambda tup: tup[1])  # sorts in place

#here is to adjust h x w ratio of landscape and portrait images, then paste the reduced size into the background
#basically we said all portraits h1/w1 must be 1.33 and landscapes h1/w1 must be 0.75.
#in order to obtain these ratios mentioned above, we cropped the images on the larger side (e.g. width in landscape)
a1=0
b1=0
background=Image.open("D:\\Wantanee farewell\\coloseo.jpg")
ratio=int(input('Please adjust the size of the pictures with values between 50 and 200'))/100.0
for jota in images_orientation:
    i=jota[0]
    im=Image.open(i)
    h1=im.size[1]
    w1=im.size[0]
    if h1>=w1:
        if h1/w1 >=1.33:

            reduction=math.sqrt(math.trunc(h1-w1/0.75)**2)
            h1=w1/0.75
            
            if reduction>20:
                im=im.crop((0,reduction/2,w1,h1-reduction/2))
            im=im.resize((math.trunc(160*ratio),math.trunc(213*ratio)))
            im.putalpha(128)
            if a1>background.size[0]:
                b1+=math.trunc(213*ratio)
                a1=0
            elif b1>background.size[1]:
                background.show()
                break
            background.paste(im,(a1,b1),im)

            print(a1)
            a1+=math.trunc(160*ratio)
                
                
                
        else:

            reduction=math.sqrt(math.trunc(w1-h1/1.33333)**2)
            w1=h1/1.33333
            

            if reduction>20:
                im=im.crop((0,reduction/2,w1,h1-reduction/2))
            im=im.resize((math.trunc(160*ratio),math.trunc(213*ratio)))
            im.putalpha(128)
            if a1>background.size[0]:
                b1+=math.trunc(213*ratio)
                a1=0
            elif b1>background.size[1]:
                background.show()
                break
            background.paste(im,(a1,b1),im)

            print(a1)
            a1+=math.trunc(160*ratio)
            
    else:

        if h1/w1 <=0.75:

            reduction=math.sqrt(math.trunc(w1-h1/0.75)**2)
            w1=h1/0.75
            if reduction>20:
                im=im.crop((0,reduction/2,w1,h1-reduction/2))
            im=im.resize((math.trunc(200*ratio),math.trunc(150*ratio)))
            im.putalpha(128)
            if a1>background.size[0]:
                b1+=math.trunc(150*ratio)
                a1=0
            elif b1>background.size[1]:
                background.show()
                break
            background.paste(im,(a1,b1),im)

            print(a1)
            a1+=math.trunc(200*ratio)
        else:

            reduction=math.sqrt(math.trunc(h1-w1/1.333333)**2)
            h1=w1/1.333333

            if reduction>20:
                im=im.crop((0,reduction/2,w1,h1-reduction/2))
            im=im.resize((math.trunc(200*ratio),math.trunc(150*ratio)))
            im.putalpha(128)
            if a1>background.size[0]:
                b1+=math.trunc(150*ratio)
                a1=0
            elif b1>background.size[1]:
                background.show()
                break
            background.paste(im,(a1,b1),im)

            print(a1)
            a1+=math.trunc(200*ratio)