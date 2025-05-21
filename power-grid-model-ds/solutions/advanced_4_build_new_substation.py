def build_new_substation(grid: Grid, location: tuple[float, float]) -> NodeArray:
    """Build a new substation at the given location.
    Return the new substation.
    """
    new_substation = MyNodeArray(
        node_type=[NodeType.SUBSTATION_NODE.value],
        u_rated=[10500.0],
        x=[location[0]],
        y=[location[1]]
    )
    grid.append(new_substation)

    new_source = SourceArray(
        node=[new_substation.id.item()],
        status=[1],
        u_ref=[1],
    )
    grid.append(new_source)
    return new_substation

# 🏗️ Add a new substation at (400, 400)
new_substation = build_new_substation(grid, (400, 400))