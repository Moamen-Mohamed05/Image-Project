import numpy as np
import cv2


class HistogramProcessing:

    # =========================
    # Histogram Stretching
    # =========================
    @staticmethod
    def stretch(image):

        # Convert to grayscale if needed
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        low = np.min(image)
        high = np.max(image)

        if high == low:
            return image

        stretched = ((image - low) / (high - low)) * 255
        return stretched.astype(np.uint8)

    # =========================
    # Histogram Equalization
    # =========================
    @staticmethod
    def equalize(image):

        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        hist, _ = np.histogram(image.ravel(), 256, [0, 256])

        pdf = hist / image.size
        cdf = pdf.cumsum()

        sk = np.round(cdf * 255).astype(np.uint8)

        return sk[image]