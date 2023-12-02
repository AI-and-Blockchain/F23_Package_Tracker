import torch
from torch.utils.data import Subset
from torch.utils import data
import torch.optim as optim
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
import pandas as pd
import math
from sklearn.preprocessing import MinMaxScaler

class TrafficModel(nn.Module):
    def __init__(self, output_size, input_size, hidden_size, num_layers):
        super().__init__()
        self.output_size = output_size
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, batch_first=True, dropout=0.2)
        self.fc_1 = nn.Linear(hidden_size, hidden_size)
        self.fc_2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        # Init hidden and cell states
        h_0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        c_0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        
        # Propagate through LSTM
        output, (hn, cn) = self.lstm(x, (h_0, c_0))
        x = self.relu(hn)
        x = self.fc_1(x)
        x = self.relu(x)
        x = self.fc_2(x)
        return x


def train(epoch, batch_size, lstm, optimiser, loss, x_train, y_train, x_test, y_test):
    lstm.train()
    
    train_batches = len(x_train) // batch_size
    test_batches = len(x_test) // batch_size
    x_batch = torch.FloatTensor()
    y_batch = torch.FloatTensor()
    running_loss = 0
    test_loss = 0
    for batch in range(train_batches + 1):
        if (batch == train_batches):
            x_batch = x_train[batch_size * batch :]
            y_batch = y_train[batch_size * batch :]
        else:
            x_batch = x_train[batch_size * batch : batch_size * (batch+1)]
            y_batch = y_train[batch_size * batch : batch_size * (batch+1)]
        
        optimiser.zero_grad()
        outputs = lstm.forward(x_batch)
        
        outputs = outputs.type(torch.FloatTensor)
        y_batch = y_batch.type(torch.FloatTensor)
                
        _loss = loss(outputs, y_batch)
        _loss.backward()
        optimiser.step()
        
        running_loss += _loss
        
    # Test
    lstm.eval()
    for batch in range(test_batches + 1):
        if (batch == test_batches):
            x_batch = x_test[batch_size * batch :]
            y_batch = y_test[batch_size * batch :]
        else:
            x_batch = x_test[batch_size * batch : batch_size * (batch+1)]
            y_batch = y_test[batch_size * batch : batch_size * (batch+1)]
        
        outputs = lstm(x_batch)
        outputs = outputs.type(torch.FloatTensor)
        y_batch = y_batch.type(torch.FloatTensor)
        
        test_loss += loss(outputs, y_batch)
    
    print(f"Epoch {epoch+1} --- Loss: {running_loss} | Test loss: {test_loss}")

def prep_input(hour, minute, id):
    sample = torch.Tensor(np.array([hour, minute, id]))
    sample = torch.reshape(sample, (1, 1, 3))
    return sample

def predict(model, xscaler, yscaler, hour, minute, id):
    #sample = torch.Tensor(xscaler.transform(np.array([hour, minute, id]).reshape(1,3)))
    sample = torch.Tensor(np.array([hour, minute, id]))
    sample = torch.reshape(sample, (1, 1, 3))
    return math.floor(yscaler.inverse_transform(np.array(model(sample)[0].item()).reshape(1,-1)).item()) // 2


if __name__ == "__main__":
    # Load dataset    
    df = pd.read_csv("datasets/2016-volumes.csv", index_col=0)
    df.drop(columns=["requestid", "boro", "yr", "m", "d", "wktgeom", "street", "fromst", "tost", "direction"], inplace=True)
    
    # Extract input and output data
    x, y = df.drop(columns=["vol"]), df.vol.values
        
    # Perform any data transformations on x or y here...
    xfit = MinMaxScaler()
    yfit = MinMaxScaler()
    x = xfit.fit_transform(x)
    y = yfit.fit_transform(y.reshape(len(y), 1))
    x, y = np.array(x), np.array(y)
    
    # Split into training and test sets
    train_ratio = 0.9
    train_cutoff = math.floor(len(x) * train_ratio)
    x_train, x_test = torch.Tensor(x[:train_cutoff]), torch.Tensor(x[train_cutoff:])
    y_train, y_test = torch.Tensor(y[:train_cutoff]), torch.Tensor(y[train_cutoff:])
    
    # Prepare datasets for interacting with the model
    x_train = torch.reshape(x_train, (x_train.shape[0], 1, x_train.shape[1]))
    x_test = torch.reshape(x_test, (x_test.shape[0], 1, x_test.shape[1]))
    
    # Output dataset statistics
    print("Total samples: ", len(x))
    print("Training shape: ", x_train.shape, y_train.shape)
    print("Testing shape: ", x_test.shape, y_test.shape)
    
    # Init model hyperparameters
    input_size = 3
    output_size = 1
    hidden_size = 32
    num_layers = 1
    epochs = 10
    batch_size = 100000 # be mindful of RAM allocation
    learning_rate = 1e-3
    model = TrafficModel(output_size, input_size, hidden_size, num_layers)
    loss = torch.nn.MSELoss()
    optimiser = torch.optim.Adam(model.parameters(), lr=learning_rate)
    
    # Train
    new_model_name = "model-10.pt"
    
    TRAIN = True
    if TRAIN:
        for epoch in range(epochs):
            train(epoch, batch_size, model, optimiser, loss, x_train, y_train, x_test, y_test)
    
        # Save model
        torch.save(model.state_dict(), f"models/{new_model_name}")
        print("Saved model")
    # else:
    #     model.load_state_dict(torch.load("models/model-1000.pt"))
    #     model.eval()
    #     print("Loaded model")