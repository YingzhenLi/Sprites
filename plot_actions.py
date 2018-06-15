from PIL import Image
import sys, os
import numpy as np
import imageio
from scipy import ndimage

def cut_image(i, j):

    img = Image.open('0.png')
    # crop to 64 * 64
    width = 64; height = 64 
    imgwidth, imgheight = img.size 
    N_width = imgwidth / width
    N_height = imgheight / height
    print i, j, j * N_width + i
    box = (i*width, j*height, (i+1)*width, (j+1)*height)
    a = img.crop(box)
    a.convert('RGB')
    
    return a
    
if __name__ == '__main__':
    n_class = 6

    img_list = []
    for attr in ['body', 'bottomwear', 'topwear', 'hair']:#, 'weapon']:
        path = attr + '/'
        filename = '0.png'
        #print path+filename
        img_list.append(Image.open(path + filename))
    # shoes
    img_list.append(Image.open('shoes/1.png'))
    
    # then merge all!
    f = Image.new('RGBA', img_list[0].size, 'black')
    for i in xrange(len(img_list)):
        f = Image.alpha_composite(f, img_list[i].convert('RGBA'))    
    # save image
    f.save('0.png')
    
    i = 4
    j_list = [9, 10, 11, 1, 2, 3, 13, 14, 15]
    images = []
    for j in j_list:
        images.append(cut_image(i, j))
        
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    new_im.save('actions.png')
    
    os.remove('0.png')
    
