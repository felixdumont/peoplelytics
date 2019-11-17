import numpy as np
import settings


def mock_incidents(df):
    overall_rates = settings.OVERALL_RATES
    env_rates = settings.ENVIRONMENT_IMPACT
    death_risk = 1 + df['driver_death_add_risk'] + df['truck_death_add_risk'] + df['route_risk']
    major_risk = 1 + df['driver_major_add_risk'] + df['truck_major_add_risk'] + df['route_risk']
    minor_risk = 1 + df['driver_minor_add_risk'] + df['truck_minor_add_risk'] + df['route_risk']

    for env_var, env_rate in env_rates.items():
        for risk in [death_risk, major_risk, minor_risk]:
            if env_var in df.columns:
                risk = risk + df[env_var]*env_rate

    death_risk_adj = death_risk / np.mean(death_risk) * overall_rates['Death']
    major_risk_adj = major_risk / np.mean(major_risk) * overall_rates['Major Incident']
    minor_risk_adj = minor_risk / np.mean(minor_risk) * overall_rates['Minor Incident']

    df['Death'] = np.random.rand(len(df)) < death_risk_adj
    df['Major Incident'] = np.random.rand(len(df)) < major_risk_adj
    df['Minor Incident'] = np.random.rand(len(df)) < minor_risk_adj
    return df