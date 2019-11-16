import pandas as pd

from preprocessing.load_data import load_drivers, load_route_data, load_route_types, load_trucks
from preprocessing.harm import get_route_harm
from preprocessing.incidents import mock_incidents

def generate_train_data():
    drivers = load_drivers()
    trucks = load_trucks()
    route_types = load_route_types()
    route_data = load_route_data()

    full_df=route_data
    full_df = pd.merge(route_data, drivers, how='inner', on='driver_id')
    full_df = pd.merge(full_df, trucks, how='inner', on='truck_id')
    #full_df = pd.merge(route_data, route_types, how='inner', on='route_id')

    # Generate incidents
    full_df = mock_incidents(full_df)

    # Assign weight
    full_df['harm'] = full_df.apply(lambda row: get_route_harm(row), axis=1)

    return full_df