import streamlit as st
import numpy as np
import cv2

# =========================
# Thresholding Functions
# =========================
def apply_basic_threshold(image, threshold_value):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, result = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return result


def apply_automatic_threshold(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, result = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return result


def apply_adaptive_threshold(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    result = cv2.adaptiveThreshold(
        image,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )
    return result


# =========================
# STREAMLIT UI (مهم يكون فوق)
# =========================
if __name__ == "__main__":
    st.set_page_config(page_title="Segmentation", layout="wide")

    st.title("🧠 Image Segmentation")
    st.markdown("---")

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])


    # =========================
    # MAIN LOGIC
    # =========================
    if uploaded_file is not None:

        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        choice = st.selectbox("Choose Method", [
            "Basic Threshold",
            "Otsu Threshold",
            "Adaptive Threshold"
        ])

        if choice == "Basic Threshold":
            val = st.slider("Threshold Value", 0, 255, 127)
            result = apply_basic_threshold(img, val)

        elif choice == "Otsu Threshold":
            result = apply_automatic_threshold(img)

        elif choice == "Adaptive Threshold":
            result = apply_adaptive_threshold(img)

        # =========================
        # DISPLAY
        # =========================
        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original")
            st.image(img, use_container_width=True)

        with col2:
            st.subheader("Result")
            st.image(result, use_container_width=True)
 