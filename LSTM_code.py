import os
import random
import numpy as np
import pandas as pd
from typing import List, Optional, Tuple

# Note: Using scikit-learn for data prep and NumPy for reshaping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score
import joblib
# ---------------------
# Config (change these)
# ---------------------
SEED = 42
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

SEQ_LEN = 50  # number of past timesteps used as input
PRED_LEN = 1  # predict next PRED_LEN joint positions
INPUT_DIM = 8 # total number of input channels (IMU + FSR)
OUTPUT_DIM = 3  # number of regress outputs per timestep (Position_X, Y, Z)
NUM_CLASSES = None  # set to int e.g., 3 if you have intention labels, else None
HIDDEN_SIZE = 128
NUM_LAYERS = 2
BATCH_SIZE = 64
LR = 1e-3
EPOCHS = 600
WEIGHT_CLF = 1.0  # weight for classification loss relative to regression
PATIENCE = 8  # early stopping
GRAD_CLIP = 1.0

# --------------------------------
# Step 1: Load and Prepare Data
# --------------------------------
# NOTE: The file path must be correct for your machine.
file_path = r'C:\Users\YF80KY\OneDrive - Aalborg Universitet\Desktop\VIEXO_Shoulder Exo\neural_network_VIEXO\LSTM_Example.csv'
try:
    df = pd.read_csv(file_path, sep=";") #Your CSV file isn’t being split into multiple columns. Instead, the entire row is being read into a single column because the separator is ; but pd.read_csv by default uses ,
    print("Data loaded successfully.")

    # A check to print the columns and verify them.
    print(f"Columns in loaded file: {df.columns.tolist()}")

    # Clean column names by removing extra spaces
    df.columns = df.columns.str.strip()
    print(f"Cleaned column names: {df.columns.tolist()}")

except FileNotFoundError:
    print(f"Error: The file at path '{file_path}' was not found.")
    print("Please make sure the file path is correct.")
    exit()
# Take a quick look
#print(df.head())   # first 5 rows
#print(df.info())   # column info
#print(df.describe()) # statistics

#plt.plot(df["Acc_X"])
# Step 2: Separate features (X) and labels (y)
feature_columns = ['Acc_X', 'Acc_Y', 'Acc_Z', 'Gyro_X', 'Gyro_Y', 'Gyro_Z', 'FSR_1', 'FSR_2']
target_columns = ['Position_X', 'Position_Y', 'Position_Z']

X = df[feature_columns] # Features (the sensor data)
y = df[target_columns] # Labels (the ground-truth positions)

# Step 3: Normalize the input features AND the target labels
# This is a CRITICAL step to ensure the model can learn effectively.
# We need separate scalers for the input and output data.
input_scaler = MinMaxScaler()
X_scaled = input_scaler.fit_transform(X)

target_scaler = MinMaxScaler()
y_scaled = target_scaler.fit_transform(y)

# We save the scalers so we can de-normalize predictions later.
joblib.dump(input_scaler, 'input_scaler.pkl')
joblib.dump(target_scaler, 'target_scaler.pkl')

print("\nInput and target scalers saved to disk.")


# Step 4: Reshape data for LSTM
# The data needs to be reshaped from a 2D array to a 3D array
# with dimensions (samples, timesteps, features).
def create_sequences(features, labels, seq_len):
    """
    Correctly creates sequences for LSTM training by using separate
    features and labels.
    """
    xs = []
    ys = []
    for i in range(len(features) - seq_len):
        x = features[i:(i + seq_len)]
        # The output label is the single data point immediately after the sequence
        # We convert the labels to numpy array to avoid the AttributeError
        y = labels[i + seq_len]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

# Correctly call the function by passing both X_scaled and y
X_reshaped, y_reshaped = create_sequences(X_scaled, y_scaled, SEQ_LEN)

# Step 5: Split the reshaped data into training and testing sets
# We split sequentially because this is time-series data.
train_size = int(len(X_reshaped) * 0.8)
X_train = X_reshaped[:train_size]
y_train = y_reshaped[:train_size]

X_test = X_reshaped[train_size:]
y_test = y_reshaped[train_size:]

print("\nData splitting and normalization complete.")
print(f"Original data points: {len(X_scaled)}")
print(f"Number of sequences created: {len(X_reshaped)}")
print(f"Training data shape: {X_train.shape}")
print(f"Testing data shape: {X_test.shape}")
print(f"Features per timestep: {X_train.shape[2]}")
print(f"Timesteps per sample: {X_train.shape[1]}")

