#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:56:27 2024

@author: gauravrathi
"""

import pandas as pd
import joblib

import warnings
warnings.filterwarnings('ignore')

area_df = pd.read_excel("area.xlsx")

sc = joblib.load("scalar_for_area.pkl")

test_rows = [0, 1, 2, 16, 17, 18, 19]

# print(area_df)
all_columns = area_df.columns.tolist()

area_scaled_numpy_data = sc.transform(area_df)
area_df_scaled = pd.DataFrame(area_scaled_numpy_data, columns=area_df.columns)
all_columns_scaled = area_df_scaled.columns.tolist()

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

# Select only the required columns
filtered_area_df = area_df_scaled[selected_features]

for i in range(7):
    area_test_list = [(filtered_area_df.iloc[test_rows[i]]).to_list()] 
     
    # Test the loaded model
    loaded_model = joblib.load("svm_model_for_area.pkl")
    predictions = loaded_model.predict(area_test_list)
    
    if(predictions[0] == 1):
        print("The provided data shows that the paitent have No Freezing of Gaits")
    else:    
        print("The provided data shows that the paitent have a Freezing of Gaits")