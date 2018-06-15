import numpy as np
from scipy import ndimage
import os

num_direction = {'front': 0, 'left': 1, 'right':2, 'back': 3}
n_class = 6
n_frames = 8
n_directions = 3

def load_seq(path, labels, action, direction):
    num = ''
    for i in xrange(len(labels)):
        num = num + str(labels[i])

    # return sequence and label
    seq = []
    for frame in xrange(n_frames):
        fr = str(frame)
        filename = action + '/' + direction + '_' + num + '_' + fr + '.png'
        im = ndimage.imread(path + filename)
        seq.append(np.asarray(im, dtype='f'))

    attr_labels = np.zeros([len(labels), n_class])
    for i in xrange(len(labels)):
        attr_labels[i, labels[i]] = 1
    di_labels = np.zeros(n_directions)
    di_labels[num_direction[direction]] = 1
    list_attr = []
    list_di = []
    for i in xrange(n_frames):
        list_attr.append(attr_labels)
        list_di.append(di_labels)

    return np.asarray(seq), np.asarray(list_attr, dtype='f'), \
           np.asarray(list_di, dtype='f')

def save_npy():
    load_path = 'frames/'
    save_path = 'npy/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    actions = ['walk', 'spellcard', 'slash']
    directions = ['front', 'left', 'right']

    seed_list = range(0, n_class**4)
    np.random.seed(423)
    seed_list = np.random.permutation(seed_list)

    for action in actions:
        for direction in directions:
            im_npy_file_name = action + '_' + direction + '_frames'
            attr_npy_file_name = action + '_' + direction + '_attributes'
            di_npy_file_name = action + '_' + direction + '_directions'
            im_seq = []
            attr_seq = []
            di_seq = []
            for seed in seed_list:
                body = int(seed / n_class**3)
                seed = int(np.mod(seed, n_class**3))
                bottom = int(seed / n_class**2)
                seed = int(np.mod(seed, n_class**2))
                top = int(seed / n_class)
                hair = int(np.mod(seed, n_class))

                labels = [body, bottom, top, hair]

                seq, attr, di = load_seq(load_path, labels, action, direction)
                im_seq.append(seq)
                attr_seq.append(attr)
                di_seq.append(di)
            im_seq = np.asarray(im_seq, dtype='f')[:, :, :, :, :3] / 256.0
            attr_seq = np.asarray(attr_seq, dtype='f')
            di_seq = np.asarray(di_seq, dtype='f')

            # training and test data
            N_train = 1000
            im_seq_train = im_seq[:N_train]
            im_seq_test = im_seq[N_train:]
            np.save(save_path + im_npy_file_name + '_train.npy', im_seq_train)
            np.save(save_path + im_npy_file_name + '_test.npy', im_seq_test)
            print 'saved ' + save_path + im_npy_file_name + '_train.npy'
            print 'saved ' + save_path + im_npy_file_name + '_test.npy'

            attr_seq_train = attr_seq[:N_train]
            attr_seq_test = attr_seq[N_train:]
            np.save(save_path + attr_npy_file_name + '_train.npy', attr_seq_train)
            np.save(save_path + attr_npy_file_name + '_test.npy', attr_seq_test)
            print 'saved ' + save_path + attr_npy_file_name + '_train.npy'
            print 'saved ' + save_path + attr_npy_file_name + '_test.npy'

            di_seq_train = di_seq[:N_train]
            di_seq_test = di_seq[N_train:]
            np.save(save_path + di_npy_file_name + '_train.npy', di_seq_train)
            np.save(save_path + di_npy_file_name + '_train.npy', di_seq_test)
            print 'saved ' + save_path + di_npy_file_name + '_train.npy'
            print 'saved ' + save_path + di_npy_file_name + '_test.npy'

if __name__ == '__main__':
    save_npy()

