import settings
import numpy as np

def add_alerts(df, threshold=settings.THRESHOLD):
    df['alert'] = (df['predictions'] > threshold)
    df['priority'] = np.where(df['predictions'] > threshold, "High",
                              np.where(df['predictions'] > threshold/2, "Medium", "Low"))
    return df