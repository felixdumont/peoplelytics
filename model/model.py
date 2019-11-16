import pandas as pd
from keras.models import Sequential
from keras.layers import Dense


def nn_model(num_neurons, input_dim):
    model = Sequential()
    model.add(Dense(num_neurons, input_dim=input_dim, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # model.summary()
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model