import numpy as np

from preprocessing.preprocessing import generate_data
import settings
from alert import add_alerts

def predict(model, scalerX, scalery, log_ind=False, input_df=None):
    if input_df is None:
        df = generate_data(train=False)
    else:
        df = input_df
        
    x_cols = settings.DEP_VARS

    X = df[x_cols]
    X_scaled = scalerX.transform(X)

    predictions = scalery.inverse_transform(model.predict(X_scaled))
    if log_ind:
        predictions = np.exp(predictions)-1
    df['predictions'] = predictions

    df['alert'] = add_alerts(df)
    return df