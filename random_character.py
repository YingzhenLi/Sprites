from PIL import Image
import sys, os
import numpy as np
import imageio
from scipy import ndimage

def gen_char(body, bottom, top, hair):

    np.random.seed(seed)

    # then randomly sample the components
    attributes = {'body': str(body), 'bottomwear': str(bottom),
                  'topwear': str(top), 'hair': str(hair)}
    img_list = []
    for attr in ['body', 'bottomwear', 'topwear', 'hair']:
        path = attr + '/'
        filename = attributes[attr] + '.png'
        #print path+filename
        img_list.append(Image.open(path + filename))
    # shoes
    img_list.append(Image.open('shoes/1.png'))

    # then merge all!
    f = Image.new('RGBA', img_list[0].size, 'black')
    for i in xrange(len(img_list)):
        f = Image.alpha_composite(f, img_list[i].convert('RGBA'))

    # save image
    classname = str(body)+str(bottom)+str(top)+str(hair)#+str(weapon)
    f.save('%s.png' % classname)

    img = Image.open('%s.png' % classname)
    # crop to 64 * 64
    width = 64; height = 64
    imgwidth, imgheight = img.size
    N_width = imgwidth / width
    N_height = imgheight / height
    path = 'frames/'
    if not os.path.exists(path):
        os.makedirs(path)

    N_total = 273   # 273 png files in total
    actions = {
    'spellcard': {'back': range(0, 7), 'left': range(13, 20),
                  'front': range(26, 33), 'right': range(39, 46)},
    'thrust': {'back': range(52, 60), 'left': range(65, 73),
               'front': range(78, 86), 'right': range(91, 99)},
    'walk': {'back': range(104, 113), 'left': range(117, 126),
             'front': range(130, 139), 'right': range(143, 152)},
    'slash': {'back': range(156, 162), 'left': range(169, 175),
              'front': range(182, 188), 'right': range(195, 201)},
    'shoot': {'back': range(208, 221), 'left': range(221, 234),
              'front': range(234, 247), 'right': range(247, 260)},
    'hurt': {'front': range(260, 266)}
    }
    duration = 0.1
    copy_path = 'frames/'

    # create save list
    for act in ['spellcard/', 'walk', 'slash']:
        if not os.path.exists(path+act+'/'):
            os.makedirs(path+act+'/')

    for j in xrange(N_height):
        for i in xrange(N_width):
            ind = j * N_width + i

            # for spellcard
            if ind >= 13 and ind < 46:
                box = (i*width, j*height, (i+1)*width, (j+1)*height)
                if ind >= 13 and ind < 20:
                    pose = 'left'
                    k = ind - 13
                    if k == 6:
                        k = k+1
                    a = img.crop(box)
                    a.convert('RGB')
                    a.save(path+'spellcard/' + pose + '_%s_%d.png' % (classname, k))
                    if k == 4:
                        a.save(path+'spellcard/' + pose + '_%s_%d.png' % (classname, 6))
                if ind >= 26 and ind < 33:
                    pose = 'front'
                    k = ind - 26
                    if k == 6:
                        k = k+1
                    a = img.crop(box)
                    a.convert('RGB')
                    a.save(path+'spellcard/' + pose + '_%s_%d.png' % (classname, k))
                    if k == 4:
                        a.save(path+'spellcard/' + pose + '_%s_%d.png' % (classname, 6))
                if ind >= 39 and ind < 46:
                    pose = 'right'
                    k = ind - 39
                    if k == 6:
                        k = k+1
                    a = img.crop(box)
                    a.convert('RGB')
                    a.save(path+'spellcard/' + pose + '_%s_%d.png' % (classname, k))
                    if k == 4:
                        a.save(path+'spellcard/' + pose + '_%s_%d.png' % (classname, 6))

            # for walk
            if ind >= 117 and ind < 152:
                box = (i*width, j*height, (i+1)*width, (j+1)*height)
                if ind >= 118 and ind < 126:
                    pose = 'left'
                    k = ind - 118
                    if k == 7:
                        k = 0
                    else:
                        k = k+1
                    a = img.crop(box)
                    a.convert('RGB')
                    a.save(path+'walk/' + pose + '_%s_%d.png' % (classname, k))
                if ind >= 131 and ind < 139:
                    pose = 'front'
                    k = ind - 131
                    if k == 7:
                        k = 0
                    else:
                        k = k+1
                    a = img.crop(box)
                    a.convert('RGB')
                    a.save(path+'walk/' + pose + '_%s_%d.png' % (classname, k))
                if ind >= 144 and ind < 152:
                    pose = 'right'
                    k = ind - 144
                    if k == 7:
                        k = 0
                    else:
                        k = k+1
                    a = img.crop(box)
                    a.convert('RGB')
                    a.save(path+'walk/' + pose + '_%s_%d.png' % (classname, k))

          # for slash
            if ind >= 169 and ind < 201:
                box = (i*width, j*height, (i+1)*width, (j+1)*height)
                if ind >= 169 and ind < 175:
                    pose = 'left'
                    k = ind - 169
                    a = img.crop(box)
                    a.convert('RGB')
                    a.save(path+'slash/' + pose + '_%s_%d.png' % (classname, k))
                    if k == 4:
                        a.save(path+'slash/' + pose + '_%s_%d.png' % (classname, 6))
                    if k == 0:
                        a.save(path+'slash/' + pose + '_%s_%d.png' % (classname, 7))
                if ind >= 182 and ind < 188:
                    pose = 'front'
                    k = ind - 182
                    a = img.crop(box)
                    a.convert('RGB')
                    a.save(path+'slash/' + pose + '_%s_%d.png' % (classname, k))
                    if k == 4:
                        a.save(path+'slash/' + pose + '_%s_%d.png' % (classname, 6))
                    if k == 0:
                        a.save(path+'slash/' + pose + '_%s_%d.png' % (classname, 7))
                if ind >= 195 and ind < 201:
                    pose = 'right'
                    k = ind - 195
                    a = img.crop(box)
                    a.convert('RGB')
                    a.save(path+'slash/' + pose + '_%s_%d.png' % (classname, k))
                    if k == 4:
                        a.save(path+'slash/' + pose + '_%s_%d.png' % (classname, 6))
                    if k == 0:
                        a.save(path+'slash/' + pose + '_%s_%d.png' % (classname, 7))

    # now remove the png files
    os.remove('%s.png' % classname)

if __name__ == '__main__':
    n_class = 6
    seed_list = seed_list = range(0, n_class**4)
    for seed in seed_list:
        body = int(seed / n_class**3)
        seed = int(np.mod(seed, n_class**3))
        bottom = int(seed / n_class**2)
        seed = int(np.mod(seed, n_class**2))
        top = int(seed / n_class)
        hair = int(np.mod(seed, n_class))

        gen_char(body, bottom, top, hair)
        if (seed+1) % 100 == 0:
            print 'generate %d/%d sequences' % (seed+1, n_class**4)

