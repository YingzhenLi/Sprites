# Sprites Video Data Generation Scripts

This repo contains scripts to generate the "Sprites" data used in the following paper:

[Yingzhen Li](http://yingzhenli.net) and 
[Stephan Mandt](http://www.stephanmandt.com)

[Disentangled Sequential Autoencoder](https://arxiv.org/abs/1803.02991)

International Conference on Machine Learning (ICML), 2018

The sprite sheets are collected from the following open-source projects:

[Liberated Pixel Cup](http://lpc.opengameart.org)

[Universal-LPC-spritesheet](https://github.com/jrconway3/Universal-LPC-spritesheet)

We do NOT claim the ownership of the original sprite sheets. But if you will be using the
code in this repo to generate the sprite video data, then consider citing the two original
open-source projects, and our paper.

## Create the dataset
You need to install python packages [Pillow](https://pillow.readthedocs.io/) and [imageio](https://imageio.github.io) first. Using pip should be sufficient.

Then clone the repo to your working directory. Then first run

    python random_character.py
    
This will create frames/ folder and generate .png files of 1296 unique characters with different actions.

Then run

    python frame_to_npy.py
    
This will read the .png files in frames/, create path npy/, and generate numpy data files .npy.

After that if you don't want to retain the .png files, simply run

    rm -rf frames/
    
## Load the dataset
In your awesome python code, simply try

    from load_sprites import sprites_act
    X_train, X_test, A_train, A_test, D_train, D_test = sprites_act('npy/', return_labels=True)
    
Here X_train contains the video frames, represented as an numpy.array with shape (N_train, T, width, height, N_channel).
A_train contains the attribute labels of shape (N_train, T, 4, 6), and D_train contains action labels of shape (N_train, T, 9).

## Citing the paper (bib)

```
@inproceedings{li2018disentangle,
  title = {Disentangled Sequential Autoencoder},
  author = {Li, Yingzhen and Mandt, Stephan},
  booktitle = {International Conference on Machine Learning},
  year = {2018}
}
```


