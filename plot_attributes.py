from PIL import Image
import sys, os
import numpy as np
import imageio
from scipy import ndimage

def cut_image(attribute, i):

    path = attribute + '/'
    filename = str(i) + '.png'
    img = Image.open(path + filename)
    
    # then merge all!
    f = Image.new('RGBA', img.size, 'black')
    f = Image.alpha_composite(f, img.convert('RGBA'))
    
    classname = attribute + '_%d' % i
    f.save('%s.png' % classname)
    
    img = Image.open('%s.png' % classname)
    # crop to 64 * 64
    width = 64; height = 64 
    imgwidth, imgheight = img.size 
    N_width = imgwidth / width
    N_height = imgheight / height
    i = 0; j = 14
    box = (i*width, j*height, (i+1)*width, (j+1)*height)
    a = img.crop(box)
    a.convert('RGB')
    if attribute == 'body':
        color = a.getpixel((32, 32))
        print color
        a = Image.new('RGBA', a.size, color)
    
    os.remove('%s.png' % classname)
    return a
    
if __name__ == '__main__':
    n_class = 6
    attributes = ['body', 'bottomwear', 'topwear', 'hair']
    for attr in attributes:
        images = []
        for i in xrange(n_class):
            images.append(cut_image(attr, i))
        
        widths, heights = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset,0))
            x_offset += im.size[0]

        new_im.save(attr + '.png')
    
