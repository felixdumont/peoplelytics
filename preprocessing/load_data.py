import pandas as pd
import settings

def load_drivers():
    df = pd.read_csv('data/drivers.csv')
    return df

def load_trucks():
    df = pd.read_csv('data/trucks.csv')
    return df

def load_route_types():
    df = pd.read_csv('data/routes.csv')
    for i in range(1, 6):
        df['route_{}'.format(i)] = (df['route_id'] == i).astype(int)
    return df

def load_weather():
    df = pd.read_csv('data/weather.csv')
    df['snow'] = df['Weather'].str.lower().str.contains('snow').astype(int)
    df['rain'] = df['Weather'].str.lower().str.contains('rain').astype(int)
    return df

def load_route_data():
    df = pd.read_csv('data/routes_data.csv')
    return df

def load_incident_weights():
    pass

def load_future_routes():
    pass