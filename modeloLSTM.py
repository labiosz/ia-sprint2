import numpy as np
import pandas as pd
import tensorflow as tf
import os
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

#Diretório dos dados (teste):
data_dir = ('/kaggle/input')

#Carrega todos os .csv encotrados no diretório:
data = pd.DataFrame()
for dirname, _, filenames in os.walk(data_dir):
    for filename in filenames:
        if filename.endswith('.csv'):
            file_path = os.path.join(dirname, filename)
            df = pd.read_csv(file_path)
            data = pd.concat([data, df], ignore_index=True)

#Caso 'data' contenha as colunas 'date' e 'quantity', temos:
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)
data = data.resample('D').sum().fillna(0)

#Preparação dos dados para o modelo LSTM:
def dataset_creator(data, time_step=1):
    X, Y = [], []
    for i in range(len(data) - time_step - 1):
        a = data[i:(i+time_step), 0]
        X.append(a)
        Y.append(data[i+time_step])
    return np.array(X), np.array(Y)

time_step = 10
X, Y = criar_dataset(data_scaled, time_step)
X = X.reshape(X.shape[0], X.shape[1], 1)

#Construção do modelo LSTM
modelo = Sequential([
    LSTM(50), return_sequences=True, input_shape=(time_step, 1), LSTM(50), Dense(1)])
modelo.compile(optimizer='adam', loss='erro_quadrático_medio')
modelo.fit(X,Y, epochs=100, batch_size=32, validation_split=0.2)

#Previsão e avaliação do modelo:
train_predict = modelo.predict(X)
train_predict = scaler.inverse_transform(train_predict)
print('Erro quadrático médio: ', math_sqrt(erro_quadratico_medio(Y, train_predict)))

#Salvando o modelo e o scaler:
modelo.save('modelo_lstm.h5')
joblib.dump(scaler,'scaler.pkl')


