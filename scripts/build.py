import numpy as np
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from radstract.data.dicom import convert_images_to_dicom

from exotic_dicoms.build import get_data_as_images

print("Frames created and saved.")

images = get_data_as_images()
# convert to  numpy array
images = np.array(images)

clip = ImageSequenceClip(list(images), fps=24)
clip.write_videofile("scripts/cutting_sphere.mp4", codec="libx264")

# store video in DICOM
dcm = convert_images_to_dicom(images)
dcm.save_as("./scripts/basic_rgb.dcm")
