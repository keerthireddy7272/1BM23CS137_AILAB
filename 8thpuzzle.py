def is_valid(state):
    """Checks if the state is valid (3x3 grid with numbers 0-8)."""
    return len(state) == 9 and sorted(state) == list(range(9))


def get_neighbors(state):
    """Returns a list of valid neighbor states from the given state."""
    neighbors = []
    zero_index = state.index(0)  # Find the blank tile
    row, col = divmod(zero_index, 3)

    # Possible moves: Right, Left, Down, Up
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:  # Check within bounds
            new_zero_index = new_row * 3 + new_col
            new_state = list(state)
            # Swap blank (0) with the target tile
            new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
            neighbors.append(tuple(new_state))  # Store as tuple (immutable)
    return neighbors


def dfs(initial_state, goal_state):
    """Solves the 8-puzzle problem using Depth First Search."""
    stack = [(initial_state, [])]  # Each entry: (current_state, path_to_state)
    visited = set()

    while stack:
        current_state, path = stack.pop()

        # Check if goal reached
        if current_state == goal_state:
            return path + [current_state]

        if current_state not in visited:
            visited.add(current_state)
            for neighbor in get_neighbors(list(current_state)):
                stack.append((neighbor, path + [current_state]))

    return None  # No solution found


def print_state(state):
    """Pretty print a 3x3 puzzle state."""
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print("-" * 5)


# Example Usage
if __name__ == "__main__":
    initial_state = (1, 2, 3,
                     4, 0, 5,
                     6, 7, 8)  # Example start state

    goal_state = (1, 2, 3,
                  4, 5, 6,
                  7, 8, 0)  # Goal state

    if is_valid(initial_state) and is_valid(goal_state):
        solution_path = dfs(initial_state, goal_state)

        if solution_path:
            print("\nSolution found! Steps:")
            for step in solution_path:
                print_state(step)
        else:
            print("No solution found for the given initial and goal states.")
    else:
        print("Invalid initial or goal state.")