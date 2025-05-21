# SPDX-FileCopyrightText: 2025 Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>
#
# SPDX-License-Identifier: MPL-2.0

from power_grid_model_ds import PowerGridModelInterface

def check_for_capacity_issues(grid: Grid) -> LineArray:
    """Check for capacity issues on the grid.
    Return the lines that with capacity issues.
    """
    pgm_interface = PowerGridModelInterface(grid)
    pgm_interface.calculate_power_flow()
    pgm_interface.update_grid()

    return grid.line[grid.line.is_overloaded]

print(check_for_capacity_issues(grid))
