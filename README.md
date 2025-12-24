# Real-Time Traffic Monitoring System🚦 
### Using Deep Learning, Computer Vision & Django

---

## Project Overview
This project implements a Real-Time Traffic Monitoring System using Deep Learning and Computer Vision techniques, integrated with a Django-based web application.

The system analyzes live or recorded traffic video streams to detect vehicles
and monitor traffic conditions in real time. By leveraging the **YOLO (You Only
Look Once)** object detection model, the application provides fast and accurate
traffic surveillance suitable for intelligent transportation systems.

This project is developed as a **college academic project** with a focus on
practical implementation and real-world relevance.

---

## Objectives
- Detect vehicles from traffic video streams in real time  
- Apply deep learning techniques for traffic surveillance  
- Integrate ML models with a web-based system  
- Provide an easy-to-use interface for traffic analysis  

---

## Key Features
-  Real-time vehicle detection from traffic videos  
-  Video-based traffic surveillance  
-  Deep learning model (YOLOv7) for object detection  
-  Django web interface with user login & registration  
-  Traffic analysis and result visualization  
-  Fast and accurate detection using CNN-based models  

---

## Tech Stack

### 🔹 Programming & Frameworks
- Python 3.7+
- Django (Web Framework)

### 🔹 Deep Learning & Computer Vision
- YOLOv7
- TensorFlow / Keras
- OpenCV
- NumPy
- Scikit-learn

### 🔹 Frontend
- HTML
- CSS
- Django Templates

### 🔹 Database
- MySQL

---

## System Workflow
1. User accesses the web application  
2. Traffic video is uploaded  
3. Video frames are extracted  
4. YOLO model detects vehicles  
5. Results are displayed on the web interface  

---

## How to Run the Project

### Prerequisites
- Python 3.7 or above
- Django
- Required Python libraries

### 🔹 Run the Server
- python manage.py runserver


## Project Modules
- **User Module** – Handles user registration and login
- **Traffic Detection Module** – Processes traffic videos
- **YOLO Model Module** – Performs vehicle detection
- **Result Display Module** – Displays detection results

---

## Dataset & Model Note
> **Note:**  
> Pre-trained model weights (`.h5`, `.hdf5`, `.weights`) and large datasets are  
> **not included in this repository** due to GitHub file size limitations.

Models are loaded locally during execution, which follows **standard industry and academic best practices**.

---

## Results
- Accurate vehicle detection from traffic videos
- Efficient real-time processing
- Improved traffic monitoring performance

---

## Future Scope
- Live CCTV camera integration
- Traffic congestion prediction
- Accident detection and alerts
- Smart city traffic management

---

## Academic Note
This project is developed as part of an academic curriculum requirement and demonstrates the practical application of **Deep Learning and Computer Vision**  
in traffic surveillance systems.
