r"""
=============================================================================
EMERGENCY EVACUATION PLANNER (PYTHON EQUIVALENT & SIMULATION)
Lab Test 2 - Set 3 (Roll No: 64, Student: Paranjay Sharma)
Course: MCA 7th Sem - Artificial Intelligence Laboratory

Problem Statement:
    During an emergency such as a fire, people inside a building need to reach
    a safe exit. Some corridors may be blocked or unsafe. Develop a system that
    represents rooms and corridors as a connected network and finds a route
    from a given starting location to an available exit.

Prolog Logic Equivalence:
    - Facts: connection(From, To, Risk), is_exit(Node).
    - Dynamic Knowledge: blocked(Node1, Node2), unsafe(Node).
    - Horn Clause Search: find_path(Current, Exit, Visited, Path, TotalRisk).
    - Constraint Handling: \+ is_blocked(A, B), \+ unsafe(B).
=============================================================================
"""

from typing import Dict, List, Optional, Set, Tuple


class EmergencyEvacuationPlanner:
    """
    Simulates the Prolog Knowledge Base, Inference Engine, and Constraint
    Satisfaction Search for building evacuation during a fire emergency.
    """

    def __init__(self):
        # Static Knowledge Base (Building Layout)
        self.locations: Dict[str, str] = {
            "room_a": "Room A (Office 101)",
            "room_b": "Room B (Conference Hall)",
            "room_c": "Room C (Computer Lab)",
            "corridor_1": "Main Central Corridor",
            "corridor_2": "North Wing Corridor",
            "corridor_3": "South Wing Corridor",
            "staircase_1": "Staircase 1 (East Fire Escape)",
            "staircase_2": "Staircase 2 (West Central Stairs)",
            "exit_1": "Exit 1 (Ground East Fire Door)",
            "exit_2": "Exit 2 (Ground Main Entrance)",
            "exit_3": "Exit 3 (North Emergency Gate)",
        }

        self.exits: Set[str] = {"exit_1", "exit_2", "exit_3"}

        # Graph Connections with Risk Weights: (NodeA, NodeB) -> Risk Factor
        # 1 = Normal/Clear, 2 = Light Smoke, 4 = High Heat/Hazard
        self.connections: List[Tuple[str, str, int]] = [
            ("room_a", "corridor_1", 1),
            ("corridor_1", "staircase_1", 2),
            ("corridor_1", "room_b", 1),
            ("room_b", "exit_2", 1),
            ("staircase_1", "exit_1", 1),
            # Bypass & Alternate routes
            ("room_a", "corridor_2", 2),
            ("corridor_2", "room_c", 1),
            ("room_c", "staircase_2", 1),
            ("staircase_2", "exit_3", 1),
            ("room_b", "corridor_3", 1),
            ("corridor_3", "staircase_1", 2),
            ("corridor_3", "exit_2", 2),
        ]

        # Dynamic Knowledge Base (Hazards asserted at runtime)
        self.blocked_connections: Set[Tuple[str, str]] = set()
        self.unsafe_locations: Set[str] = set()

    # --- Knowledge Base Modifiers (Simulating Prolog assertz / retractall) ---

    def reset_hazards(self):
        """Clears all dynamic hazard assertions (retractall equivalent)."""
        self.blocked_connections.clear()
        self.unsafe_locations.clear()

    def block_connection(self, node_a: str, node_b: str):
        """Marks a bidirectional connection as impassable/blocked."""
        self.blocked_connections.add((node_a, node_b))
        self.blocked_connections.add((node_b, node_a))

    def mark_unsafe(self, location: str):
        """Marks a room or corridor as unsafe (e.g. fire/smoke engulfed)."""
        self.unsafe_locations.add(location)

    # --- Prolog-Style Predicate Checking ---

    def is_blocked(self, u: str, v: str) -> bool:
        """Prolog rule: is_blocked(X, Y) :- blocked(X, Y); blocked(Y, X)."""
        return (u, v) in self.blocked_connections

    def is_safe_transition(self, u: str, v: str) -> bool:
        """
        Prolog rule:
        safe_transition(From, To) :-
            adjacent(From, To),
            \\+ is_blocked(From, To),
            \\+ unsafe(To).
        """
        if self.is_blocked(u, v):
            return False
        if v in self.unsafe_locations:
            return False
        return True

    def get_neighbors(self, node: str) -> List[Tuple[str, int]]:
        """Finds all connected adjacent nodes and their risk weights."""
        neighbors = []
        for u, v, cost in self.connections:
            if u == node:
                neighbors.append((v, cost))
            elif v == node:
                neighbors.append((u, cost))
        return neighbors

    # --- Path Search Algorithm (Prolog Backtracking & Depth First Search) ---

    def find_all_routes(
        self,
        current: str,
        visited: List[str],
        current_risk: int
    ) -> List[Tuple[int, List[str], str]]:
        """
        Pure recursive DFS mirroring Prolog's backtracking search:
        find_path(Current, Exit, Visited, [Current|Tail], TotalRisk).
        Returns a list of tuples: (TotalRisk, PathList, DestinationExit).
        """
        # Base case: Reached an exit node
        if current in self.exits:
            return [(current_risk, visited, current)]

        routes = []
        for neighbor, edge_risk in self.get_neighbors(current):
            # Constraint check: safe transition and not in visited accumulator
            if self.is_safe_transition(current, neighbor) and neighbor not in visited:
                sub_routes = self.find_all_routes(
                    neighbor,
                    visited + [neighbor],
                    current_risk + edge_risk
                )
                routes.extend(sub_routes)

        return routes

    def evacuate(self, start: str, prefer_lowest_risk: bool = True) -> Optional[Tuple[int, List[str], str]]:
        """
        Finds the best evacuation path from start location to an available exit.
        If prefer_lowest_risk is True, sorts by cumulative risk score.
        """
        if start in self.unsafe_locations:
            return None

        routes = self.find_all_routes(start, [start], 0)
        if not routes:
            return None

        if prefer_lowest_risk:
            # Sort by total risk, then by number of hops
            routes.sort(key=lambda r: (r[0], len(r[1])))
        return routes[0]

    # --- Formatted Output and Visualization ---

    def display_evacuation_result(self, start: str):
        """Displays formatted output matching the examination specification."""
        result = self.evacuate(start)
        print("=" * 60)
        print("            EMERGENCY EVACUATION PLANNER             ")
        print("=" * 60)
        print(f"Starting Location : {start} ({self.locations.get(start, 'Unknown')})")

        if result is None:
            print("Status            : NO SAFE ROUTE AVAILABLE!")
            print("Alert             : All exit corridors/routes are blocked or unsafe.")
            print("Recommended Action: Shelter in place, seal doors, and await rescue.")
            print("=" * 60)
            return

        total_risk, path, destination = result
        path_str = " -> ".join(path)
        hops = len(path) - 1

        print("Route Found       :")
        print(f"  {path_str}")
        print(f"Destination Exit  : {destination} ({self.locations.get(destination, '')})")
        print(f"Total Transitions : {hops} hops")
        print(f"Cumulative Risk   : {total_risk} (Lower is safer)")
        print("Status            : Route found (Safe to proceed).")
        print("=" * 60)


