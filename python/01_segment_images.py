import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

IMG_DIR = data/raw/brain_images
OUTDIR = data/processed
os.makedirs(OUTDIR, exist_ok=True)

for fname in os.listdir(IMG_DIR):
    if not fname.endswith(.jpg):
        continue
    img_path = os.path.join(IMG_DIR, fname)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    blur = cv2.GaussianBlur(img, (5, 5), 2)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    output_path = os.path.join(OUTDIR, fname.replace(.jpg, _mask.tif))
    cv2.imwrite(output_path, thresh)

    print(fProcessed: {fname})

    # Optional: Show
    # plt.imshow(thresh, cmap=gray)
    # plt.title(fname)
    # plt.show()

