# Freezing of Gait Prediction

## Overview
This repository contains a Python script (`predict_fog.py`) that predicts whether a patient has Freezing of Gait (FOG) using a pre-trained Support Vector Machine (SVM) model. The model utilizes brain area feature values stored in an Excel file (`area.xlsx`) and scales them using a saved scaler (`scalar_for_area.pkl`).

## Prerequisites
Ensure you have the following installed on your system:

- Python 3.x
- Required Python packages (see Installation section below)
- `area.xlsx` file containing the patient data
- `scale_data.pkl` for data normalization
- `predict_output.pkl` pre-trained machine learning model

## Installation

Clone this repository and navigate to the project folder:

```sh
git clone https://github.com/EN4D2Lab/FreezingOfGaitPrediction.git
cd FreezingOfGaitPrediction
```

Install the required dependencies:

```sh
pip install pandas joblib openpyxl
```

## Preparing the Data

1. Ensure the `area.xlsx` file is present in the project folder. This file should contain columns representing different brain regions' areas, and fill in the values (cortical area data) as per the same columns for the patients you want to test/predict whether they are FOG or not.
2. The script selects specific features for prediction. If you modify `area.xlsx`, ensure that it retains the necessary columns listed in `selected_features` inside `predict_fog.py`.
3. The `area.xlsx` file should not have less than 68 columns in it; otherwise, the code will throw an error. Ensure that the data is properly updated under each column name without renaming or deleting columns.
4. If `area.xlsx` is empty, the script will prompt you to add data before proceeding.

## Running the Prediction Script

Execute the script using:

```sh
python predict_fog.py
```

### Expected Output
The script will load the patient data, preprocess it using `scalar_for_area.pkl`, and pass it to the trained `svm_model_for_area.pkl`. It will then output:

For each row in `area.xlsx`, the script will predict:
- **"Row X: The provided data shows that the patient has No Freezing of Gaits"** (if prediction is 1)
- **"Row X: The provided data shows that the patient has a Freezing of Gaits"** (if prediction is 0)

## Understanding the Code
- **Data Loading:** Reads `area.xlsx` using `pandas`. If the file is empty, it prompts the user to add data.
- **Scaling:** Uses `scalar_for_area.pkl` to normalize the data.
- **Feature Selection:** Selects a predefined list of brain region features. These column names should not be changed as they are essential for prediction.
- **Model Loading & Prediction:** Uses `svm_model_for_area.pkl` to predict FoG for each row in `area.xlsx`.
- **Output:** Displays the prediction results row by row in the console.

## Issues & Contributions
If you encounter issues or want to contribute, feel free to open an issue or submit a pull request.

---

