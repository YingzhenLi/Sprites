"""
Visualising animations
"""

import numpy as np

def reshape_and_tile_images(array, shape=(28, 28), n_cols=None):
    if n_cols is None:
        n_cols = int(math.sqrt(array.shape[0]))
    n_rows = int(np.ceil(float(array.shape[0])/n_cols))
    if len(shape) == 2:
        order = 'C'
    else:
        order = 'F'

    def cell(i, j):
        ind = i*n_cols+j
        if i*n_cols+j < array.shape[0]:
            return array[ind].reshape(*shape, order='C')
        else:
            return np.zeros(shape)

    def row(i):
        return np.concatenate([cell(i, j) for j in range(n_cols)], axis=1)

    return np.concatenate([row(i) for i in range(n_rows)], axis=0)

def plot_gif(x_seq, shape, path, filename):
    n_cols = int(np.sqrt(x_seq.shape[0])) 
    x_seq = x_seq[:n_cols**2]
    T = x_seq.shape[1]
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    
    fig = plt.figure()
    x0 = reshape_and_tile_images(x_seq[:, 0], shape, n_cols)
    im = plt.imshow(x0, animated=True, cmap='gray')
    plt.axis('off')
    
    def update(t):
        x_frame = reshape_and_tile_images(x_seq[:, t], shape, n_cols)
        im.set_array(x_frame)
        return im,
        
    anim = FuncAnimation(fig, update, frames=np.arange(T), \
                          interval=1000, blit=True)
    anim.save(path+filename+'.gif', writer='imagemagick')
    print 'image saved as ' + path+filename+'.gif'

