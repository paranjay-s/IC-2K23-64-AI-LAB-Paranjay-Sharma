from collections import deque

# ==========================================
# CONFIGURABLE TEST CASES (Change these lines!)
# ==========================================
TOTAL_M = 3         # Total Missionaries
TOTAL_C = 3         # Total Cannibals
BOAT_CAPACITY = 2   # Max people the boat can hold

def is_valid(m_left, c_left):
    """Checks if a state is safe according to the rules."""
    # 1. Check if numbers are within valid bounds
    if m_left < 0 or m_left > TOTAL_M or c_left < 0 or c_left > TOTAL_C:
        return False
    
    # 2. Check left bank safety: If missionaries > 0, cannibals cannot outnumber them
    if m_left > 0 and m_left < c_left:
        return False
    
    # 3. Check right bank safety: Remaining people on the right
    m_right = TOTAL_M - m_left
    c_right = TOTAL_C - c_left
    if m_right > 0 and m_right < c_right:
        return False
        
    return True

def solve_missionaries_and_cannibals():
    """Solves the problem using BFS and returns the path of steps."""
    # Queue stores: (m_left, c_left, boat_position, path_history)
    # boat_position: 1 = Left bank, 0 = Right bank
    queue = deque([(TOTAL_M, TOTAL_C, 1, [])])
    visited = set([(TOTAL_M, TOTAL_C, 1)])
    
    # Generate all possible valid boat moves (combinations of missionaries and cannibals)
    possible_moves = []
    for m in range(BOAT_CAPACITY + 1):
        for c in range(BOAT_CAPACITY + 1):
            if 1 <= m + c <= BOAT_CAPACITY:
                possible_moves.append((m, c))
                
    while queue:
        m_left, c_left, boat, path = queue.popleft()
        
        # Check if we reached the goal state (Everyone on right, boat on right)
        if m_left == 0 and c_left == 0 and boat == 0:
            return path + [(m_left, c_left, boat)]
            
        # Try all possible boat moves
        for m_move, c_move in possible_moves:
            if boat == 1:
                # Boat is moving from Left to Right
                next_m = m_left - m_move
                next_c = c_left - c_move
                next_boat = 0
                action = f"Move {m_move} Missionary(es) and {c_move} Cannibal(s) Left -> Right"
            else:
                # Boat is moving from Right to Left
                next_m = m_left + m_move
                next_c = c_left + c_move
                next_boat = 1
                action = f"Move {m_move} Missionary(es) and {c_move} Cannibal(s) Right -> Left"
                
            # If the resulting state is safe and hasn't been visited, explore it
            if is_valid(next_m, next_c) and (next_m, next_c, next_boat) not in visited:
                visited.add((next_m, next_c, next_boat))
                queue.append((next_m, next_c, next_boat, path + [(m_left, c_left, boat, action)]))
                
    return None

# ==========================================
# Execution
# ==========================================
if __name__ == "__main__":
    print(f"--- Solving for {TOTAL_M} Missionaries, {TOTAL_C} Cannibals (Boat Capacity: {BOAT_CAPACITY}) ---\n")
    
    solution = solve_missionaries_and_cannibals()
    
    if solution:
        print(f"Solution found in {len(solution) - 1} steps!\n")
        for step_num, step_info in enumerate(solution):
            if len(step_info) == 4:
                m, c, boat, action = step_info
                side = "Left" if boat == 1 else "Right"
                print(f"Step {step_num}: {action}")
                print(f"   -> Left Bank status: {m} Missionaries, {c} Cannibals. (Boat is on {side})\n")
            else:
                print(f"Goal Reached! Everyone is safely across.")
    else:
        print("No solution exists for these parameters.")
