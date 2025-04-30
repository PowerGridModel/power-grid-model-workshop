# Create a line between node 101 and 102
new_line = MyLineArray(
    id=[201],
    from_node=[101],
    to_node=[102],
    from_status=[1],      # 1 = active from-side, 
    to_status=[1],        # 1 = active to-side (both ends active)
    i_n=[200.0],          # line current capacity (e.g., 200 A)
    r1=[0.1], x1=[0.03],  # line resistance and reactance
    c1=[0.0], tan1=[0.0]  # line capacitance and loss tangent (0 for simplicity)
)
grid.append(new_line, check_max_id=False)