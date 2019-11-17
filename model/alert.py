import settings

def add_alerts(df, threshold=settings.THRESHOLD):
    return (df['predictions'] > threshold)
