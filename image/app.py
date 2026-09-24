import streamlit as st
import numpy as np
import cv2

# Import all modules
from Neighborhood import NeighborhoodProcessing
from edge import get_sobel
from histogram import HistogramProcessing
from segmentation import apply_basic_threshold, apply_automatic_threshold, apply_adaptive_threshold
from restoration import ImageRestoration
from morphology import get_morphology, get_boundary
import operation

st.set_page_config(page_title="Comprehensive Image Processing App", layout="wide")

# Sidebar for Navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("Select an image processing category:")
category = st.sidebar.selectbox("Category", [
    "Point & Color Operations",
    "Neighborhood Processing",
    "Histogram Processing",
    "Image Restoration",
    "Image Segmentation",
    "Morphology",
    "Edge Detection"
])

st.title(f"🖼️ {category}")
st.markdown("---")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Pre-process image for different modules
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    
    # === Performance Optimization ===
    # Neighborhood and Restoration have pure python loops. 
    # Resize them automatically to prevent Streamlit from hanging.
    if category in ["Neighborhood Processing", "Image Restoration"]:
        max_size = 300
        h, w = img_gray.shape
        if max(h, w) > max_size:
            scale = max_size / max(h, w)
            new_w, new_h = int(w * scale), int(h * scale)
            img_gray = cv2.resize(img_gray, (new_w, new_h))
            img_rgb = cv2.resize(img_rgb, (new_w, new_h))
            st.warning(f"⚠️ تم تصغير الصورة تلقائياً إلى {new_w}x{new_h} لتجنب تجميد التطبيق وتسريع الفلاتر اليدوية.")
            
    result = None

    # 1. Point & Color Operations
    if category == "Point & Color Operations":
        choice = st.selectbox("Choose Operation", [
            "Addition", "Subtraction", "Division", "Complement", 
            "Change Red Lighting", "Swap Red & Green", "Eliminate Red"
        ])
        if choice == "Addition":
            val = st.slider("Brightness Value", 0, 255, 50)
            result = operation.add_brightness(img_rgb, val)
        elif choice == "Subtraction":
            val = st.slider("Darkness Value", 0, 255, 50)
            result = operation.subtract_brightness(img_rgb, val)
        elif choice == "Division":
            val = st.slider("Division Value", 1, 10, 2)
            result = operation.divide_image(img_rgb, val)
        elif choice == "Complement":
            result = operation.complement_image(img_rgb)
        elif choice == "Change Red Lighting":
            val = st.slider("Boost Value", 0, 255, 100)
            result = operation.change_red_lighting(img_rgb, val)
        elif choice == "Swap Red & Green":
            result = operation.swap_red_green(img_rgb)
        elif choice == "Eliminate Red":
            result = operation.eliminate_red(img_rgb)

    # 2. Neighborhood Processing
    elif category == "Neighborhood Processing":
        choice = st.selectbox("Choose Filter", [
            "Average Filter", "Gaussian Filter", "Laplacian Filter", "Median Filter"
        ])
        processor = NeighborhoodProcessing(img_gray)
        if choice == "Average Filter":
            result = processor.average_filter()
        elif choice == "Gaussian Filter":
            result = processor.gaussian_filter()
        elif choice == "Laplacian Filter":
            result = processor.laplacian_filter()
        elif choice == "Median Filter":
            result = processor.median_filter()

    # 3. Histogram Processing
    elif category == "Histogram Processing":
        choice = st.selectbox("Choose Method", ["Stretch", "Equalize"])
        if choice == "Stretch":
            result = HistogramProcessing.stretch(img_gray)
        elif choice == "Equalize":
            result = HistogramProcessing.equalize(img_gray)

    # 4. Image Restoration
    elif category == "Image Restoration":
        choice = st.selectbox("Choose Method", ["Median Filter", "Outlier Method"])
        if choice == "Median Filter":
            result = ImageRestoration.median_filter_manual(img_gray)
        elif choice == "Outlier Method":
            thresh = st.slider("Threshold", 0, 100, 40)
            result = ImageRestoration.outlier_method_manual(img_gray, thresh)

    # 5. Image Segmentation
    elif category == "Image Segmentation":
        choice = st.selectbox("Choose Method", [
            "Basic Threshold", "Otsu Threshold", "Adaptive Threshold"
        ])
        if choice == "Basic Threshold":
            val = st.slider("Threshold Value", 0, 255, 127)
            result = apply_basic_threshold(img_rgb, val)
        elif choice == "Otsu Threshold":
            result = apply_automatic_threshold(img_rgb)
        elif choice == "Adaptive Threshold":
            result = apply_adaptive_threshold(img_rgb)

    # 6. Morphology
    elif category == "Morphology":
        sub_category = st.selectbox("Operation Type", ["Basic Morphology", "Boundary Extraction"])
        if sub_category == "Basic Morphology":
            mode = st.selectbox("Mode", ["dilation", "erosion", "opening"])
            result = get_morphology(img_rgb, mode)
        else:
            mode = st.selectbox("Mode", ["internal", "external", "gradient"])
            result = get_boundary(img_rgb, mode)

    # 7. Edge Detection
    elif category == "Edge Detection":
        result = get_sobel(img_rgb)


    # Display Results
    st.markdown("---")
    st.header("Results")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Image")
        st.image(img_rgb, use_container_width=True)
        
    with col2:
        st.subheader("Processed Image")
        if result is not None:
            # Streamlit handles 2D (grayscale) and 3D (RGB) numpy arrays automatically
            st.image(result, use_container_width=True)
