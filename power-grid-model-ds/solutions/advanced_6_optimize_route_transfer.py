def optimize_route_transfer(grid: Grid, connection_point: NodeArray, new_substation: NodeArray) -> None:
    """Attempt to optimize the route transfer moving the naturally open point (NOP) upstream towards the old substation.
    This way, the new substation will take over more nodes of the original route.
    """
    old_substation_node_id = connection_point.feeder_node_id.item()
    path, _ = grid.graphs.active_graph.get_shortest_path(connection_point.id.item(), old_substation_node_id)
    print("Path from overload to old substation:", path)

    current_branch = grid.line.filter(
        from_node=[connection_point.id, new_substation.id],
        to_node=[connection_point.id, new_substation.id]
    )
    for from_node, to_node in zip(path[0:-1], path[1:]):
        # Check if the route is still overloaded
        capacity_issues = check_for_capacity_issues(grid)
        route_capacity_issues = capacity_issues.filter(feeder_branch_id=connection_point.feeder_branch_id)
        if not any(route_capacity_issues):
            break

        grid.make_active(current_branch)
        current_branch = grid.line.filter(from_node=[from_node, to_node], to_node=[from_node, to_node])
        grid.make_inactive(current_branch)
    
    grid.set_feeder_ids()