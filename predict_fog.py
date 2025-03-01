#!/usr/bin/env python3
# -*- coding: utf-8 -*-

test_rows = [0, 1, 2, 16, 17, 18, 19]

import pandas as pd
import joblib
import warnings

warnings.filterwarnings('ignore')

# Load your cortical area data for the patients you want test for FOG or not
area_df = pd.read_excel("area.xlsx")

# Check if there is data
if area_df.empty:
    print("Please add data or records in area.xlsx")
else:
    # Load scaler and model
    sc = joblib.load("scalar_for_area.pkl")
    loaded_model = joblib.load("svm_model_for_area.pkl")

    # Scale data
    area_scaled_numpy_data = sc.transform(area_df)
    area_df_scaled = pd.DataFrame(area_scaled_numpy_data, columns=area_df.columns)

    # Selected features
    # Do not change any column name from these, since these are selected as predictive features by our model
    selected_features = [
        'lh_inferiorparietal_area', 'lh_lingual_area', 'lh_medialorbitofrontal_area', 
        'lh_middletemporal_area', 'lh_parahippocampal_area', 'lh_parsopercularis_area', 
        'lh_parsorbitalis_area', 'lh_pericalcarine_area', 'lh_rostralanteriorcingulate_area', 
        'lh_superiorfrontal_area', 'lh_supramarginal_area', 'lh_temporalpole_area', 'lh_insula_area', 
        'rh_bankssts_area', 'rh_cuneus_area', 'rh_lingual_area', 'rh_middletemporal_area', 
        'rh_pericalcarine_area', 'rh_precuneus_area', 'rh_superiortemporal_area', 
        'rh_supramarginal_area', 'rh_frontalpole_area', 'rh_temporalpole_area', 
        'rh_transversetemporal_area'
    ]

    # Filter data for selected features
    filtered_area_df = area_df_scaled[selected_features]

    # Iterate over each row for prediction
    for index, row in filtered_area_df.iterrows():
        area_test_list = [row.to_list()]
        prediction = loaded_model.predict(area_test_list)

        result = "No Freezing of Gaits" if prediction[0] == 1 else "Freezing of Gaits"
        print(f"Row {index + 1}: The provided data shows that the patient has {result}")
