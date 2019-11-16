from preprocessing import generate_train_data

def train_model():
    train_df = generate_train_data()

    batch_size = [5, 10]
    epochs = [10, 100, 1000]
    num_neurons = [5, 100, 1000]
    param_grid = dict( batch_size=batch_size,
        epochs=epochs,
        num_neurons=num_neurons)



    model = KerasRegressor(build_fn=bm, verbose=0)
    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=3, scoring='neg_mean_squared_error')
    grid_result = grid.fit(X_train_scaled, y_train_scaled)


def save_model():
    pass