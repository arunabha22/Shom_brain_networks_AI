
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
import matplotlib.pyplot as plt

# Exact full path
file_path = r"C:\Users\YF80KY\OneDrive - Aalborg Universitet\Desktop\VIEXO_Shoulder Exo\neural_network_VIEXO\LearningNeuralNetwork.xlsx"

data_1 = pd.read_excel(file_path)  # reads all data into a pandas DataFrame

# Suppose columns A, B, C are inputs and D, E, F, G, H are outputs
input = ['Aa', 'Bb', 'Cc']   # replace with your Excel column names ##### Change here.
output = ['Dd', 'Ee', 'Ff', 'GGg'] ##### Change here.
output_cols = output
X = data_1[input].values
Y = data_1[output].values


# Standardize inputs and outputs for better optimization.
scaler_X = StandardScaler() # scaling for better performance.
scaler_Y = StandardScaler()

X_scaled = scaler_X.fit_transform(X)
Y_scaled = scaler_Y.fit_transform(Y)


# Neural Network Design.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..............................................................................................................................................................................................................................................................................................
# Step 5: Train-test split
num_train_rows = int(0.8 * len(data_1))   # customize ##### Change here.
num_test_rows = len(data_1) - num_train_rows    # customize ##### Change here.

# Random shuffle indices
total_rows = len(data_1)
indices = np.random.permutation(total_rows) # generate numbers in different permutation at random between 0-total no. of rows.


train_idx = indices[:num_train_rows] #use the generated random numbers inside indices as the means to select the random rows. also total rows selected is total number of train rows(0-800).
test_idx = indices[num_train_rows:num_train_rows+num_test_rows] #use the generated random numbers inside indices as the means to select the  random rows. also total rows selected is total number of test rows (800-1000).

X_train, X_test = X_scaled[train_idx], X_scaled[test_idx] #assisgn input X and output Y for both training and testing. 
Y_train, Y_test = Y_scaled[train_idx], Y_scaled[test_idx]


# Step 6: Build Neural Network
num_inputs = X_train.shape[1]
num_outputs = Y_train.shape[1]

model = Sequential([
    Dense(20, activation='relu', input_shape=(num_inputs,)), ##### Change here. also change the activation function.
    Dense(20, activation='sigmoid'),                          ##### Change here. add more DENSE in order to add more hidden layers. 
    #SimpleRNN(32, activation='tanh', input_shape=(timesteps, num_features), return_sequences=True),
    Dense(num_outputs)  # linear activation for regression
]) #You can change number of layers, neurons, and activation functions if needed.

# Step 7: Compile model
optimizer_choice = 'adam'   # can be 'sgd', 'rmsprop', etc. ##### Change here.
model.compile(optimizer=optimizer_choice, loss='mse') 

# --------------------------
# Step 5: Custom Callback to Track Per-Output MSE
# --------------------------
class PerOutputMSECallback(tf.keras.callbacks.Callback):
    def __init__(self, X_train, Y_train, X_test, Y_test):
        self.X_train = X_train
        self.Y_train = Y_train
        self.X_test = X_test
        self.Y_test = Y_test
        self.train_mse = []
        self.test_mse = []
# saving the MSE values for test and train 
    def on_epoch_end(self, epoch, logs=None):
        Y_train_pred = self.model.predict(self.X_train, verbose=0)
        Y_test_pred = self.model.predict(self.X_test, verbose=0)

        mse_train = np.mean((self.Y_train - Y_train_pred) ** 2, axis=0)
        mse_test = np.mean((self.Y_test - Y_test_pred) ** 2, axis=0)

        self.train_mse.append(mse_train)
        self.test_mse.append(mse_test)

# Instantiate callback
per_output_cb = PerOutputMSECallback(X_train, Y_train, X_test, Y_test)


# Step 8: Train the model
epochs = 200 # customize number of epochs
history = model.fit(
    X_train, 
    Y_train, 
    validation_data=(X_test, Y_test), 
    epochs=epochs, 
    batch_size=10, #change the batch size in order to have better results
    callbacks=[per_output_cb], 
    verbose=1
    )


# Convert lists to arrays for easy plotting
train_mse_arr = np.array(per_output_cb.train_mse)
test_mse_arr = np.array(per_output_cb.test_mse)


# Convert results into DataFrame
epochs_range = range(1, epochs+1)
mse_df = pd.DataFrame({
    "Epoch": epochs_range,
    **{f"Train_{col}": train_mse_arr[:, i] for i, col in enumerate(output_cols)},
    **{f"Test_{col}": test_mse_arr[:, i] for i, col in enumerate(output_cols)},
})



# Save to Excel

# Define save path change according to your requirement
save_path = r"C:\Users\YF80KY\OneDrive - Aalborg Universitet\Desktop\VIEXO_Shoulder Exo\neural_network_VIEXO\MSE_per_output.xlsx"

# Save MSE to Excel at desired location
mse_df.to_excel(save_path, index=False)

print(f"MSE per output saved at: {save_path}")



# ------------------------
# Plot separate line graphs per output
# ------------------------
output_labels = [f'Output {i+1}' for i in range(num_outputs)]

for i in range(num_outputs):
    plt.figure(figsize=(8,5))
    plt.plot(range(1, epochs+1), train_mse_arr[:, i], label='Train MSE', color='blue')
    plt.plot(range(1, epochs+1), test_mse_arr[:, i], label='Test MSE', color='red')
    plt.xlabel('Epoch')
    plt.ylabel('MSE')
    plt.title(f'MSE vs Epoch for {output_labels[i]}')
    plt.legend()
    plt.grid(True)
    plt.show()


Y_pred = model.predict(X_test)

num_outputs = Y_test.shape[1]
mse_per_output = []

for i in range(num_outputs):
    mse_i = np.mean((Y_test[:, i] - Y_pred[:, i])**2)
    mse_per_output.append(mse_i)

print("MSE per output:", mse_per_output)


plt.bar(range(num_outputs), mse_per_output)
plt.xlabel('Output Index')
plt.ylabel('MSE')
plt.title('MSE for Each Output')
plt.show()

num_outputs = Y_train.shape[1]
epochs = len(history.history['loss'])

# Initialize arrays to store MSE for each output per epoch
train_mse_per_output = np.zeros((epochs, num_outputs))
test_mse_per_output = np.zeros((epochs, num_outputs))


# ------------------------
#### saving all weights ##################3
# ------------------------
all_weights = {}

for i, layer in enumerate(model.layers):
    weights, biases = layer.get_weights()
    all_weights[f"Layer{i+1}_weights"] = weights.flatten()
    all_weights[f"Layer{i+1}_biases"] = biases.flatten()

weights_df = pd.DataFrame(dict([(k, pd.Series(v)) for k,v in all_weights.items()]))

# Define save path change according to your requirement
save_path = r"C:\Users\YF80KY\OneDrive - Aalborg Universitet\Desktop\VIEXO_Shoulder Exo\neural_network_VIEXO\NN_Weights.xlsx"
weights_df.to_excel(save_path, index=False)

print(f"Neural network weights saved at: {save_path}")

