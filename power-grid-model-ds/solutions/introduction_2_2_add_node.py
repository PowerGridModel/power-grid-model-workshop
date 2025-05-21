# Create another node
load_node = MyNodeArray(
    id=[102],
    u_rated=[10500.0],
    node_type=[NodeType.UNSPECIFIED.value]
)
grid.append(load_node, check_max_id=False)