from collections import deque
from simulation_classes.elements.game_map import Map
from typing import Tuple


def bfs_find_path(
    game_map: "Map", start_position: Tuple[int, int], target_position: Tuple[int, int]
):
    queue = deque([start_position])
    visited = {start_position}
    came_from = {start_position: None}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        current_position = queue.popleft()
        if current_position == target_position:
            path = []
            while current_position is not None:
                path.append(current_position)
                current_position = came_from[current_position]
            return path[::-1]
        for x, y in directions:
            neighbor_x = current_position[0] + x
            neighbor_y = current_position[1] + y
            neighbor_position = (neighbor_x, neighbor_y)
            if game_map.is_within_bounds(neighbor_position):
                if neighbor_position not in visited:
                    if (
                        game_map.is_empty(neighbor_position)
                        or neighbor_position == target_position
                    ):
                        queue.append(neighbor_position)
                        visited.add(neighbor_position)
                        came_from[neighbor_position] = current_position

    return []
