# Credit Card Fraud Detection

## 📌 Project Overview

Credit Card Fraud Detection is a Machine Learning project developed to identify fraudulent and non-fraudulent credit card transactions. The project uses Python and machine learning techniques to analyze transaction data, handle class imbalance, visualize transaction patterns, and build classification models for fraud detection.

The project uses a Kaggle credit card transaction dataset and focuses on understanding how machine learning can be applied to an imbalanced classification problem.

## 🎯 Objective

The main objective of this project is to develop a machine learning model that can classify credit card transactions as:

* **0 → Normal Transaction**
* **1 → Fraudulent Transaction**

The project also focuses on reducing the chances of missing fraudulent transactions by properly handling the highly imbalanced dataset.

## 📊 Dataset

The project uses the **Credit Card Fraud Detection Dataset 2023** from Kaggle.

🔗 **Dataset:** https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023

The dataset contains over 550,000 anonymized credit card transaction records and includes a `Class` column representing normal and fraudulent transactions.

> The dataset is not included in this repository. Please download it from Kaggle and place the CSV file in the project folder.

## 🔧 Technologies Used

* **Python**
* **Pandas** – Data processing and analysis
* **NumPy** – Numerical operations
* **Scikit-learn** – Machine learning models and evaluation
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical visualization
* **Imbalanced-learn** – Handling class imbalance using SMOTE
* **Streamlit** – Displaying project visualizations through a web interface

## 🔄 Project Workflow

1. Import the Kaggle credit card fraud dataset.
2. Explore and understand the dataset.
3. Check for missing values.
4. Perform Exploratory Data Analysis (EDA).
5. Visualize normal and fraudulent transactions.
6. Analyze feature correlations.
7. Handle class imbalance using **SMOTE**.
8. Split the data into training and testing sets.
9. Scale the required features.
10. Train machine learning classification models.
11. Evaluate the models using suitable performance metrics.
12. Display important visualizations using Streamlit.

## 📈 Exploratory Data Analysis

The project includes:

* **Bar Graph** – Fraud vs Non-Fraud transactions
* **Histogram** – Transaction amount distribution
* **Box Plot** – Comparison of transaction amounts by class
* **Correlation Heatmap** – Relationship between dataset features

## ⚖️ Handling Class Imbalance

Credit card fraud datasets contain significantly fewer fraudulent transactions compared to normal transactions.

To handle this imbalance, **SMOTE (Synthetic Minority Over-sampling Technique)** is used to generate synthetic samples for the minority class.

This helps the machine learning models learn fraudulent transaction patterns more effectively.

## 🤖 Machine Learning Models

The project uses classification models such as:

* Logistic Regression
* Random Forest

## 📊 Model Evaluation

The models are evaluated using:

* Confusion Matrix
* Precision
* Recall
* F1-Score
* ROC-AUC

## 🌐 Streamlit Visualization

Streamlit is used to display the dataset and EDA visualizations through a simple web interface.

Run the application using:

```bash
python -m streamlit run app.py
```

## 📁 Project Structure

```text
Credit-Card-Fraud-Detection/
│
├── app.py
├── requirements.txt
├── README.md
└── creditcard.csv
```

> The dataset may be excluded from the repository due to its size and licensing terms. Download it directly from the Kaggle link provided above.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
```

### 2. Open the project folder

```bash
cd Credit-Card-Fraud-Detection
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Download the dataset

Download the dataset from:

https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023

Place the CSV file in the project folder.

### 5. Run the Streamlit application

```bash
python -m streamlit run app.py
```

## 📚 Learning Outcome

Through this project, I learned the basic workflow of a Machine Learning classification project, including:

* Data preprocessing
* Exploratory Data Analysis
* Data visualization
* Handling imbalanced datasets
* SMOTE
* Machine learning classification
* Model evaluation
* Streamlit-based visualization

## 👨‍💻 Project Type

**Academic / Student Machine Learning Project**

This project was developed for learning and demonstrating the basic concepts of Machine Learning and data analysis.

