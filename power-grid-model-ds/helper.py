# SPDX-FileCopyrightText: 2025 Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>
#
# SPDX-License-Identifier: MPL-2.0

import pandas as pd
from power_grid_model_ds.arrays import SymLoadArray, SourceArray

def load_dummy_grid(grid_class):
    nodes_csv = pd.read_csv("data/nodes.csv")
    loads_csv = pd.read_csv("data/loads.csv")
    lines_csv = pd.read_csv("data/lines.csv")

    grid = grid_class.empty()

    nodes = grid.node.__class__(
        id=nodes_csv.id.tolist(),
        u_rated=nodes_csv.u_rated.tolist(),
        node_type=nodes_csv.node_type.tolist(),
        x=nodes_csv.x.tolist(),
        y=nodes_csv.y.tolist(),
        u=[-1.0] * len(nodes_csv),
    )
    loads = SymLoadArray(
        id=loads_csv.id.tolist(),
        node=loads_csv.node.tolist(),
        status=[1] * len(loads_csv),
        type=[0] * len(loads_csv),
        p_specified=loads_csv.p_specified.tolist(),
        q_specified=loads_csv.q_specified.tolist(),
    )
    lines = grid.line.__class__(
        id=lines_csv.id.tolist(),
        from_node=lines_csv.from_node.tolist(),
        to_node=lines_csv.to_node.tolist(),
        from_status=lines_csv.from_status.tolist(),     # 1 means active connection from-side, 
        to_status=lines_csv.to_status.tolist(),         # 1 means active connection to-side
        i_n=lines_csv.i_n.tolist(),                     # line max current capacity (e.g., 200 A)
        r1=lines_csv.r1.tolist(),                       # line resistance
        x1=lines_csv.x1.tolist(),                       # line reactance
        c1=lines_csv.c1.tolist(),                       # line capacitance
        tan1=lines_csv.tan1.tolist()                    # line loss tangent
    )
    sources = SourceArray(
        id=[401],
        node=[101],
        status=[1],
        u_ref=[1.0],
    )

    grid.append(nodes, check_max_id=False)
    grid.append(loads, check_max_id=False)
    grid.append(lines, check_max_id=False)
    grid.append(sources, check_max_id=False)

    grid.set_feeder_ids()

    return grid