def print_building_network():
    """Prints ASCII representation of the building's emergency layout."""
    print("""
+-----------------------------------------------------------------+
|                    BUILDING NETWORK TOPOLOGY                    |
+-----------------------------------------------------------------+
|                                                                 |
|   [Room C] <=======> [Corridor 2] <=======> [Room A] (Start)    |
|      |                                         |                |
|      v (Stairs 2)                              v (Risk 1)       |
|  [Exit 3] (North Gate)                    [Corridor 1]          |
|                                            /        \\           |
|                        (Risk 2, Blockable)/          \\ (Risk 1)  |
|                                          v            v         |
|                                   [Staircase 1]   [Room B]      |
|                                          |            |         |
|                                          v            v         |
|                                       [Exit 1]     [Exit 2]     |
|                                    (Ground East) (Main Ground)  |
+-----------------------------------------------------------------+
    """)


def run_test_cases():
    planner = EmergencyEvacuationPlanner()

    print("\n" + "#" * 65)
    print("#  AI LAB TEST 2 - SET 3: EMERGENCY EVACUATION PLANNER")
    print("#  Candidate: Paranjay Sharma | Roll No: 64 | Batch: MCA 7th")
    print("#" * 65)

    print_building_network()

    # -------------------------------------------------------------
    # TEST CASE 1: Syllabus Default Scenario
    # -------------------------------------------------------------
    print("\n" + "-" * 65)
    print(">>> TEST CASE 1: Standard Syllabus Scenario")
    print("Conditions : Start = Room A")
    print("Hazard     : Blocked connection between Corridor 1 and Staircase 1")
    print("-" * 65)
    planner.reset_hazards()
    planner.block_connection("corridor_1", "staircase_1")
    planner.display_evacuation_result("room_a")

    # -------------------------------------------------------------
    # TEST CASE 2: Multi-Hazard & Alternative Route via North Wing
    # -------------------------------------------------------------
    print("\n" + "-" * 65)
    print(">>> TEST CASE 2: Multi-Hazard Routing (Alternative North Wing Exit)")
    print("Conditions : Start = Room A")
    print("Hazards    : Corridor 1 - Staircase 1 is BLOCKED")
    print("             Corridor 1 - Room B is BLOCKED")
    print("Expectation: System backtracks, discovers North Wing -> Exit 3")
    print("-" * 65)
    planner.reset_hazards()
    planner.block_connection("corridor_1", "staircase_1")
    planner.block_connection("corridor_1", "room_b")
    planner.display_evacuation_result("room_a")

    # -------------------------------------------------------------
    # TEST CASE 3: Total Isolation / All Paths Blocked
    # -------------------------------------------------------------
    print("\n" + "-" * 65)
    print(">>> TEST CASE 3: Total Lockdown / Extreme Emergency Scenario")
    print("Conditions : Start = Room A")
    print("Hazards    : Corridor 1 and Corridor 2 are both engulfed in fire")
    print("Expectation: Failsafe logic activates, warns occupant to shelter")
    print("-" * 65)
    planner.reset_hazards()
    planner.mark_unsafe("corridor_1")
    planner.mark_unsafe("corridor_2")
    planner.display_evacuation_result("room_a")


if __name__ == "__main__":
    run_test_cases()
