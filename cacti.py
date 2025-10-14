# cacti.py
from typing import List


def cacti_number(plot: List[List[int]]) -> int:
    # validation
    if not isinstance(plot, list) or not plot or not all(isinstance(r, list) for r in plot):
        raise TypeError("Input must be a non-empty 2D list")
    rows = len(plot)
    cols = len(plot[0])
    if cols == 0 or any(len(r) != cols for r in plot):
        raise ValueError("Grid must be rectangular (all rows same length)")
    for r in plot:
        for v in r:
            if v not in (0, 1):
                raise ValueError("Grid values must be 0 or 1")

    # helper to check surrounding area
    def has_adjacent_one(i: int, j: int) -> bool:
        if i > 0 and plot[i - 1][j] == 1:
            return True
        if i + 1 < rows and plot[i + 1][j] == 1:
            return True
        if j > 0 and plot[i][j - 1] == 1:
            return True
        if j + 1 < cols and plot[i][j + 1] == 1:
            return True
        return False

    # sanity: the given plot should already obey the rule
    for i in range(rows):
        for j in range(cols):
            if plot[i][j] == 1 and has_adjacent_one(i, j):
                raise ValueError("Input grid already has adjacent cacti")

    # count how many safe empty cells exist on each checkerboard color
    count_color = [0, 0]  # index 0 -> (i+j)%2 == 0, index 1 -> 1
    for i in range(rows):
        for j in range(cols):
            if plot[i][j] == 0 and not has_adjacent_one(i, j):
                color = (i + j) & 1
                count_color[color] += 1

    # choose the better color; same-color placements never touch orthogonally
    return max(count_color[0], count_color[1])