# Optional: Print a small sample of the normalized data to see the result
print("\nFirst 5 rows of normalized feature data (X_train):")
# We use a DataFrame to make the output easy to read and understand.
#print(pd.DataFrame(X_train, columns=feature_columns).head())
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  LSTM Code.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------
# Step 6: Define the LSTM Model
# --------------------------------
class LSTM_Model(nn.Module):
    """
    A simple LSTM model for time-series regression.
    """
    def __init__(self, input_dim, hidden_size, num_layers, output_dim):
        """
        Initializes the model's layers.
        
        Args:
            input_dim (int): The number of features per time step.
            hidden_size (int): The number of neurons in the hidden layers of the LSTM.
            num_layers (int): The number of LSTM layers stacked on top of each other.
            output_dim (int): The number of outputs to predict (e.g., 3 for x, y, z positions).
        """
        super(LSTM_Model, self).__init__()
        
        # Define the LSTM layer
        self.lstm = nn.LSTM(
            input_size=input_dim,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True # This makes the input tensor (batch, seq, features)
        )
        
        # Define the fully connected layer for the final output
        self.fc = nn.Linear(hidden_size, output_dim)
        
    def forward(self, x):
        """
        Defines the forward pass of the model.
        
        Args:
            x (torch.Tensor): The input tensor with shape (batch, seq_len, input_dim).
        
        Returns:
            torch.Tensor: The predicted output with shape (batch, output_dim).
        """
        # Pass the input through the LSTM layer
        # The output contains the hidden state for each time step.
        # The hidden_state and cell_state contain the final state of the last layer.
        lstm_out, (hidden_state, cell_state) = self.lstm(x)
        
        # We only care about the hidden state of the last time step.
        # This state summarizes the entire input sequence.
        # We use hidden_state[-1] to get the hidden state of the last layer.
        last_hidden_state = hidden_state[-1]
        
        # Pass the last hidden state through the fully connected layer to get the final prediction.
        out = self.fc(last_hidden_state)
        
        return out
    
# --------------------------------
# Step 7: Training Loop and Evaluation
# --------------------------------

# Convert numpy arrays to PyTorch tensors and move to the selected device (CPU or GPU)
X_train_tensor = torch.from_numpy(X_train).float().to(device)
y_train_tensor = torch.from_numpy(y_train).float().to(device) # .values to get the numpy array from the DataFrame
X_test_tensor = torch.from_numpy(X_test).float().to(device)
y_test_tensor = torch.from_numpy(y_test).float().to(device)

print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")

print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")
# Instantiate the model, loss function, and optimizer
model = LSTM_Model(
    input_dim=INPUT_DIM,
    hidden_size=HIDDEN_SIZE,
    num_layers=NUM_LAYERS,
    output_dim=OUTPUT_DIM
).to(device) # Move the model to the selected device

loss_function = nn.MSELoss() # Mean Squared Error is a standard loss for regression
optimizer = torch.optim.Adam(model.parameters(), lr=LR) # Adam is a popular optimizer

# Define lists to store loss history for plotting
train_losses = []
test_losses = []

print("\nStarting model training...")
# The main training loop
for epoch in range(EPOCHS):
    model.train() # Set the model to training mode
    
    # We will train on the entire dataset without batching for simplicity, 
    # but for larger datasets, you would use a DataLoader here.
    optimizer.zero_grad() # Clear previous gradients
    
    # Forward pass: get predictions from the model
    y_pred = model(X_train_tensor)
    
    # Calculate the training loss
    loss = loss_function(y_pred, y_train_tensor)
    
    # Backward pass: compute gradients
    loss.backward()
    
    # Update the model's weights
    optimizer.step()
    
    # Store training loss
    train_losses.append(loss.item())

    # Evaluation on the test set
    model.eval() # Set the model to evaluation mode
    with torch.no_grad(): # Disable gradient calculation for evaluation
        test_pred = model(X_test_tensor)
        test_loss = loss_function(test_pred, y_test_tensor)
        test_losses.append(test_loss.item())
    
    # Print progress every few epochs
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/{EPOCHS}], Train Loss: {loss.item():.4f}, Test Loss: {test_loss.item():.4f}")

print("\nTraining complete.")

# Optional: Plot the training and test loss
plt.figure(figsize=(10, 6))
plt.plot(train_losses, label='Training Loss')
plt.plot(test_losses, label='Testing Loss')
plt.title('Training and Testing Loss Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()    

# --------------------------------
# Step 8: Save the Trained Model
# --------------------------------
model_save_path = r'C:\Users\YF80KY\OneDrive - Aalborg Universitet\Desktop\VIEXO_Shoulder Exo\neural_network_VIEXO\lstm_position_model.pth'
torch.save(model.state_dict(), model_save_path)
print(f"\nModel saved to '{model_save_path}'.")