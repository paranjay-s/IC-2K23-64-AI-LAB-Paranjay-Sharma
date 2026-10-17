from collections import deque

def water_jug_problem(capacity_a, capacity_b, target):
    """
    Solves the Water Jug Problem using Breadth-First Search (BFS).
    :param capacity_a: Max capacity of Jug 1
    :param capacity_b: Max capacity of Jug 2
    :param target: Target amount of water to measure
    """
    # Queue stores tuples of (current_a, current_b, path_of_steps)
    queue = deque([(0, 0, [])])
    
    # Set to keep track of visited states to avoid infinite loops
    visited = set()
    visited.add((0, 0))
    
    while queue:
        current_a, current_b, path = queue.popleft()
        
        # Check if we reached the target in either jug
        if current_a == target or current_b == target:
            return path + [(current_a, current_b)]
        
        # List of all possible next states and the action description
        possible_transitions = [
            # 1. Fill Jug A
            (capacity_a, current_b, "Fill Jug A"),
            # 2. Fill Jug B
            (current_a, capacity_b, "Fill Jug B"),
            # 3. Empty Jug A
            (0, current_b, "Empty Jug A"),
            # 4. Empty Jug B
            (current_a, 0, "Empty Jug B"),
            # 5. Pour Jug A -> Jug B
            (
                current_a - min(current_a, capacity_b - current_b),
                current_b + min(current_a, capacity_b - current_b),
                "Pour Jug A -> Jug B"
            ),
            # 6. Pour Jug B -> Jug A
            (
                current_a + min(current_b, capacity_a - current_a),
                current_b - min(current_b, capacity_a - capacity_a), # Fixed minor calc logic below
                "Pour Jug B -> Jug A"
            )
        ]
        
        # Correcting transition 6 pour logic safety
        pour_b_to_a_amount = min(current_b, capacity_a - current_a)
        possible_transitions[5] = (
            current_a + pour_b_to_a_amount,
            current_b - pour_b_to_a_amount,
            "Pour Jug B -> Jug A"
        )

        for next_a, next_b, action in possible_transitions:
            if (next_a, next_b) not in visited:
                visited.add((next_a, next_b))
                queue.append((next_a, next_b, path + [(current_a, current_b, action)]))
                
    return None

# Example Execution
if __name__ == "__main__":
    jug1_cap = 4
    jug2_cap = 3
    target_amount = 2
    
    print(f"Solving for Jugs ({jug1_cap}L, {jug2_cap}L) to get {target_amount}L:\n")
    solution = water_jug_problem(jug1_cap, jug2_cap, target_amount)
    
    if solution:
        print("Steps to reach the goal:")
        for step_num, state_info in enumerate(solution):
            if len(state_info) == 3:
                a, b, action = state_info
                print(f"Step {step_num}: {action} -> Jugs: ({a}, {b})")
            else:
                print(f"Goal Reached! Final State: {state_info}")
    else:
        print("No solution possible for the given capacities and target.")
