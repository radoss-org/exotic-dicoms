import pydicom
from radstract.data.dicom import convert_dicom_to_images

from exotic_dicoms.test import test_dicom_image_conversion


def pre_step(dcm):
    return pydicom.dcmread(dcm)


results = test_dicom_image_conversion(
    func=convert_dicom_to_images,
    dicom_kwarg_name="old_dicom",
    prestep=pre_step,
)

for filename, bad_results in results:
    for i, bad_result in enumerate(bad_results):
        img = bad_result.visualize()
        img.save(f"bad_{filename}_{i}.png")
