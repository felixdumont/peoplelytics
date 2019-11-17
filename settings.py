# Variables used across scripts

# Modelling variables
IND_VAR = 'harm'
DEP_VARS = ['snow', 'rain', 'Congestion', 'age', 'time_since_last_training', 'age_truck',
            'truck_5yr_incidents', 'time_since_maintenance', 'school_zone_ct', 'avg_speed']


# Incident variables
HARM_COSTS = {'Death':100, 'Major Incident':10, 'Minor Incident':1}
OVERALL_RATES = {'Death':0.0001, 'Major Incident':0.001, 'Minor Incident':0.02}
ENVIRONMENT_IMPACT = {'snow':5, 'rain':3, 'Congestion':3}

