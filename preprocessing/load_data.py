import pandas as pd


def load_drivers():
    df = pd.read_csv('data/drivers.csv')
    return df

def load_trucks():
    df = pd.read_csv('data/trucks.csv')
    return df

def load_route_types():
    df = pd.read_csv('data/routes.csv')
    return df

def load_weather():
    df = pd.read_csv('data/weather.csv')
    return df

def load_route_data():
    df = pd.read_csv('data/routes_data_2.csv')
    return df

def load_incident_weights():
    pass

def load_future_routes():
    pass