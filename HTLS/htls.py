"""
TODO: Add documentation/citation
"""
import argparse

import matplotlib.pyplot as plt

import skimage
from skimage import filters
from skimage import io


def threshold(gray_image, mode='Otsu'):
    """
    Parameters
    ----------
    gray_image: numpy.ndarray
        The gray image to thresholded.
    mode: str
        Threshold mode, either 'Otsu' or 'Adaptive'.

    Returns
    -------
    binary_image: numpy.ndarray
        The new thresholded binary image.

    Raises
    -------
    ValueError:
        When given mode is neither 'Otsu' nor 'Adaptive'.
    """
    if mode == "Otsu":
        threshold = skimage.filters.threshold_otsu(gray_image)
        return gray_image <= threshold
    elif mode == 'Adaptive':
        """ TODO: check block_size """
        return skimage.filters.threshold_adaptive(gray_image, block_size=7)
    else:
        raise ValueError("Given threshold mode: " + mode + " is not supported.")

 
def segment_image(gray_image, thresh_mode='Otsu'):
    """
    Parameters
    ----------
    gray_image: numpy.ndarray
        The gray image to segmented.
    thresh_mode: str
        Threshold mode, either 'Otsu' or 'Adaptive'.

    Returns
    -------
    segmented_lines: TODO: check this

    Raises
    ------
    ValueError:
        When given mode is neither 'Otsu' nor 'Adaptive'.
    """
    binary_image = threshold(gray_image, thresh_mode)

    return binary_image


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i",   "--image",       help="path to input image", required=True)
    parser.add_argument("-thm", "--thresh_mode", help="'Otsu' or 'Adaptive'", default='Otsu')

    args = vars(parser.parse_args())
    
    input_image = skimage.io.imread(args["image"], as_gray=True)
    segmented_image = segment_image(input_image, args["thresh_mode"])

    plt.imshow(segmented_image, cmap=plt.cm.gray)
    plt.show()
