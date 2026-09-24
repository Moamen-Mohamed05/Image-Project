import numpy as np
import cv2


# =========================
# Basic Morphology
# =========================
def get_morphology(img, mode):
    """
    mode: 'dilation' | 'erosion' | 'opening'
    """

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Binary image
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    kernel = np.ones((7, 7), np.uint8)

    if mode == 'dilation':
        return cv2.dilate(binary, kernel)

    elif mode == 'erosion':
        return cv2.erode(binary, kernel)

    elif mode == 'opening':
        return cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

    else:
        raise ValueError("Invalid mode")


# =========================
# Boundary Extraction
# =========================
def get_boundary(img, mode):
    """
    mode: 'internal' | 'external' | 'gradient'
    """

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)

    if mode == 'internal':
        temp = cv2.erode(binary, kernel)
        return cv2.subtract(binary, temp)

    elif mode == 'external':
        temp = cv2.dilate(binary, kernel)
        return cv2.subtract(temp, binary)

    elif mode == 'gradient':
        return cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

    else:
        raise ValueError("Invalid mode")