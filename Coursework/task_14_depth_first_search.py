"""
Task 14: Depth First Search (DFS) Implementation
AI Lab Coursework - Uninformed State-Space Search

AI Concept:
    Depth First Search (DFS) is an uninformed search algorithm that explores
    as deep as possible along each branch before backtracking. It uses a LIFO
    (stack) data structure, either explicitly or via call-stack recursion.

Description:
    Implements DFS traversal (recursive and iterative) and DFS goal-path finding
    with visited tracking to prevent infinite loops in cyclic graphs.
"""

from typing import Dict, List, Optional, Set


# Sample AI State-Space Graph
SAMPLE_GRAPH: Dict[str, List[str]] = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["F"],
    "F": [],
    "G": ["H"],
    "H": [],
}


def dfs_recursive(graph: Dict[str, List[str]], start_node: str, visited: Optional[Set[str]] = None) -> List[str]:
    """Traverses the graph using recursive Depth First Search."""
    if visited is None:
        visited = set()

    traversal_order = [start_node]
    visited.add(start_node)

    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            traversal_order.extend(dfs_recursive(graph, neighbor, visited))

    return traversal_order


def dfs_iterative(graph: Dict[str, List[str]], start_node: str) -> List[str]:
    """Traverses the graph using an explicit LIFO Stack."""
    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            traversal_order.append(current)
            # Push neighbors in reverse order to maintain left-to-right exploration
            for neighbor in reversed(graph.get(current, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order


def dfs_find_path(
    graph: Dict[str, List[str]],
    start: str,
    goal: str,
    visited: Optional[Set[str]] = None
) -> Optional[List[str]]:
    """
    Finds a path from start to goal node using DFS.
    Returns list of nodes representing the path, or None if unreachable.
    """
    if visited is None:
        visited = set()

    visited.add(start)

    if start == goal:
        return [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dfs_find_path(graph, neighbor, goal, visited)
            if path is not None:
                return [start] + path

    return None


def main():
    print("=" * 60)
    print("Task 14: Depth First Search (DFS)")
    print("=" * 60)

    print("Graph Adjacency Structure:")
    for node, neighbors in SAMPLE_GRAPH.items():
        print(f"  {node} -> {neighbors}")

    start_node = "A"
    rec_order = dfs_recursive(SAMPLE_GRAPH, start_node)
    iter_order = dfs_iterative(SAMPLE_GRAPH, start_node)

    print(f"\nDFS Traversal from '{start_node}':")
    print(f"  Recursive Order : {' -> '.join(rec_order)}")
    print(f"  Iterative Order : {' -> '.join(iter_order)}")

    # Path finding test
    start, goal = "A", "H"
    found_path = dfs_find_path(SAMPLE_GRAPH, start, goal)
    print(f"\nFinding Path from '{start}' to '{goal}':")
    if found_path:
        print(f"  Goal found! Path: {' -> '.join(found_path)}")
    else:
        print("  No path exists.")


if __name__ == "__main__":
    main()
