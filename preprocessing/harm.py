import settings

def get_route_harm(df_row, harm_costs=settings.HARM_COSTS):
    """
    Given a row of a dataframe containing all of the harm events (e.g. death), search for all the columns present in the
    harm costs dictionary, and apply their associated value as a cost.
    :param df_row: Single row of a dataframe containing all the necessary columns
    :param harm_costs: Dictionary where each key is an incident (e.g. death), and each value is the associated cost
    :return: A number containing the calculated cost
    """
    cols = set(harm_costs.keys())
    missing_cols = cols.difference(set(df_row.index))
    if missing_cols:
        return None # Missing columns!
    else:
        cost = sum([df_row[incident] * value for incident, value in harm_costs.items()])
        return cost