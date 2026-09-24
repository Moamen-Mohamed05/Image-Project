import numpy as np
import cv2


# =========================
# Sobel Edge Detection
# =========================
def get_sobel(img):
    """
    Input: RGB image
    Output: Edge image (grayscale)
    """

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Sobel X and Y
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Combine gradients
    edges = cv2.magnitude(sobel_x, sobel_y)

    return np.uint8(edges)