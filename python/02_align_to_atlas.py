import os
import SimpleITK as sitk

IMG_DIR = data/processed
ATLAS_IMG = data/raw/atlas/allen_reference_slice.tif  # Must exist!
OUTPUT_DIR = data/processed/aligned
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load reference atlas slice
atlas = sitk.ReadImage(ATLAS_IMG, sitk.sitkFloat32)

# Loop through segmented images
for fname in os.listdir(IMG_DIR):
    if not fname.endswith(_mask.tif):
        continue

    img_path = os.path.join(IMG_DIR, fname)
    moving = sitk.ReadImage(img_path, sitk.sitkFloat32)

    # Set up the registration method (rigid)
    registration = sitk.ImageRegistrationMethod()
    registration.SetMetricAsMattesMutualInformation(numberOfHistogramBins=50)
    registration.SetInterpolator(sitk.sitkLinear)
    registration.SetOptimizerAsRegularStepGradientDescent(
        learningRate=2.0,
        minStep=1e-4,
        numberOfIterations=200
    )
    registration.SetTransform(sitk.TranslationTransform(atlas.GetDimension()))
    registration.SetInitialTransform(sitk.TranslationTransform(atlas.GetDimension()))

    # Perform registration
    final_transform = registration.Execute(atlas, moving)

    # Resample moving image
    resampled = sitk.Resample(moving, atlas, final_transform, sitk.sitkNearestNeighbor, 0.0, moving.GetPixelID())

    # Save result
    out_path = os.path.join(OUTPUT_DIR, fname.replace(_mask.tif, _aligned.tif))
    sitk.WriteImage(resampled, out_path)
    print(fAligned and saved: {out_path})

