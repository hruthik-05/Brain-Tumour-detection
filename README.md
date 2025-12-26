# Brain Tumor Detection using Deep Learning

This project implements an end-to-end deep learning system for brain tumor classification using MRI images.  
The model was trained in Google Colab, saved, and downloaded for integration with a web-based user interface built using HTML, CSS, and JavaScript.

---

## Project Overview

Brain tumor detection from MRI scans is a challenging and time-consuming task that requires expert analysis.  
This project aims to assist in automated classification of brain tumors using deep learning techniques and demonstrates how a trained model can be exported from a notebook environment and used in a real-world application.

---

## Tumor Classes

The model classifies MRI images into the following categories:

- Glioma  
- Meningioma  
- Pituitary Tumor  
- No Tumor  

---

## Technologies Used

### Machine Learning
- Python  
- TensorFlow / Keras  
- NumPy, Pandas  
- Matplotlib  
- Google Colab  

### Web Technologies
- HTML  
- CSS  
- JavaScript  

---

## Model Training and Export

- The deep learning model was trained using Google Colab with GPU acceleration.
- MRI images were resized and normalized before training.
- Dropout and batch normalization were applied to reduce overfitting.
- After training, the model was **saved and downloaded** for later use in the web application.

---

## Web Interface Integration

The downloaded trained model is integrated with a simple web interface to demonstrate practical usability:

- Users can upload an MRI image
- The image is processed and passed to the trained model
- The model returns the predicted tumor class
- The UI is designed to be minimal and easy to use

---

## Results

The model achieved promising accuracy in classifying different types of brain tumors.  
This project focuses on demonstrating the complete workflow from model training to deployment-ready integration.

---

## Future Improvements

- Deploy the model using Flask or FastAPI
- Host the application on a cloud platform (AWS / GCP)
- Improve accuracy with larger datasets
- Add confidence scores to predictions
- Enhance the web interface

---

## Disclaimer

This project is intended for educational purposes only and should not be used for medical diagnosis.

---

## Author

Hruthik
