# Create a source at node 101
source = SourceArray(
    id=[501],
    node=[101],
    status=[1],
    u_ref=[1.0]
)
grid.append(source, check_max_id=False)