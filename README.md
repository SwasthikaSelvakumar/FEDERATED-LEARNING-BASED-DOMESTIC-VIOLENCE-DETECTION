## SafeSpeak: AI-Powered Domestic Violence Detection System

## Overview

**SafeSpeak** is an AI-driven web application designed to identify potential signs of domestic violence or emotional distress from audio recordings. The system analyzes the uploaded or recorded audio to estimate the level of distress and provides access to relevant emergency helpline numbers. The project emphasizes **privacy**, **local inference**, and includes a demonstration of **federated learning** concepts.

---

## Core Concept

SafeSpeak processes speech audio to evaluate the emotional tone and intensity using machine learning. Audio features are extracted and passed into a trained **artificial neural network (ANN)** model, which classifies the severity level as **Normal**, **Concerning**, or **Critical**. No user data is stored or transmitted externally, ensuring complete privacy.

---

## Tech Stack

| Layer                       | Technology                     | Purpose                                                                 |
| --------------------------- | ------------------------------ | ----------------------------------------------------------------------- |
| **Frontend**                | HTML, CSS, JavaScript          | Handles user interaction, file upload, and UI visualization             |
| **Backend**                 | Flask (Python)                 | Processes API requests, runs model inference, and returns results       |
| **Machine Learning**        | ANN model (Keras/Scikit-learn) | Predicts severity from audio features                                   |
| **Audio Processing**        | Librosa, NumPy                 | Extracts MFCC and spectral features                                     |
| **Visualization**           | Custom JS Meter                | Displays real-time severity estimation                                  |
| **Federated Learning Demo** | JavaScript Simulation          | Demonstrates how devices can train collaboratively without sharing data |

---

## Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/SafeSpeak.git
cd SafeSpeak
```

### Step 2: Install required dependencies

```bash
pip install flask librosa numpy scikit-learn matplotlib
```

### Step 3: Run the Flask application

```bash
python app.py
```

### Step 4: Open in your browser

Visit `http://127.0.0.1:5000` to access the application interface.

---

## Folder Structure

```
SafeSpeak/
│
├── static/
│   ├── index.html        # Main web interface
│   ├── style.css         # Styling file (optional if inline CSS used)
│   └── script.js         # Frontend logic
│
├── model/
│   └── model.h5          # Trained ANN model
│
├── app.py                # Flask backend script
└── README.md             # Documentation
```

---

## Key Features

* Audio-based emotional distress detection
* Privacy-focused design (no data stored or shared)
* Local ML model for real-time inference
* Federated Learning simulation for privacy-preserving training
* Integrated India-specific emergency helpline numbers
* Simple and lightweight deployment on any system

---

## Workflow

1. User uploads or records an audio file.
2. The file is sent to the Flask backend for analysis.
3. Features are extracted using **Librosa**.
4. The trained model predicts a severity score and classification label.
5. The result is displayed on a circular progress meter in the interface.
6. Helpline options are provided if distress is detected.

---

## Future Improvements

* Integrate real federated learning for distributed training.
* Add voice activity detection (VAD) for better noise handling.
* Expand to multimodal analysis (text + audio).
* Deploy a cloud-hosted version with end-to-end encryption.

---

## Disclaimer

This project is intended for **research and educational purposes only**.
It is **not a clinical or emergency diagnostic tool**.
If you or someone you know is in immediate danger, contact **112 (India Emergency Services)** or relevant authorities immediately.


