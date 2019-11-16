# Variables used across scripts

# Modelling variables
IND_VAR = 'harm'
DEP_VARS = ['Weather', 'Congestion', 'age', 'time_since_last_training']


# Incident variables
HARM_COSTS = {'Death':100, 'Major Incident':10, 'Minor Incident':1}
OVERALL_RATES = {'Death':0.0001, 'Major Incident':0.001, 'Minor Incident':0.02}
ENVIRONMENT_IMPACT = {'Weather':5, 'Congestion':3}

