# Description: Preprocesses sample images
import os
import cv2
import numpy as np
from PIL import Image
from src.shared import raw_dir, preprocess_dir
from src.preprocess import preprocess


def main():
    print(f"Preprocessing images in {raw_dir}")

    for filename in os.listdir(raw_dir):
        if not filename.endswith(".jpg"):
            continue

        raw_path = os.path.join(raw_dir, filename)
        image = np.array(Image.open(raw_path))

        image = preprocess(image)

        # Save to preprocessed
        preprocessed_path = os.path.join(preprocess_dir, filename)
        cv2.imwrite(preprocessed_path, image)

        print(f"Preprocessed {filename}")

    print("Done")


if __name__ == "__main__":
    main()
