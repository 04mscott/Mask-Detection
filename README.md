<center><h1>Image Classification Neural Network</h1></center>
<center><h2>Mask Detection Using TensorFlow</h2></center>

<img src="assets/imgs/incorrect_mask.png" class="img-responsive" alt="">

Deployment ended to make way for (Air Quality App's)[] deployment

---

## Overview
This project leverages machine learning to develop an image classification system capable of detecting whether individuals are wearing masks. Using a Convolutional Neural Network (CNN) built with TensorFlow, the project achieved high performance and user accessibility through a custom-designed graphical interface.

## Key Features
+ High-Performance Model:
  - Constructed a CNN using TensorFlow's functional API to classify mask-wearing in images.
  - Achieved a 99.24% test accuracy with a loss of 0.0306, demonstrating excellent performance in real-world scenarios.
+ Dataset Preparation:
  - Collected and preprocessed images from a public dataset, creating balanced training, validation, and testing datasets.
  - Utilized custom file I/O functions to organize and prepare data pipelines efficiently.
+ Hyperparameter Tuning:
  - Experimented with various hyperparameters, including learning rates, activation functions, optimizers, and layer configurations, to optimize the model's performance.
+ Interactive User Interface:
  - Designed and implemented a Graphical User Interface (GUI) using TaiPy, enabling users to:
    - Upload an image directly through the interface.
    - Receive real-time predictions on whether the individual in the image is wearing a mask.

## Technologies Used
+ Machine Learning Framework: TensorFlow (Functional API)
+ Programming Language: Python
+ GUI Development: TaiPy
+ Data Handling: File I/O for dataset management
  
## How It Works
+ Upload an Image: Users upload an image of a person through the TaiPy-powered GUI.
+ Prediction in Real-Time: The model processes the image and outputs whether the person is wearing a mask or not, along with confidence scores.
+ Seamless Experience: Designed for non-technical users with an intuitive interface that simplifies model predictions.
