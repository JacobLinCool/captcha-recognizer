# Description: Collects sample images for the website
import os
import time
import urllib.request
from src.shared import raw_dir

count = 100


def main():
    print(f"Collecting {count} images to {raw_dir}")

    for i in range(count):
        url = "https://cos2s.ntnu.edu.tw/AasEnrollStudent/RandImage"
        filename = os.path.join(raw_dir, f"{i}.jpg")
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded {i+1}/{count} {filename}")
        time.sleep(0.1)

    print("Done")


if __name__ == "__main__":
    main()
