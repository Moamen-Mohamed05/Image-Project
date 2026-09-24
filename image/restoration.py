import streamlit as st
import numpy as np
import cv2


class ImageRestoration:

    @staticmethod
    def median_filter_manual(noisy_img):
        row, col = noisy_img.shape
        output = np.zeros_like(noisy_img)

        padded = np.pad(noisy_img, (1, 1), mode='edge')

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                window = padded[i-1:i+2, j-1:j+2].flatten()
                window.sort()
                output[i-1, j-1] = window[4]

        return output.astype(np.uint8)

    @staticmethod
    def outlier_method_manual(noisy_img, threshold=40):
        row, col = noisy_img.shape
        output = np.copy(noisy_img)
        img_int = noisy_img.astype(np.int32)

        for i in range(1, row - 1):
            for j in range(1, col - 1):

                sum_neighbors = (
                    img_int[i-1, j-1] + img_int[i-1, j] + img_int[i-1, j+1] +
                    img_int[i, j-1]                     + img_int[i, j+1] +
                    img_int[i+1, j-1] + img_int[i+1, j] + img_int[i+1, j+1]
                )

                m = sum_neighbors / 8.0
                p = noisy_img[i, j]

                if abs(p - m) > threshold:
                    output[i, j] = int(m)
                else:
                    output[i, j] = p

        return output.astype(np.uint8)


# =========================
# UI
# =========================
if __name__ == "__main__":
    st.set_page_config(page_title="Image Restoration App", layout="wide")

    st.title("🖼️ Image Restoration App")
    st.markdown("---")

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:

        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

        # ✔ FIX: keep original image (RGB)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        choice = st.selectbox("Choose Method", [
            "Median Filter",
            "Outlier Method"
        ])

        processor = ImageRestoration()

        if choice == "Median Filter":
            result = processor.median_filter_manual(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))
        else:
            result = processor.outlier_method_manual(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY))

        st.markdown("---")
        st.header("Results")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(img, use_container_width=True)

        with col2:
            st.subheader("Processed Image")
            st.image(result, use_container_width=True)