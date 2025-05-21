# SPDX-FileCopyrightText: 2025 Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>
#
# SPDX-License-Identifier: MPL-2.0

def find_connection_point(route: NodeArray, new_substation: NodeArray) -> NodeArray:
    """Calculate the connection point for the new route.
    This should be the geographically closest node to the new substation.
    """
    x_difference = route.x - new_substation.x
    y_difference = route.y - new_substation.y
    distances = (x_difference**2 + y_difference**2) ** 0.5
    
    idx_closest_node = np.argmin(distances)
    closest_node = route[idx_closest_node]
    return closest_node