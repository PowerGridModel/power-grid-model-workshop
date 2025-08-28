def connect_to_route(grid: Grid, connection_point: NodeArray, new_substation: NodeArray) -> None:
    """Connect the new substation node to the connection point.
    """
    # Create a new line that connects the two nodes
    new_line = MyLineArray(
        from_node=[new_substation.id],
        to_node=[connection_point.id],
        from_status=[0], # status is 0 to make sure the line is not active
        to_status=[1],
        i_n=[360.0],
        r1=[0.05], x1=[0.01], c1=[0.0], tan1=[0.0]
    )
    grid.append(new_line)
