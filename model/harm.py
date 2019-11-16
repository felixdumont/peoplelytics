import pandas as pd

def get_route_harm(df_row, harm_costs={}):
    """
    Given a row of a dataframe containing all of the harm events (e.g. death), search for all the columns present in the
    harm costs dictionary, and apply their associated value as a cost.
    :param df_row: Single row of a dataframe containing all the necessary columns
    :param harm_costs: Dictionary where each key is an incident (e.g. death), and each value is the associated cost
    :return: A number containing the calculated cost
    """
    cols = set(harm_costs.keys())
    missing_cols = cols.difference(set(df_row.index))

    if missing_cols is not None:
        return None # Missing columns!
    else:
        cost = sum([df_row[incident] * value for incident, value in harm_costs.items()])
        return cost


# Testing
harm_costs = {'death':10, 'minor':2, 'major':3}
data = [[0,1,2,3],[0,1,2,2],[0,3,4,6]]
df = pd.DataFrame(data=data, columns=['test','death', 'minoar', 'major'])

print(get_route_harm(df.iloc[0,:],harm_costs))
