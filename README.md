# Exotic DICOMs (Work in Progress!)

**Note that this repository is a work in progress. We are actively looking for interesting DICOMs to add to this repository. If you have any interesting DICOMs that you would like to share, please open a pull request with the DICOMs and a README.md file that describes the DICOMs.**

Exotic DICOMs provides a simple way to test DICOM conversion functions in python, and beyond. It contains a wide range of DICOMs to check if your DICOM conversion functions can handle a wide-range of edge-cases

## Quickstart

```bash
pip install git+https://github.com/radoss-org/exotic-dicoms.git
```

This is a quickstart on testing dicoms with RadStract (https://github.com/radoss-org/radstract)

```python
import pydicom
from radstract.data.dicom import convert_dicom_to_images

from exotic_dicoms.test import test_dicom_image_conversion


def pre_step(dcm):
    return pydicom.dcmread(dcm)

# This will run the convert_dicom_to_images function for each DICOM in the test data.
# and check if the output is correct.
results = test_dicom_image_conversion(
    func=convert_dicom_to_images,
    dicom_kwarg_name="old_dicom",
    prestep=pre_step,
)
```

Since radstract only accepts pydicom objects as input, we use a prestep function to convert the path that exotic_dicoms provides to a pydicom object.

## Viewing bad DICOMs

If you get bad results, here is how you can inspect the bad DICOMs:

```python
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
```

![](https://files.mcaq.me/4a8h3.png)

## Manual Checking

You can download the test cases directly from the following link:

https://github.com/radoss-org/exotic-dicoms/tree/main/exotic_dicoms/test-data

You should see this exact data from each DICOM: https://files.mcaq.me/8086j.mp4

![](https://files.mcaq.me/8086j.mp4)

## License

This project is licensed under Apache 2.0. See the [LICENSE](LICENSE) file for more details.

## Call for Contributions

We are actively looking for interesting DICOMs to add to this repository. If you have any interesting DICOMs that you would like to share, please open a pull request with the DICOMs and a README.md file that describes the DICOMs.