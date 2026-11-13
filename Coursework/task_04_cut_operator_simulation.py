"""
Task 4: Cut Operator Concept Simulation
AI Lab Coursework - Pruning Backtracking & Early Exit

Prolog Equivalent:
    % Without cut: Prolog may backtrack into subsequent rules even after finding a match.
    % With cut (!): Commits to choices made so far and prevents backtracking.
    max(X, Y, X) :- X >= Y, !.
    max(_, Y, Y).

    grade(Score, 'A') :- Score >= 90, !.
    grade(Score, 'B') :- Score >= 80, !.
    grade(Score, 'C') :- Score >= 70, !.
    grade(_, 'Fail').

Description:
    Demonstrates Prolog's Cut (!) operator in Python. Cut commits the interpreter
    to all choices made since the parent goal was invoked, effectively pruning
    the search tree and preventing unwanted backtracking.
"""

from typing import Generator, List, Tuple


def grade_with_cut(score: float) -> str:
    """
    Simulates Prolog's cut operator (!) in rule matching.
    Once a condition evaluates to True, we immediately return (early exit),
    preventing any subsequent alternative rules from being checked.
    """
    if score >= 90:
        return "A"  # Cut: Commit to 'A', do not check lower grades
    if score >= 80:
        return "B"  # Cut: Commit to 'B'
    if score >= 70:
        return "C"  # Cut: Commit to 'C'
    return "Fail"


def search_solutions(items: List[int], target: int) -> Generator[Tuple[int, int], None, None]:
    """Generator representing standard Prolog backtracking (searches all pairs)."""
    for i, x in enumerate(items):
        for j, y in enumerate(items):
            if i != j and x + y == target:
                yield (x, y)


def search_with_cut_simulation(items: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Simulates Cut (!): Stops backtracking immediately after the first
    successful unification/solution is encountered.
    """
    solutions = []
    for pair in search_solutions(items, target):
        solutions.append(pair)
        # Cut simulation: break immediately, pruning all remaining branches
        print(f"    [Cut Triggered!] Found first valid pair {pair}. Pruning remaining search space.")
        break
    return solutions


def max_with_cut(x: int, y: int) -> int:
    """
    Simulates:
        max(X, Y, X) :- X >= Y, !.
        max(_, Y, Y).
    """
    if x >= y:
        return x  # Cut prevents evaluating second rule
    return y


def main():
    print("=" * 60)
    print("Task 4: Simulation of Prolog's Cut Operator (!) in Python")
    print("=" * 60)

    print("\n[1] Rule Evaluation with Cut (Grade Classification):")
    test_scores = [95, 83, 72, 55]
    for s in test_scores:
        print(f"  Score: {s:2d} -> Grade: {grade_with_cut(s)}")

    print("\n[2] Backtracking Search Space Pruning:")
    numbers = [1, 3, 5, 2, 4, 6]
    target_sum = 7

    print(f"  List: {numbers}, Target Sum: {target_sum}")
    print("\n  a) Without Cut (Find ALL solutions via backtracking):")
    all_solutions = list(search_solutions(numbers, target_sum))
    for sol in all_solutions:
        print(f"     Found solution: {sol[0]} + {sol[1]} = {target_sum}")

    print("\n  b) With Cut Simulation (Commit to first solution and prune):")
    cut_solution = search_with_cut_simulation(numbers, target_sum)
    print(f"     Resulting Solutions: {cut_solution}")

    print("\n[3] Max of Two Numbers with Cut Logic:")
    print(f"  max_with_cut(15, 8)  -> {max_with_cut(15, 8)}")
    print(f"  max_with_cut(7, 23)  -> {max_with_cut(7, 23)}")


if __name__ == "__main__":
    main()
