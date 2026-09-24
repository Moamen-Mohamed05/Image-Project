import numpy as np
import cv2


class NeighborhoodProcessing:

    def __init__(self, image):
        self.original_image = image  # لازم تكون grayscale

    # =========================
    # Convolution
    # =========================
    def apply_convolution(self, kernel):
        img_h, img_w = self.original_image.shape
        kh, kw = kernel.shape

        padded = np.pad(
            self.original_image,
            ((kh // 2, kh // 2), (kw // 2, kw // 2)),
            mode='edge'
        )

        output = np.zeros((img_h, img_w), dtype=np.float32)

        for i in range(img_h):
            for j in range(img_w):
                region = padded[i:i + kh, j:j + kw]
                output[i, j] = np.sum(region * kernel)

        return output

    # =========================
    # Filters
    # =========================
    def average_filter(self):
        kernel = np.ones((3, 3)) / 9
        result = self.apply_convolution(kernel)
        return np.uint8(np.clip(result, 0, 255))

    def gaussian_filter(self):
        kernel = (1/16) * np.array([[1,2,1],
                                    [2,4,2],
                                    [1,2,1]])
        result = self.apply_convolution(kernel)
        return np.uint8(np.clip(result, 0, 255))

    def laplacian_filter(self):
        kernel = np.array([[0,1,0],
                           [1,-4,1],
                           [0,1,0]])
        result = self.apply_convolution(kernel)
        return np.uint8(np.clip(np.abs(result), 0, 255))

    def median_filter(self):
        img_h, img_w = self.original_image.shape
        padded = np.pad(self.original_image, ((1,1),(1,1)), mode='edge')

        output = np.zeros((img_h, img_w), dtype=np.uint8)

        for i in range(img_h):
            for j in range(img_w):
                window = padded[i:i+3, j:j+3].flatten()
                output[i,j] = np.median(window)

        return output