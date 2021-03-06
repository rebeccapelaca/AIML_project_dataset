import random
import os
from PIL import Image
import numpy as np


def permutation(same=False):
    # same = False -> the permutation must be diferent from the original
    i=0
    j=1
    k=2
    
    if not same:
        while i==0 and j==1 and k==2:
            i=random.choice([0,1,2])
            j=random.choice([0,1,2])
            while j==i:
                j=random.choice([0,1,2])
            k=random.choice([0,1,2])
            while k==i or k==j:
                k=random.choice([0,1,2])
    else:
        i=random.choice([0,1,2])
        j=random.choice([0,1,2])
        while j==i:
            j=random.choice([0,1,2])
        k=random.choice([0,1,2])
        while k==i or k==j:
            k=random.choice([0,1,2])
    
    return i,j,k
    
def change_color(img):
    pixels = img.load()
    width, height = img.size
    
    first = True
    ch=np.zeros(3)
    i=j=k=0
    for y in range(height):
        for x in range(width):
            r,g,b=pixels[x,y]
            if first:
                i,j,k=permutation(same=True)     # compute permutation of rgb
                first=False                     # The permutation will be the same for 
                                                # the whole image. The image could
                                                # remain unchanged due to same=True
            ch[i]=r
            ch[j]=g
            ch[k]=b
            
            pixels[x,y]=(int(ch[0]),int(ch[1]),int(ch[2]))
    return img

    
cartoon ='C:\\Users\\Marianna\\Desktop\\AIML_proj\\datasets\\cartoon\\initial_dataset'
dataset = 'C:\\Users\\Marianna\\Desktop\\dataset4'

dog_path = cartoon+'\dog'
elephant_path = cartoon+'\elephant'
giraffe_path = cartoon+'\giraffe'
guitar_path = cartoon+'\guitar'
horse_path = cartoon+'\horse'
house_path = cartoon+'\house'
person_path = cartoon+'\person'

paths = [dog_path, elephant_path, giraffe_path, guitar_path, 
         horse_path, house_path, person_path]

count1 = 0
count2 = 0
count3 = 0
count4 = 0

if not os.path.exists(dataset):
                os.mkdir(dataset)
        
for path1 in paths:
    
    path_len1 = len(os.listdir(path1))
    indx = int(path_len1/4)
    print(path_len1)
    
    count = 0

    for img_file in os.listdir(path1):
        count = count + 1

        im1 = Image.open(path1 + '/' + img_file)
                
        
        for path2 in paths:
            
            if path1 != path2:
                
                num2 = random.randint(1, path_len1)
                num3 = random.randint(1, path_len1)
                
                while (num2==num3) or (num2!=num3 and img_file.find(str(num2))!=-1 and img_file.find(str(num3))!=-1):
                    num2 = random.randint(1, path_len1)
                    num3 = random.randint(1, path_len1)
                    print("qui")

                # coloured_dataset_2.2
                # I change color here so there will be 
                # sets with the same images but probably with 
                # different colors
                
                im2 = Image.open(path1 + '/img_' + str(num2) + '.jpg')
                im3 = Image.open(path1 + '/img_' + str(num3) + '.jpg')
                im1 = change_color(im1)
                im2 = change_color(im2)
                im3 = change_color(im3)
                path_len2 = len(os.listdir(path2))
                num = random.randint(1, path_len2)
                odd = Image.open(path2 + '/img_' + str(num) + '.jpg')
                odd = change_color(odd)
    
                if count<=indx:
                    # odd = immagine 1
                    count1 = count1 + 1
                    label1_path = dataset+'\\1'
                    
                    if not os.path.exists(label1_path):
                        os.mkdir(label1_path)
                        
                    label1_path = label1_path+'\\'+str(count1) # folder name of this dataset entry
                    if not os.path.exists(label1_path):
                        os.mkdir(label1_path)
                        
                    odd.save(label1_path+'\\1.jpg')
                    im1.save(label1_path+'\\2.jpg')
                    im2.save(label1_path+'\\3.jpg')
                    im3.save(label1_path+'\\4.jpg')
                    # break        
                elif count>indx and count<=indx*2:
                    # odd = immagine 2
                    count2 = count2 + 1
                    label2_path = dataset+'\\2'
                    
                    if not os.path.exists(label2_path):
                        os.mkdir(label2_path)
                        
                    label2_path = label2_path+'\\'+str(count2)
                    if not os.path.exists(label2_path):
                        os.mkdir(label2_path)
                        
                    im1.save(label2_path+'\\1.jpg')
                    odd.save(label2_path+'\\2.jpg')
                    im2.save(label2_path+'\\3.jpg')
                    im3.save(label2_path+'\\4.jpg')
        
                elif count>indx*2 and count<=indx*3:
                    # odd = immagine 3
                    count3 = count3 + 1
                    label3_path = dataset+'\\3'
                    
                    if not os.path.exists(label3_path):
                        os.mkdir(label3_path)
                        
                    label3_path = label3_path +'\\'+str(count3)
                    if not os.path.exists(label3_path):
                        os.mkdir(label3_path)
                        
                    im1.save(label3_path+'\\1.jpg')
                    im2.save(label3_path+'\\2.jpg')
                    odd.save(label3_path+'\\3.jpg')
                    im3.save(label3_path+'\\4.jpg')
        
                else:
                    # odd = immagine 4
                    count4 = count4 + 1
                    label4_path = dataset+'\\4'
                    
                    if not os.path.exists(label4_path):
                        os.mkdir(label4_path)            
                    
                    label4_path = label4_path +'\\'+str(count4)
                    if not os.path.exists(label4_path):
                        os.mkdir(label4_path)
                        
                    im1.save(label4_path+'\\1.jpg')
                    im2.save(label4_path+'\\2.jpg')
                    im3.save(label4_path+'\\3.jpg')
                    odd.save(label4_path+'\\4.jpg')
