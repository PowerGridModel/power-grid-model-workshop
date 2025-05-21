# SPDX-FileCopyrightText: 2025 Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>
#
# SPDX-License-Identifier: MPL-2.0

# Create a substation node entry
substation_node = MyNodeArray(
    id=[101],
    u_rated=[10500.0],                         # e.g., 10.5 kV base voltage
    node_type=[NodeType.SUBSTATION_NODE.value] # type = 1 (Substation node)
)
# Append this node to the grid
grid.append(substation_node, check_max_id=False)