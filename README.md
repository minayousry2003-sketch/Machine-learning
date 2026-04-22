# 🩺 Diabetes Detection Web Application

A machine learning-powered web application that predicts whether a patient is likely to have diabetes based on medical input data. The project combines **data science** and **web development** to deliver a real-world healthcare solution.

---

## 🚀 Project Overview

This project aims to:

* Predict diabetes risk using patient health data
* Provide a simple and accessible web interface
* Bridge the gap between machine learning models and real-world usage

The system takes user input (medical attributes) and returns a prediction:

* **Positive (Diabetes)**
* **Negative (No Diabetes)**

---

## 📊 Dataset Description

The dataset used is `diabetes.csv`.

### 🔢 Dataset Info:

* Number of records: **768**
* Number of features: **8 input features**
* Target variable: **Outcome (0 or 1)**

### 🧾 Features:

| Feature                  | Description                |
| ------------------------ | -------------------------- |
| Pregnancies              | Number of times pregnant   |
| Glucose                  | Blood glucose level        |
| BloodPressure            | Blood pressure value       |
| SkinThickness            | Skin thickness measurement |
| Insulin                  | Insulin level              |
| BMI                      | Body Mass Index            |
| DiabetesPedigreeFunction | Genetic influence factor   |
| Age                      | Patient age                |

### 🎯 Target:

* `0` → No Diabetes
* `1` → Diabetes

---

## ⚠️ Data Preprocessing

Some features contain **invalid zero values** (e.g., Glucose, BMI, Insulin).
These were handled by:

* Replacing zeros with **median values**
* Cleaning data before training the model

---

## 🤖 Machine Learning Model

### ✅ Algorithm Used:

* Logistic Regression

### 💡 Why?

* Simple and interpretable
* Works well for binary classification
* Fast and efficient

### 🔄 Workflow:

1. Load dataset
2. Clean and preprocess data
3. Split into training and testing sets
4. Train the model
5. Evaluate performance

---

## 📈 Evaluation Metrics

The model is evaluated using:

* **Accuracy** (~77–80%)
* **Precision**
* **Recall**
* **F1-Score**

### 📊 Visual Metrics:

* Confusion Matrix
* ROC Curve (AUC Score)

---

## 🌐 Web Application

The model is integrated into a web app using Django.

### 🔧 Features:

* User inputs medical data
* Data is sent to the backend
* Model predicts result
* Output displayed instantly

---

## 💻 Project Structure

```
project/
│
├── diabetes.csv          # Dataset
├── model.py / notebook   # ML model training
├── views.py              # Django logic
├── templates/            # HTML files
├── static/               # Images / CSS
└── manage.py             # Django entry point
```

---

## ▶️ How to Run

### 1. Install Requirements

```bash
pip install pandas numpy scikit-learn django
```

### 2. Run Django Server

```bash
python manage.py runserver
```

### 3. Open Browser

```
http://127.0.0.1:8000/
```

---

## 🎯 Expected Output

Example:

| Input                         | Output   |
| ----------------------------- | -------- |
| Glucose=148, BMI=33.6, Age=50 | Positive |
| Glucose=85, BMI=26.6, Age=31  | Negative |

---

## 🔮 Future Improvements

* Use advanced models (Random Forest, SVM)
* Save trained model using `joblib`
* Deploy on cloud (AWS / Heroku)
* Improve UI/UX
* Add data visualization dashboard

---

## 🧠 Conclusion

This project demonstrates how machine learning can be transformed into a **practical healthcare solution** by integrating it with a web application.

---

## 👨‍💻 Author

**Mina Yousry Saad**
Computer Science Student – Faculty of Science
Tanta University

---
