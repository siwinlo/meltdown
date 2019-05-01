from PIL import Image
import PIL
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

def main():

    sherrielevine = resize_candidate("sherrielevine/SLKirchner.png")
    #sherrielevine = resize_candidate("sherrielevine/SLMondrian.png")


    #images_dir='mondrian'
    images_dir='kirchner'
    image_paths = glob.glob(images_dir+"/*")

    #images_small_dir='mondrian_small'
    images_small_dir='kirchner_small'

    distances=[]

    for image_path in image_paths:
        candidate = resize_candidate(image_path)
        _, filename = os.path.split(image_path)
        file, _ = os.path.splitext(filename)

        # candidate.save (images_small_dir + file + '.png')
        Image.fromarray(candidate.astype(np.uint8)).save (images_small_dir+'/'+file+'.png')

        distances.append([calcdistance(candidate, sherrielevine), image_path])

    for d in distances:
        print(d)
    print('-----------------')
    for d in sorted(distances):
        print(d)

def resize_candidate(filename, height=4, width=3):
    im_orig = Image.open(filename)
    im = im_orig.resize((width, height), PIL.Image.LANCZOS)
    return np.array(im).astype(np.int32)

def calcdistance(image1, image2):
    return np.sqrt( np.sum(np.square(image1-image2)))

if __name__ == "__main__":
    main()



'''

    # The number of pixels we would like to resize the small image to
    small_width = 3
    small_height = 4

    images_dir='/Users/siwinlo/PycharmProjects/meltdown/images/'
    images_small_dir='/Users/siwinlo/PycharmProjects/meltdown/images_small/'

    # We will meltdown all the images in the directory "images"

    image_paths = glob.glob(images_dir+"/*")
    for image_path in image_paths:

        _, filename = os.path.split(image_path)
        file, _ = os.path.splitext(filename)

        print (image_path)
        im_orig = Image.open(image_path)
        im = im_orig.resize((small_width, small_height), PIL.Image.LANCZOS)

        #We are saving to images_small_dir so no need to change filename
        im.save (images_small_dir + file + '.png')

    # We will convert the images to rgb values

'''
