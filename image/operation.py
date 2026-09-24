import streamlit as st
import numpy as np
import cv2


# =========================
# Operations
# =========================
def add_brightness(img, value=50):
    return cv2.add(img, np.array([value]))

def subtract_brightness(img, value=50):
    return cv2.subtract(img, np.array([value]))

def divide_image(img, value=2):
    return (img / value).astype(np.uint8)

def complement_image(img):
    return 255 - img

def change_red_lighting(img, boost=100):
    b, g, r = cv2.split(img)
    r = cv2.add(r, boost)
    return cv2.merge((b, g, r))

def swap_red_green(img):
    swapped = img.copy()
    swapped[:, :, 1], swapped[:, :, 2] = img[:, :, 2], img[:, :, 1]
    return swapped

def eliminate_red(img):
    result = img.copy()
    result[:, :, 2] = 0
    return result


# =========================
# UI
# =========================
if __name__ == "__main__":
    st.set_page_config(page_title="Point Operations", layout="wide")

    st.title("🎨 Point & Color Image Operations")
    st.markdown("---")

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:

        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        choice = st.selectbox("Choose Operation", [
            "Addition",
            "Subtraction",
            "Division",
            "Complement",
            "Change Red Lighting",
            "Swap Red & Green",
            "Eliminate Red"
        ])

        # =========================
        # PROCESSING
        # =========================
        if choice == "Addition":
            result = add_brightness(img)

        elif choice == "Subtraction":
            result = subtract_brightness(img)

        elif choice == "Division":
            result = divide_image(img)

        elif choice == "Complement":
            result = complement_image(img)

        elif choice == "Change Red Lighting":
            result = change_red_lighting(img)

        elif choice == "Swap Red & Green":
            result = swap_red_green(img)

        elif choice == "Eliminate Red":
            result = eliminate_red(img)

        # =========================
        # DISPLAY
        # =========================
        st.markdown("---")
        st.header("Results")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(img, use_container_width=True)

        with col2:
            st.subheader("Processed Image")
            st.image(result, use_container_width=True)