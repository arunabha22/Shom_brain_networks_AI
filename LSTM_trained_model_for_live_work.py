import os
import random
import numpy as np
import pandas as pd
from typing import List, Optional, Tuple
import time

try:
    import serial
except ImportError:
    print("The 'pyserial' library is not installed.")
    print("Please install it using: pip install pyserial")
    exit()

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
OUTPUT_DIM = 3 # number of regress outputs per timestep (Position_X, Y, Z)
HIDDEN_SIZE = 128
NUM_LAYERS = 2
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Serial Port Config
# TODO: REPLACE WITH YOUR ACTUAL PORT AND BAUD RATE
SERIAL_PORT = 'COM3' # Example: 'COM3' on Windows, '/dev/ttyACM0' on Linux
BAUD_RATE = 115200


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
# Step 3: Real-Time Prediction Loop
# --------------------------------
# This list will act as a sliding window of sensor data
data_window = []

# Function to read a single data point from your sensors
# TODO: You MUST replace this with your actual sensor reading function.
# This function should return a numpy array of shape (1, 8)
# in the order of Acc_X, Acc_Y, Acc_Z, Gyro_X, Gyro_Y, Gyro_Z, FSR_1, FSR_2.
def read_sensor_data():
    # Simulate reading a new data point from hardware
    # Replace this with your actual code to read from the Teensy's USB serial port
    # and parse the data string into a numpy array.
    
    # For now, we'll just return random data to simulate a live stream.
    return np.random.rand(1, INPUT_DIM)


print("\nStarting real-time prediction loop.")
print("Waiting for data stream...")

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Successfully connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
    
    # Give the serial connection a moment to initialize
    time.sleep(2)

    while True:
        # Read a new data point from your sensors
        new_data_point = read_sensor_data()
        
        # Add the new data point to our sliding window
        data_window.append(new_data_point[0])
        
        # Keep the window at the correct size
        if len(data_window) > SEQ_LEN:
            data_window.pop(0)

        # Only make a prediction once the window is full
        if len(data_window) == SEQ_LEN:
            # Reshape the window for the model
            input_sequence = np.array(data_window).reshape(1, SEQ_LEN, INPUT_DIM)
            
            # Normalize the input sequence
            input_sequence_scaled = input_scaler.transform(input_sequence.reshape(-1, INPUT_DIM)).reshape(1, SEQ_LEN, INPUT_DIM)
            
            # Convert to PyTorch tensor and move to device
            input_tensor = torch.from_numpy(input_sequence_scaled).float().to(device)
            
            # Make a prediction
            with torch.no_grad():
                prediction_normalized = model(input_tensor)
                
            # Convert the output back to a numpy array
            prediction_normalized_np = prediction_normalized.cpu().numpy()
            
            # Denormalize the prediction
            predicted_position = target_scaler.inverse_transform(prediction_normalized_np)[0]
            
            # Print and send the prediction to the Teensy board
            pos_x, pos_y, pos_z = predicted_position
            output_string = f"{pos_x:.4f},{pos_y:.4f},{pos_z:.4f}\n"
            
            # Send the data over serial
            ser.write(output_string.encode('utf-8'))
            
            # Print to console for monitoring
            print(f"Predicted Position: X={pos_x:.4f}, Y={pos_y:.4f}, Z={pos_z:.4f}")
            
            # Small delay to avoid overwhelming the system
            time.sleep(0.01)

except serial.SerialException as e:
    print(f"Serial Port Error: {e}")
    print(f"Please check if {SERIAL_PORT} is correct and the Teensy board is connected.")
except KeyboardInterrupt:
    print("\nPrediction loop stopped by user.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed.")
