import numpy as np
import pandas as pd
import tensorflow as tf
import os
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import joblib
import math

# Diretório dos dados (teste):
data_dir = '/kaggle/input'

# Carrega todos os .csv encontrados no diretório:
data = pd.DataFrame()
for dirname, _, filenames in os.walk(data_dir):
    for filename in filenames:
        if filename.endswith('.csv'):
            file_path = os.path.join(dirname, filename)
            df = pd.read_csv(file_path)
            data = pd.concat([data, df], ignore_index=True)

# Caso 'data' contenha as colunas 'date' e 'quantity', temos:
if 'date' in data.columns and 'quantity' in data.columns:
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)
    data = data.resample('D').sum().fillna(0)

    # Escalando os dados
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(data['quantity'].values.reshape(-1, 1))

    # Preparação dos dados para o modelo LSTM:
    def dataset_creator(data, time_step=1):
        X, Y = [], []
        for i in range(len(data) - time_step - 1):
            a = data[i:(i + time_step), 0]
            X.append(a)
            Y.append(data[i + time_step, 0])
        return np.array(X), np.array(Y)

    time_step = 10
    X, Y = dataset_creator(data_scaled, time_step)
    X = X.reshape(X.shape[0], X.shape[1], 1)

    # Construção do modelo LSTM
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(time_step, 1)),
        LSTM(50),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, Y, epochs=100, batch_size=32, validation_split=0.2)

    # Previsão e avaliação do modelo:
    train_predict = model.predict(X)
    train_predict = scaler.inverse_transform(train_predict)
    print('Erro quadrático médio: ', math.sqrt(np.mean((Y - train_predict[:, 0]) ** 2)))

    # Salvando o modelo e o scaler:
    model.save('modelo_lstm.h5')
    joblib.dump(scaler, 'scaler.pkl')
else:
    print("As colunas 'date' e 'quantity' não foram encontradas no conjunto de dados.")

