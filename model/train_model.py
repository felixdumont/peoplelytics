from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline

import settings
from preprocessing.preprocessing import generate_train_data
from model.model import nn_model

def split_datasets(df):
    y_pred = settings.IND_VAR
    x_cols = settings.DEP_VARS
    y = df[y_pred].values
    X = df[x_cols]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size = 0.2, random_state = 42)

    scalerX = StandardScaler().fit(X_train)
    scalery = StandardScaler().fit(y_train)
    X_train_scaled = scalerX.transform(X_train)
    y_train_scaled = scalery.transform(y_train)
    X_test_scaled = scalerX.transform(X_test)
    y_test_scaled = scalery.transform(y_test)
    return X_train_scaled, y_train_scaled, X_test_scaled, y_test_scaled, scalerX, scalery

def train_model():
    df = generate_train_data()
    X_train_scaled, y_train_scaled, X_test_scaled, y_test_scaled, scalerX, scalery = split_datasets(df)

    batch_size = [5, 10]
    epochs = [10, 100, 1000]
    num_neurons = [5, 100, 1000]
    param_grid = dict(batch_size=batch_size,
                      epochs=epochs,
                      num_neurons=num_neurons)

    model = KerasRegressor(build_fn=nn_model, verbose=0)
    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=3, scoring='neg_mean_squared_error')
    grid_result = grid.fit(X_train_scaled, y_train_scaled)


def save_model():
    pass
