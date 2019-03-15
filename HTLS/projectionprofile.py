"""
TODO: Add documentation/citation
"""
import numpy as np


def get_projection_profile(binary_image):
    """
    Parameters
    ----------
    binary_image: numpy.ndarray
        The binary image to be projected.

    Returns
    -------
    projection_profile: numpy.ndarray
        A binary image representing the projection_profile.
    """
    chunk_percentage = 0.05
    chunk_width = int(chunk_percentage * binary_image.shape[1])
    projection_profile_width = int(1 / chunk_percentage * chunk_width)
    projection_profile = np.ones((binary_image.shape[0], projection_profile_width))

    start_col = 0
    while start_col < binary_image.shape[1]:
        end_col = min(start_col + chunk_width, binary_image.shape[1])

        for row in range(binary_image.shape[0]):
            horizontal_hist = np.sum(binary_image[row, start_col:end_col])
            hist_len = int(horizontal_hist / (end_col - start_col) * chunk_width)
            projection_profile[row, start_col:start_col+hist_len] = 0

        start_col = end_col

    return projection_profile
