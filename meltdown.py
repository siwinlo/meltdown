from PIL import Image
import PIL
import os
import glob


def main():
    # The number of pixels we would like to resize the small image to
    small_width = 3
    small_height = 4

    images_dir='/Users/siwinlo/PycharmProjects/meltdown/images/'
    images_small_dir='/Users/siwinlo/PycharmProjects/meltdown/images_small/'

    # We will scale up the small image by resize_factor so we don't have a very small image
    resize_factor = 500

    # We will meltdown all of the images in the directory "images"

    image_paths = glob.glob(images_dir+"/*")
    for image_path in image_paths:

        _, filename = os.path.split(image_path)
        file, _ = os.path.splitext(filename)

        print (image_path)
        im_orig = Image.open(image_path)
        im = im_orig.resize((small_width, small_height), PIL.Image.LANCZOS)

        im = im.resize((small_width * resize_factor, small_height * resize_factor))

        #We are saving to images_small_dir so no need to change filename
        im.save (images_small_dir + file + '.png')
if __name__ == "__main__":
    main()
