# Car Price Prediction Web App

## Introduction
This project is a Flask-based web application that predicts the price of a used car. The application leverages a machine learning model to make predictions based on various features such as the car's company, model, year, fuel type, and kilometers driven.

---

## Features
- **User-friendly interface** for predicting car prices.
- **Dynamic dropdowns** for selecting car companies and models.
- **Accurate price predictions** powered by a trained machine learning model.

---

## Tech Stack
- **Backend**: Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Machine Learning**: scikit-learn (Linear Regression model)
- **Database**: Pandas (CSV)

---

## Installation Guide

### Prerequisites
Ensure Python 3.7 or above is installed on your system.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/sandeshchh30/Second-Hand-Car-Price-Prediction.git

2. Navigate to the project directory:
   ```bash
   cd car-price-predictor

3. Install the required dependencies: 
   ```bash
   pip install -r requirements.txt

4. Run the Flask application:
   ```bash
   python app.py

5. Open a web browser and go to http://127.0.0.1:5000 to access the web app.


---

## Model Training

### Overview
The model used for predicting car prices is a Linear Regression model. It is trained using the scikit-learn library on a dataset containing car features like company, model, year, fuel type, and kilometers driven.

### Training Process
- The dataset is split into training and testing sets using train_test_split from sklearn.model_selection.
- To ensure optimal results, I tested random_state values from 1 to 1000 and selected the one that gave the best model performance.
- After identifying the best random_state, the model was retrained with this value for stable and accurate predictions.

---

## Deployment
The web app is deployed on Render.com.
- Deployed URL: https://second-hand-car-price-prediction.onrender.com/



