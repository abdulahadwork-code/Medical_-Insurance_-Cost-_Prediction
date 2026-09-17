# Medical Insurance Cost Prediction

## Project Overview

This project develops a Machine Learning model to predict an individual's medical insurance charges based on personal and demographic characteristics.

The project uses Multiple Linear Regression to estimate insurance costs from features such as age, BMI, number of children, smoking status, gender, and region.

The project also includes a Streamlit web application that allows users to enter their information and receive an estimated insurance cost.

---

## Problem Statement

Medical insurance costs can vary significantly between individuals based on factors such as age, BMI, smoking status, number of children, gender, and geographic region.

The goal of this project is to build a Machine Learning model that can learn the relationship between these characteristics and medical insurance charges and use that knowledge to predict estimated insurance costs for new customers.

---

## Dataset

The project uses the Medical Cost Personal Dataset.

The dataset contains 1,338 records and 7 columns.

### Features

- Age
- Gender
- BMI
- Number of children
- Smoking status
- Region

### Target Variable

- Charges

The `charges` column represents the medical insurance cost that the model is trained to predict.

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using Pandas.
2. Separated the features and target variable.
3. Identified numerical and categorical features.
4. Converted categorical variables into numerical values using one-hot encoding.
5. Split the dataset into training and testing sets.
6. Used 80% of the data for training and 20% for testing.

---

## Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the dataset and identify relationships between variables.

The following visualizations were created:

- Target variable distribution
- BMI vs insurance charges scatterplot
- Insurance charges boxplot
- Correlation matrix
- Correlation heatmap

### Key Findings

The insurance charges distribution is right-skewed, with most customers having relatively lower charges and a smaller number having very high charges.

The scatterplot showed a weak positive relationship between BMI and insurance charges.

Among the numerical variables, age showed the strongest positive correlation with insurance charges, followed by BMI.

The boxplot also showed several high-value outliers.

---

## Machine Learning Model

### Multiple Linear Regression

Multiple Linear Regression was selected to predict insurance charges using multiple input features.

The model was trained using the training dataset.

The training process was:

1. Prepare X and y.
2. Split the dataset into training and testing sets.
3. Create a Linear Regression model.
4. Train the model using the training data.
5. Generate predictions on the testing data.
6. Evaluate the predictions using regression metrics.

---

## Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Results

| Metric | Result |
|---|---:|
| MAE | ADD YOUR VALUE |
| MSE | ADD YOUR VALUE |
| RMSE | ADD YOUR VALUE |
| R² Score | ADD YOUR VALUE |

These values were calculated using the unseen testing dataset.

---

## Actual vs Predicted Results

The trained model was used to predict insurance charges for the testing data.

Example comparison:

| Actual Charges | Predicted Charges |
|---:|---:|
| ADD VALUE | ADD VALUE |
| ADD VALUE | ADD VALUE |
| ADD VALUE | ADD VALUE |
| ADD VALUE | ADD VALUE |
| ADD VALUE | ADD VALUE |

---

## Prediction Application

A Streamlit application was developed to allow users to enter:

- Age
- BMI
- Number of children
- Gender
- Smoking status
- Region

The application processes the input using the same encoding used during model training and passes it to the trained Linear Regression model.

The application then displays the estimated medical insurance cost.

---

## Screenshots

### Dataset Exploration

Add your dataset screenshot here.

### Exploratory Data Analysis

Add your histogram, scatterplot, and boxplot screenshots here.

### Correlation Analysis

Add your correlation heatmap screenshot here.

### Model Evaluation

Add your MAE, MSE, RMSE, and R² results here.

### Prediction Application

Add your Streamlit application screenshot here.

---

## Project Structure

```text
medical-insurance-cost-prediction/
│
├── app.py
├── insurance.csv
├── insurance_model.pkl
├── model_columns.pkl
├── requirements.txt
```

## Limitations
The model is based on the available dataset and may not represent every real-world insurance customer.
Linear Regression assumes a relatively linear relationship between the input features and insurance charges.
The dataset contains a limited number of features.
Predictions are estimates and should not be considered exact insurance quotations.
Model performance may vary when applied to data from a different population or insurance system.

## Future Improvements

Testing additional regression algorithms.
Hyperparameter tuning.
Feature engineering.
Using larger and more diverse datasets.
Comparing Linear Regression with Random Forest, Gradient Boosting, and XGBoost.
Deploying the application for public use.

## Technologies Used

Python
Pandas
NumPy
Scikit-learn
Streamlit
Joblib
Matplotlib
Seaborn

## Conclusion
This project demonstrates a complete Machine Learning workflow, from data loading and exploratory analysis to preprocessing, model training, evaluation, and deployment.
