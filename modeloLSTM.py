import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Supondo que você tenha um DataFrame `data` com as colunas 'date' e 'quantity'
data = pd.read_csv('stock_data.csv')

# Pré-processamento de dados
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)
data = data.resample('D').sum().fillna(0)  # Resample para dias e preenche valores ausentes

# Normalização dos dados
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

# Preparação dos dados para o modelo LSTM
def create_dataset(data, time_step=1):
    X, Y = [], []
    for i in range(len(data) - time_step - 1):
        a = data[i:(i + time_step), 0]
        X.append(a)
        Y.append(data[i + time_step, 0])
    return np.array(X), np.array(Y)

time_step = 10
X, Y = create_dataset(data_scaled, time_step)
X = X.reshape(X.shape[0], X.shape[1], 1)

# Construção do modelo LSTM
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(time_step, 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Treinamento do modelo
model.fit(X, Y, epochs=100, batch_size=32, validation_split=0.2)

# Previsão
train_predict = model.predict(X)
train_predict = scaler.inverse_transform(train_predict)

# Avaliação do modelo
from sklearn.metrics import mean_squared_error
import math
print("MSE:", math.sqrt(mean_squared_error(Y, train_predict)))
