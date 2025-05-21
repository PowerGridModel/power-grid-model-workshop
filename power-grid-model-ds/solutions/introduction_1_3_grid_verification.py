# SPDX-FileCopyrightText: 2025 Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>
#
# SPDX-License-Identifier: MPL-2.0

print("Node 'u' field exists?", hasattr(grid.node, "u"))
print("Line 'i_from' field exists?", hasattr(grid.line, "i_from"))
print("Node array:", grid.node)