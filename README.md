# 🌾🤖 AgriBot – AI-Powered Farmer Chatbot

**Empowering agriculture with artificial intelligence to help farmers make smarter, data-driven decisions.**

AgriBot is an intelligent chatbot assistant built to support farmers with real-time crop advice and plant disease diagnosis. It combines **Machine Learning**, **Deep Learning**, and a user-friendly chat interface to deliver powerful tools for modern, sustainable agriculture.

---

## 🚀 Key Features

- 🌱 **Crop Recommendation System**  
  Suggests the best crop to cultivate based on soil nutrients, climate, and previous yield data using **Random Forest** and **XGBoost** models.

- 🦠 **Plant Disease Detection**  
  Uses deep learning (**ResNet-99**) to analyze plant leaf images and detect diseases with remedy suggestions.

- 💬 **Interactive Chatbot Interface**  
  Real-time AI-powered chatbot to guide farmers through queries and recommendations in a conversational manner.

- 📈 **Sustainable Farming Support**  
  Encourages practices that boost productivity, reduce losses, and support eco-friendly agriculture.

---

## 🧠 Tech Stack

| Layer        | Technologies Used                            |
|--------------|-----------------------------------------------|
| Frontend     | HTML, CSS, JS, Chat UI                        |
| Backend      | Python, Flask, Django (dual app run)          |
| ML Models    | Random Forest, XGBoost                        |
| DL Models    | ResNet-99 (for image classification)          |
| Tools        | OpenCV, Scikit-learn, Keras, TensorFlow       |
| Database     | WAMP Server (MySQL)                           |
| Deployment   | Localhost (Anaconda Terminal, Flask, Django)  |

---

## 🛠️ Setup & Installation Guide

### 🔁 Step-by-Step Instructions:

1. **Open Anaconda Navigator**
2. **Create a new environment**  
   - Name: `AgriBot`  
   - Python version: `3.8`
3. **Open terminal** (Play button → Open Terminal) in the new environment.
4. **Install dependencies** (run one by one):

```bash
pip install tensorflow
conda install -c conda-forge keras
conda install -c anaconda scikit-learn
conda install -c conda-forge opencv
conda install -c anaconda scikit-image
conda install -c anaconda flask
pip install pandas
pip install werkzeug==2.3.7


# Terminal 1
python app.py

# Terminal 2
python manage.py runserver


🤝 Contribution
Feel free to fork, star ⭐, or contribute improvements to this project!

                                                                 "Technology rooted in soil – for farmers, by innovation.”

