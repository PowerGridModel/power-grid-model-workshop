# SPDX-FileCopyrightText: 2025 Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>
#
# SPDX-License-Identifier: MPL-2.0

def get_all_congested_routes(grid: Grid) -> list[NodeArray]:
    """Get all nodes on routes that contain an overloaded line."""
    grid.set_feeder_ids()
    lines_with_congestion = check_for_capacity_issues(grid)
    feeder_branch_ids_with_congestion = np.unique(lines_with_congestion['feeder_branch_id'])
    return [grid.node.filter(feeder_branch_id=branch_id) for branch_id in feeder_branch_ids_with_congestion]
 
congested_routes = get_all_congested_routes(grid)