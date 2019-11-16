from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
import numpy as np

import settings
from preprocessing.preprocessing import generate_train_data
from model.model import nn_model, xgb_model


def split_datasets(df):
    y_pred = settings.IND_VAR
    x_cols = settings.DEP_VARS
    y = df[y_pred].values
    y_logged = np.log(1 + y)
    X = df[x_cols]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_logged, test_size=0.2, random_state=42)

    scalerX = StandardScaler().fit(X_train)
    scalery = StandardScaler().fit(y_train.reshape(-1, 1))
    X_train_scaled = scalerX.transform(X_train)
    y_train_scaled = scalery.transform(y_train.reshape(-1, 1))
    X_test_scaled = scalerX.transform(X_test)
    y_test_scaled = scalery.transform(y_test.reshape(-1, 1))
    return X_train_scaled, y_train_scaled, X_test_scaled, y_test_scaled, scalerX, scalery, X_test, y_test


def evaluate_grid(grid_result):
    print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.cv_results_['mean_test_score']
    stds = grid_result.cv_results_['std_test_score']
    params = grid_result.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print("%f (%f) with: %r" % (mean, stdev, param))


def train_model(model='NN'):
    df = generate_train_data()
    X_train_scaled, y_train_scaled, X_test_scaled, y_test_scaled, scalerX, scalery, X_test, y_test = split_datasets(df)

    if model == 'NN':
        batch_size = [5, 10]
        epochs = [10, 100]
        num_neurons = [2, 5]
        input_dim = [2]
        param_grid = dict(  # batch_size=batch_size,
            epochs=epochs,
            input_dim=input_dim,
            num_neurons=num_neurons)

        model = KerasRegressor(build_fn=nn_model, verbose=0)
    if model == 'XGB':
        param_grid = dict(learning_rate=[0.01, 0.1],
                          n_estimators=[10, 100])
        model = xgb_model()

    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=3, scoring='neg_mean_squared_error')
    grid_result = grid.fit(X_train_scaled, y_train_scaled)
    evaluate_grid(grid_result)
    return grid, X_train_scaled, y_train_scaled, X_test_scaled, scalery, X_test, y_test


def save_model():
    pass
