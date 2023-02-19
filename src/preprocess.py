import cv2
import numpy as np


def preprocess(image: np.ndarray) -> np.ndarray:
    # Upscale, interpolation with nearest neighbor
    image = cv2.resize(image, (0, 0), fx=3, fy=3, interpolation=cv2.INTER_NEAREST)

    # Denoise gray-like pixels
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 70, 70), (255, 255, 255))
    mask = cv2.bitwise_not(mask)
    image[np.where(mask)] = 255

    # Convert to binary
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)

    # Fix some holes
    kernel = np.ones((3, 3), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=2)

    # add padding
    image = cv2.copyMakeBorder(
        image, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=(255, 255, 255)
    )

    return image
