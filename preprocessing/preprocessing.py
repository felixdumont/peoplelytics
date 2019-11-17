import pandas as pd

from preprocessing.load_data import load_drivers, load_route_data, load_route_types, load_trucks\
    , load_future_routes, load_weather
from preprocessing.harm import get_route_harm
from preprocessing.incidents import mock_incidents


def generate_data(train=True):
    """
    Generate datasets for training and predictions. Set train to True if this is the labelled training dataset,
    and to False if this is for future predictions
    :param train:
    :return:
    """
    drivers = load_drivers()
    trucks = load_trucks()
    route_types = load_route_types()
    weather = load_weather()
    if train:
        route_data = load_route_data()
    else:
        route_data = load_future_routes()
    full_df = pd.merge(route_data, drivers, how='inner', on='driver_id')
    full_df = pd.merge(full_df, trucks, how='inner', on='truck_id')
    full_df = pd.merge(full_df, weather, how='inner', on='day')
    full_df = pd.merge(full_df, route_types, how='inner', on='route_id')

    # Generate incidents
    if train:
        full_df = mock_incidents(full_df)
        # Assign weight
        full_df['harm'] = full_df.apply(lambda row: get_route_harm(row), axis=1)

    return full_df
