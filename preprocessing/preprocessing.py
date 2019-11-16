import pandas as pd

def load_drivers():
    pass

def load_trucks():
    pass

def load_route_types():
    pass

def load_route_data():
    pass

def generate_train_data():
    drivers = load_drivers()
    trucks = load_trucks()
    route_types = load_route_types()
    route_data = load_route_data()

    full_df = pd.merge(route_data, drivers, how='inner', on='driver_id')
    full_df = pd.merge(full_df, trucks, how='inner', on='truck_id')
    full_df = pd.merge(route_data, route_types, how='inner', on='route_id')
    return full_df