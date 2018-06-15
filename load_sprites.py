import os, time
import numpy as np

def sprites_act(path, seed=0, return_labels = False):
    directions = ['front', 'left', 'right']
    actions = ['walk', 'spellcard', 'slash']
    start = time.time()
    path = path + 'npy/'
    X_train = []
    X_test = []
    if return_labels:
        A_train = []; A_test = []
        D_train = []; D_test = []
    for act in xrange(len(actions)):
        for i in xrange(len(directions)):
            label = 3 * act + i
            print actions[act], directions[i], act, i, label
            x = np.load(path + '%s_%s_frames_train.npy' % (actions[act], directions[i]))
            X_train.append(x)
            y = np.load(path + '%s_%s_frames_test.npy' % (actions[act], directions[i]))
            X_test.append(y)
            if return_labels:
                a = np.load(path + '%s_%s_attributes_train.npy' % (actions[act], directions[i]))
                A_train.append(a)
                d = np.zeros([a.shape[0], a.shape[1], 9])
                d[:, :, label] = 1; D_train.append(d)

                a = np.load(path + '%s_%s_attributes_test.npy' % (actions[act], directions[i]))
                A_test.append(a)
                d = np.zeros([a.shape[0], a.shape[1], 9])
                d[:, :, label] = 1; D_test.append(d)

    X_train = np.concatenate(X_train, axis=0)
    X_test = np.concatenate(X_test, axis=0)
    np.random.seed(seed)
    ind = np.random.permutation(X_train.shape[0])
    X_train = X_train[ind]
    if return_labels:
        A_train = np.concatenate(A_train, axis=0)
        D_train = np.concatenate(D_train, axis=0)
        A_train = A_train[ind]
        D_train = D_train[ind]
    ind = np.random.permutation(X_test.shape[0])
    X_test = X_test[ind]
    if return_labels:
        A_test = np.concatenate(A_test, axis=0)
        D_test = np.concatenate(D_test, axis=0)
        A_test = A_test[ind]
        D_test = D_test[ind]
        print A_test.shape, D_test.shape, X_test.shape, 'shapes'
    print X_train.shape, X_test.min(), X_test.max()
    end = time.time()
    print 'data loaded in %.2f seconds...' % (end - start)

    if return_labels:
        return X_train, X_test, A_train, A_test, D_train, D_test
    else:
        return X_train, X_test

