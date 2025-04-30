# Create a source at node 101
source = SourceArray(
    id=[501],
    node=[101],
    status=[1],
    u_ref=[0.0]   # reference voltage or angle (0.0 as a placeholder)
)
grid.append(source, check_max_id=False)