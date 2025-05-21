# Create a load at node 102
load = SymLoadArray(
    id=[401],
    node=[102],
    type=[1],                # load type (e.g., 1 for constant power load)
    p_specified=[1_000_000.0],  # 1e6 W = 1 MW
    q_specified=[1_000_000.0],  # 1e6 VAR
    status=[1]               # active
)
grid.append(load, check_max_id=False)