import logging
import os
from typing import Any, Callable, List, Tuple

import numpy as np
from PIL import Image

from exotic_dicoms.build.data import get_data_as_images


class BadResult:
    def __init__(self, image, gt_image):
        self.image = image
        self.gt_image = gt_image

    def visualize(self) -> Image.Image:
        # draw both side by side in cv2
        # and return an image
        image = np.hstack((self.gt_image, self.image))

        # convert to pillow
        return Image.fromarray(image)


# Get File Dir
FILE_DIR = os.path.dirname(os.path.abspath(__file__))

# Set Logging config
logging.basicConfig(level=logging.INFO)


def test_dicom_image_conversion(
    func: Callable[[Any], Image.Image],
    dicom_kwarg_name: str,
    func_kwargs: dict = None,
    prestep: Callable[[str], Any] = None,
) -> List[Tuple[str, List[BadResult]]]:
    """
    Test the image conversion function.

    :param func: function to test.
    :param dicom_kwarg_name: name of the keyword argument that contains the dicom file.
    :param func_kwargs: keyword arguments for the function.
    :param prestep: function to run before the function.

    :return: list of indices of bad images.
    """

    # get the images
    ground_truth_images = get_data_as_images()

    results = []

    # Load every dicom in the data folder
    for dicom_file in os.listdir(os.path.join(FILE_DIR, "../test-data")):
        if not dicom_file.endswith(".dcm"):
            continue

        logging.info(f"Testing {dicom_file}...")

        filepath = os.path.join(FILE_DIR, "../test-data", dicom_file)

        if prestep:
            dicom = prestep(filepath)
        else:
            dicom = filepath

        if func_kwargs is None:
            func_kwargs = {}

        func_kwargs[dicom_kwarg_name] = dicom

        # get the images from the function
        images = func(**func_kwargs)

        bad_images = []

        # check if the images are the same
        for i, (gt_image, image) in enumerate(
            zip(ground_truth_images, images)
        ):
            if not np.allclose(gt_image, image):
                bad_images.append(BadResult(image, gt_image))

        if not bad_images:
            bad_images = True
            logging.info(f"{dicom_file} passed.")

        else:
            logging.info(f"{dicom_file} failed.")
            results.append([dicom_file, bad_images])

    return results
