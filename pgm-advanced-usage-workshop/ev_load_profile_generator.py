
# EV load profile generator
import numpy as np


def generate_ev_load_profiles(n_load_nodes: int, n_timesteps: int, n_vehicles: int = 1000,
                             avg_kwh_per_vehicle: float = 50.0, charging_power_kw: float = 7.0,
                             arrival_window: tuple = (18, 23), seed: int | None = None):
    """Generate synthetic EV charging load profiles.
    Parameters:
    - n_load_nodes: number of load nodes (distribution of vehicles across nodes)
    - n_timesteps: number of time steps to generate (e.g., hours)
    - n_vehicles: total number of vehicles in the fleet
    - avg_kwh_per_vehicle: average energy required per vehicle during the charging event
    - charging_power_kw: charging power per vehicle (kW) -> used to spread charging over timesteps
    - arrival_window: tuple (start_hour, end_hour) where most arrivals occur (inclusive start, exclusive end)
    - seed: random seed for reproducibility
    Returns a numpy array of shape (n_timesteps, n_load_nodes) representing kW loads per node.
    The model: randomly distribute vehicles across nodes, sample arrival times (hour of day) within window,
    sample dwell/charging duration from a simple distribution, and accumulate charging power into timesteps.
    """
    import numpy as _np
    if seed is not None:
        _np.random.seed(seed)

    # Distribute vehicles to nodes (multinomial)
    p = _np.ones(n_load_nodes) / n_load_nodes
    vehicles_per_node = _np.random.multinomial(n_vehicles, p)

    # Prepare output array in kW (timesteps x nodes)
    profile = _np.zeros((n_timesteps, n_load_nodes), dtype=float)

    # For each node, generate arrival times and durations
    for node_idx in range(n_load_nodes):
        nv = vehicles_per_node[node_idx]
        if nv == 0:
            continue

        # arrivals: sample hours within arrival_window, but allow spread across whole timeseries days
        # compute number of days covered by timesteps (assume hourly)
        steps_per_day = 24
        n_days = int(_np.ceil(n_timesteps / steps_per_day))

        # sample vehicle arrival day and hour for each vehicle
        arrival_days = _np.random.randint(0, n_days, size=nv)
        arrival_hours = _np.random.randint(arrival_window[0], arrival_window[1], size=nv)
        arrival_steps = arrival_days * steps_per_day + arrival_hours

        # sample required kWh per vehicle around avg (lognormal-ish to avoid negatives)
        kwh = _np.random.normal(loc=avg_kwh_per_vehicle, scale=avg_kwh_per_vehicle * 0.25, size=nv)
        kwh = _np.clip(kwh, 1.0, None)

        # compute charging duration in hours (kwh / charging_power) and convert to integer timesteps
        duration_hours = _np.ceil(kwh / charging_power_kw).astype(int)

        # accumulate charging power into profile (simple rectangular charging)
        for a_step, dur in zip(arrival_steps, duration_hours):
            if a_step >= n_timesteps:
                continue
            end = min(n_timesteps, a_step + dur)
            profile[a_step:end, node_idx] += charging_power_kw

    return profile

n_profiles = 10

n_timesteps = 24 * 365  # one year of hourly data
ev_profile = generate_ev_load_profiles(n_load_nodes=n_profiles, n_timesteps=n_timesteps, n_vehicles=5000,
                                       avg_kwh_per_vehicle=40.0, charging_power_kw=7.0,
                                       arrival_window=(17, 22), seed=42)


print('Generated EV profiles:')
print('  ev_profile shape (timesteps, nodes):', ev_profile.shape)

np.savetxt("data/ev_profile.csv", ev_profile, delimiter=",")

