
\# 🧍 AI-Based Smart Posture Monitoring and Correction System



\## 📌 Project Overview



This project presents an \*\*AI-based smart posture monitoring and correction system\*\* that detects human posture in real time and provides corrective suggestions. The system uses computer vision and machine learning techniques to identify posture patterns and reduce posture-related health issues.



The system is designed with \*\*dual monitoring capability\*\*:



\- \*\*Webcam-based posture monitoring (Software Implementation – Completed)\*\*

\- \*\*Wearable sensor-based posture monitoring (Hardware Integration – Upcoming)\*\*



The main goal is to prevent long-term posture problems such as back pain, neck strain, and spinal disorders by continuously monitoring posture and providing corrective feedback.



---



\## 🎯 Problem Statement



Improper posture during prolonged sitting and device usage has become a major health concern among students and professionals. Continuous slouching and poor head alignment can lead to severe musculoskeletal problems.



Existing posture monitoring systems are either expensive, intrusive, or rely on a single sensing technique. There is a need for an intelligent, affordable, and adaptive posture monitoring system capable of real-time correction.



---



\## 🎯 Objectives



\- Detect human posture using artificial intelligence

\- Classify posture into Good, Mild Slouch, and Severe Slouch

\- Provide real-time corrective suggestions

\- Develop a wearable posture monitoring system

\- Reduce posture-related health issues through continuous monitoring



---



\## 🚀 Current Implementation (Software Phase — Completed)



\### ✅ Webcam-Based Posture Monitoring

\- Face detection using OpenCV Haar Cascade

\- Head position tracking

\- Slouch detection using vertical displacement

\- Head tilt detection (left/right)

\- Real-time posture suggestions

\- Noise smoothing for stable predictions

\- Automatic baseline posture calibration



\### ✅ Machine Learning Pipeline for Wearable Mode

\- WISDM dataset preprocessing

\- Data cleaning and normalization

\- Sensor data windowing

\- Feature extraction from accelerometer data

\- Random Forest classifier training

\- Posture classification

\- Real-time prediction simulation



---



\## 🧠 Technologies Used



\### Programming Language

\- Python



\### Libraries Used



\#### OpenCV

\- Face detection

\- Computer vision processing

\- Real-time webcam input



\#### NumPy

\- Numerical computations

\- Feature calculations

\- Array processing



\#### Pandas

\- Dataset loading and preprocessing

\- Data cleaning



\#### Scikit-learn

\- Machine learning model training

\- Random Forest classification

\- Model evaluation



\#### Joblib

\- Model saving and loading



---



\## 📊 Dataset Used



\### WISDM Dataset (Wireless Sensor Data Mining)



The WISDM dataset contains real accelerometer data collected from smartphones and is widely used in wearable computing research.



\### Why WISDM was selected:

\- Real 3-axis accelerometer data (x, y, z)

\- Large labeled dataset

\- Standard benchmark dataset

\- Matches MPU6050 sensor structure

\- Suitable for human activity recognition



\### Activity to Posture Mapping

\- Standing / Walking → Good posture

\- Sitting / Upstairs → Mild slouch

\- Jogging / Downstairs → Severe slouch



---



\## ⚙ Machine Learning Pipeline



\### Data Processing Steps

1\. Data cleaning and preprocessing

2\. Windowing (40 samples, overlap 20)

3\. Feature extraction

4\. Model training

5\. Posture classification

6\. Real-time prediction logic



\### Extracted Features

\- Mean acceleration

\- Standard deviation

\- Root Mean Square (RMS)

\- Resultant acceleration

\- Pitch angle

\- Roll angle



\### Model Used

\- Random Forest Classifier



\### Model Performance

\- Accuracy: ~92–93%



---



\## 🏗 System Architecture



\### Webcam Mode


=======
>>>>>>> ab3a6bc422ff073fc98d1c2fbf320ccd669e6c4d

