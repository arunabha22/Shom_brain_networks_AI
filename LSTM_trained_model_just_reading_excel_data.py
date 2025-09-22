import os
import random
import numpy as np
import pandas as pd
from typing import List, Optional, Tuple
import time

import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler
import joblib

# ---------------------
# Config
# ---------------------
# These must be the SAME as your training script
SEQ_LEN = 50  # number of past timesteps used as input
INPUT_DIM = 8 # total number of input channels (IMU + FSR)
OUTPUT_DIM = 3  # number of regress outputs per timestep (Position_X, Y, Z)
HIDDEN_SIZE = 128
NUM_LAYERS = 2
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# File Path Config
data_file_path = r'C:\Users\YF80KY\OneDrive - Aalborg Universitet\Desktop\VIEXO_Shoulder Exo\neural_network_VIEXO\LSTM_Example.csv'

# --------------------------------
# Step 1: Define the LSTM Model
# --------------------------------
# We need to redefine the model class so we can load the trained weights into it.
class LSTM_Model(nn.Module):
    """
    A simple LSTM model for time-series regression.
    """
    def __init__(self, input_dim, hidden_size, num_layers, output_dim):
        """
        Initializes the model's layers.
        """
        super(LSTM_Model, self).__init__()
        
        self.lstm = nn.LSTM(
            input_size=input_dim,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )
        
        self.fc = nn.Linear(hidden_size, output_dim)
        
    def forward(self, x):
        """
        Defines the forward pass of the model.
        """
        lstm_out, (hidden_state, cell_state) = self.lstm(x)
        last_hidden_state = hidden_state[-1]
        out = self.fc(last_hidden_state)
        
        return out

# --------------------------------
# Step 2: Load the Trained Model and Scalers
# --------------------------------
model_path = r'C:\Users\YF80KY\OneDrive - Aalborg Universitet\Desktop\VIEXO_Shoulder Exo\neural_network_VIEXO\lstm_position_model.pth'
input_scaler_path = 'input_scaler.pkl'
target_scaler_path = 'target_scaler.pkl'

try:
    # Instantiate the model architecture
    model = LSTM_Model(
        input_dim=INPUT_DIM,
        hidden_size=HIDDEN_SIZE,
        num_layers=NUM_LAYERS,
        output_dim=OUTPUT_DIM
    ).to(device)

    # Load the saved state dictionary
    model.load_state_dict(torch.load(model_path))
    model.eval() # Set the model to evaluation mode

    # Load the scalers
    input_scaler = joblib.load(input_scaler_path)
    target_scaler = joblib.load(target_scaler_path)

    print("Model and scalers loaded successfully.")

except FileNotFoundError:
    print(f"Error: One or more files were not found.")
    print(f"Please ensure '{model_path}', '{input_scaler_path}', and '{target_scaler_path}' exist.")
    exit()

# --------------------------------
# Step 3: Load Data from File
# --------------------------------
print("\nLoading data from file for a single prediction...")
try:
    df = pd.read_csv(data_file_path, sep=";")
    df.columns = df.columns.str.strip()
    
    # We will use the last SEQ_LEN rows for our prediction
    feature_columns = ['Acc_X', 'Acc_Y', 'Acc_Z', 'Gyro_X', 'Gyro_Y', 'Gyro_Z', 'FSR_1', 'FSR_2']
    last_sequence_df = df[feature_columns].tail(SEQ_LEN)
    new_data_unscaled = last_sequence_df.values
    
    if len(new_data_unscaled) != SEQ_LEN:
        print("Error: The file does not contain enough data points for a full sequence.")
        print(f"Required: {SEQ_LEN}, Found: {len(new_data_unscaled)}")
        exit()

except FileNotFoundError:
    print(f"Error: The data file at '{data_file_path}' was not found.")
    exit()

# --------------------------------
# Step 4: Normalize and Predict
# --------------------------------
# Reshape the data to match the model's input shape (batch_size, seq_len, features)
new_data_scaled = input_scaler.transform(new_data_unscaled)
new_data_tensor = torch.from_numpy(new_data_scaled).float().unsqueeze(0).to(device)

print("Making a prediction...")
with torch.no_grad():
    prediction_normalized = model(new_data_tensor)

# Convert the output back to a numpy array
prediction_normalized_np = prediction_normalized.cpu().numpy()

# --------------------------------
# Step 5: Denormalize the Prediction
# --------------------------------
# The model's output is normalized, so we need to use the target scaler
# to transform it back to the original units.
prediction_denormalized = target_scaler.inverse_transform(prediction_normalized_np)

# Extract the final prediction
predicted_position = prediction_denormalized[0]

# --------------------------------
# Step 6: Display the Final Result
# --------------------------------
print("\nPrediction complete!")
print("The predicted position for the last sequence in the file is:")
print(f"Position_X: {predicted_position[0]:.4f}")
print(f"Position_Y: {predicted_position[1]:.4f}")
print(f"Position_Z: {predicted_position[2]:.4f}")
