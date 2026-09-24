🖼️ Comprehensive Image Processing App

A comprehensive Image Processing Web Application built with Python, Streamlit, NumPy, and OpenCV.

The application provides an interactive interface for experimenting with different image processing techniques, including point operations, spatial filtering, histogram processing, image restoration, image segmentation, morphological operations, and edge detection.

✨ Features
🎨 Point & Color Operations

Perform different pixel-level and color operations on uploaded images:

Brightness Addition

Brightness Subtraction

Image Division

Image Complement

Red Channel Lighting

Red & Green Channel Swapping

Red Channel Elimination

🔲 Neighborhood Processing

Includes manually implemented spatial filtering techniques:

Average Filter

Gaussian Filter

Laplacian Filter

Median Filter

Manual Convolution

The filters are implemented using NumPy operations and explicit pixel-level processing.

📊 Histogram Processing

Improve image contrast using:

Histogram Stretching

Histogram Equalization

The histogram operations are implemented manually using NumPy.

🛠️ Image Restoration

Includes noise reduction and restoration techniques:

Manual Median Filter

Outlier Method

Configurable Outlier Threshold

These methods are implemented manually to demonstrate the underlying image processing concepts.

🧠 Image Segmentation

Three thresholding techniques are available:

Basic Thresholding

Otsu Automatic Thresholding

Adaptive Gaussian Thresholding

⚙️ Morphological Processing

Perform binary morphological operations:

Dilation

Erosion

Opening

📐 Boundary Extraction

Extract object boundaries using:

Internal Boundary

External Boundary

Morphological Gradient

🔎 Edge Detection

Detect image edges using:

Sobel X Gradient

Sobel Y Gradient

Combined Sobel Magnitude

🖥️ Interactive Web Interface

The application provides:

Image upload support

Category-based navigation

Interactive controls

Side-by-side original and processed image comparison

Adjustable processing parameters

Automatic image preprocessing

🛠️ Technologies

Python

Streamlit

NumPy

OpenCV

Pandas

Plotly

📁 Project Structure
Image-Processing-App/
│
├── app.py
├── operation.py
├── Neighborhood.py
├── edge.py
├── histogram.py
├── segmentation.py
├── restoration.py
├── morphology.py
└── README.md


Rename app.py in the structure if your main file has a different name.

🚀 Installation
1. Clone the Repository
git clone https://github.com/Moamen-Mohamed05/Image-Project
cd image-processing-app

2. Create a Virtual Environment
python -m venv venv


Activate the environment:

Windows:

venv\Scripts\activate


macOS / Linux:

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
streamlit run app.py


The application will open in your browser.

📦 Requirements

Create a requirements.txt file containing:

streamlit
numpy
opencv-python
pandas
plotly

🖼️ How to Use

Run the Streamlit application.

Upload an image in .jpg, .jpeg, or .png format.

Select an image processing category from the sidebar.

Choose the desired processing technique.

Adjust parameters when available.

Compare the original image with the processed result.

⚡ Performance Optimization

Some processing techniques, especially the manually implemented neighborhood filters and restoration algorithms, use Python loops and can be computationally expensive for large images.

To improve performance, the application automatically resizes large images when using:

Neighborhood Processing

Image Restoration

The maximum processing dimension is limited to 300 pixels for these operations.

This helps prevent the Streamlit application from becoming unresponsive while demonstrating manual image processing algorithms.

📚 Processing Techniques Overview
Category	Techniques
Point & Color Operations	Addition, Subtraction, Division, Complement, RGB Operations
Neighborhood Processing	Average, Gaussian, Laplacian, Median
Histogram Processing	Stretching, Equalization
Image Restoration	Median Filter, Outlier Method
Image Segmentation	Basic, Otsu, Adaptive Threshold
Morphology	Dilation, Erosion, Opening
Boundary Extraction	Internal, External, Gradient
Edge Detection	Sobel
🎯 Project Purpose

This project was developed as a practical implementation of fundamental Digital Image Processing concepts.

Instead of relying entirely on built-in image processing functions, several algorithms are implemented manually using Python and NumPy to demonstrate how these techniques work at the pixel and neighborhood level.

The project can be useful for:

Learning Digital Image Processing

Understanding image filtering

Experimenting with segmentation techniques

Studying histogram operations

Understanding morphological operations

Practicing OpenCV and NumPy

Demonstrating image processing concepts through an interactive UI

🔮 Future Improvements

Possible improvements include:

📥 Download processed images

🌓 Light/Dark theme switch

🎚️ More adjustable filter parameters

📊 Display image histograms before and after processing

🔄 Undo/Reset processing

🧩 Additional edge detection algorithms

🧠 More segmentation techniques

🖌️ Additional morphological operations

📈 Image quality metrics such as MSE and PSNR

⚡ Performance optimization for large images

🖼️ Batch image processing

⚠️ Notes

Some algorithms in this project are intentionally implemented manually for educational purposes. Built-in OpenCV alternatives may provide better performance for production applications.

The application is primarily intended for educational purposes and experimentation with digital image processing techniques.

📄 License

This project is available for educational and personal use.

You may add a license such as the MIT License if you want to make the project openly reusable.

⭐ If you found this project useful, consider giving it a star!
