# SPDX-FileCopyrightText: 2025 Contributors to the Power Grid Model project <powergridmodel@lfenergy.org>
#
# SPDX-License-Identifier: MPL-2.0

@dataclass
class ExtendedGrid(Grid):
    node: MyNodeArray
    line: MyLineArray