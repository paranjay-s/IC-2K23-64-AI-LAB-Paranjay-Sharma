"""
Task 15: Solve the Traveling Salesman Problem (TSP)
AI Lab Coursework - Heuristic & Combinatorial Search Optimization

Problem Formulation:
    Given a set of cities and pairwise distances, find the shortest Hamiltonian
    cycle that visits each city exactly once and returns to the starting city.

Description:
    Implements:
      1. Exact exhaustive search (Permutations / Brute-Force) to guarantee optimal tour.
      2. Nearest-Neighbor greedy heuristic search to demonstrate AI heuristic approximation.
"""

import itertools
import math
from typing import Dict, List, Tuple


# Sample cities with pairwise symmetric distance matrix (in km)
CITIES = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru"]

DISTANCE_MATRIX = {
    ("Delhi", "Delhi"): 0,
    ("Delhi", "Mumbai"): 1400,
    ("Delhi", "Kolkata"): 1500,
    ("Delhi", "Chennai"): 2180,
    ("Delhi", "Bengaluru"): 2150,

    ("Mumbai", "Delhi"): 1400,
    ("Mumbai", "Mumbai"): 0,
    ("Mumbai", "Kolkata"): 1960,
    ("Mumbai", "Chennai"): 1340,
    ("Mumbai", "Bengaluru"): 980,

    ("Kolkata", "Delhi"): 1500,
    ("Kolkata", "Mumbai"): 1960,
    ("Kolkata", "Kolkata"): 0,
    ("Kolkata", "Chennai"): 1660,
    ("Kolkata", "Bengaluru"): 1870,

    ("Chennai", "Delhi"): 2180,
    ("Chennai", "Mumbai"): 1340,
    ("Chennai", "Kolkata"): 1660,
    ("Chennai", "Chennai"): 0,
    ("Chennai", "Bengaluru"): 350,

    ("Bengaluru", "Delhi"): 2150,
    ("Bengaluru", "Mumbai"): 980,
    ("Bengaluru", "Kolkata"): 1870,
    ("Bengaluru", "Chennai"): 350,
    ("Bengaluru", "Bengaluru"): 0,
}


def calculate_tour_distance(tour: List[str]) -> float:
    """Calculates total cost of visiting all cities in order and returning to start."""
    total = 0.0
    for i in range(len(tour)):
        from_city = tour[i]
        to_city = tour[(i + 1) % len(tour)]
        total += DISTANCE_MATRIX[(from_city, to_city)]
    return total


def solve_tsp_brute_force(cities: List[str], start_city: str) -> Tuple[List[str], float]:
    """
    Exhaustive search evaluating all (N-1)! permutations.
    Guarantees the global minimum cost tour.
    """
    other_cities = [c for c in cities if c != start_city]
    best_tour = None
    min_distance = float("inf")

    for perm in itertools.permutations(other_cities):
        current_tour = [start_city] + list(perm)
        dist = calculate_tour_distance(current_tour)
        if dist < min_distance:
            min_distance = dist
            best_tour = current_tour

    return best_tour, min_distance


def solve_tsp_nearest_neighbor(cities: List[str], start_city: str) -> Tuple[List[str], float]:
    """Greedy heuristic: Always visits the nearest unvisited city next."""
    unvisited = set(cities)
    unvisited.remove(start_city)
    tour = [start_city]
    current = start_city

    while unvisited:
        nearest = min(unvisited, key=lambda city: DISTANCE_MATRIX[(current, city)])
        tour.append(nearest)
        unvisited.remove(nearest)
        current = nearest

    total_dist = calculate_tour_distance(tour)
    return tour, total_dist


def main():
    print("=" * 65)
    print("Task 15: Traveling Salesman Problem (TSP)")
    print("=" * 65)

    start = "Delhi"
    print(f"Cities: {CITIES}")
    print(f"Starting and Ending Hub: {start}\n")

    # 1. Exact Optimal Solution
    optimal_tour, opt_dist = solve_tsp_brute_force(CITIES, start)
    full_opt_path = optimal_tour + [start]
    print("[1] Exact Optimal Solution (Exhaustive Search):")
    print(f"    Path: {' -> '.join(full_opt_path)}")
    print(f"    Total Cost: {opt_dist:.1f} km\n")

    # 2. Nearest Neighbor Heuristic
    nn_tour, nn_dist = solve_tsp_nearest_neighbor(CITIES, start)
    full_nn_path = nn_tour + [start]
    print("[2] Nearest Neighbor Heuristic (Greedy Approximation):")
    print(f"    Path: {' -> '.join(full_nn_path)}")
    print(f"    Total Cost: {nn_dist:.1f} km")


if __name__ == "__main__":
    main()

