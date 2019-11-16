import pandas as pd

from preprocessing.harm import get_route_harm

#TODO Formalize as unit tests

# Testing
harm_costs = {'death':10, 'minor':2, 'major':3}
data = [[0,1,2,3],[0,1,2,2],[0,3,4,6]]
df = pd.DataFrame(data=data, columns=['test','death', 'minor', 'major'])

print(get_route_harm(df.iloc[0,:],harm_costs))

harm_costs_2 = {'death':10, 'minor':2, 'major':3, 'other':55}

print(get_route_harm(df.iloc[0,:],harm_costs_2)) # Returns None
