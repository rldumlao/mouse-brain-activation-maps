import os
import requests

# Example c-Fos ISH image from Allen Mouse Brain Atlas
# Experiment ID: 79556694 (c-Fos sagittal ISH)
BASE_URL = https://api.brain-map.org/api/v2/image_download/

IMAGE_IDS = [
    127053634, 127053635, 127053636  # sample image IDs from experiment
]

OUTDIR = data/raw/brain_images
os.makedirs(OUTDIR, exist_ok=True)

for img_id in IMAGE_IDS:
    url = f{BASE_URL}{img_id}
    out_path = os.path.join(OUTDIR, fcfos_{img_id}.jpg)
    print(fDownloading: {url})
    response = requests.get(url)
    with open(out_path, wb) as f:
        f.write(response.content)

print(Downloaded all c-Fos images.)

