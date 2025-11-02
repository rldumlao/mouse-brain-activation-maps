// ImageJ Macro: preprocess.ijm
// Purpose: Preprocess mouse brain slices (grayscale) for segmentation
// Steps: Convert to grayscale, enhance contrast, smooth, and threshold

// Open an image (user provides path)
open("/path/to/your/brain_slice.tif");

// Convert to 8-bit grayscale
run("8-bit");

// Enhance contrast with normalization
run("Enhance Contrast...", "saturated=0.35 normalize");

// Apply Gaussian Blur to reduce noise
run("Gaussian Blur...", "sigma=2");

// Apply automatic thresholding (Otsu or Triangle works well for IEGs)
setAutoThreshold("Otsu dark");
run("Convert to Mask");

// Optional: Fill small holes
run("Fill Holes");

// Analyze Particles to extract ROIs (optional)
run("Set Measurements...", "area mean min centroid");
run("Analyze Particles...", "size=100-Infinity show=Outlines display include");

// Save the binary mask
saveAs("Tiff", "/path/to/output/processed_mask.tif");

// Done
print("Preprocessing complete.");
