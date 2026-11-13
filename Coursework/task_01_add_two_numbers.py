"""
Task 1: Add Two Numbers
AI Lab Coursework - Python Equivalent of Prolog Arithmetic

Prolog Equivalent:
    add(X, Y, Sum) :- Sum is X + Y.

Description:
    Demonstrates basic addition in Python, representing both standard functional
    arithmetic and a declarative/recursive logic approach (Peano arithmetic)
    analogous to Prolog's relational arithmetic.
"""


def add_numbers(a: float, b: float) -> float:
    """Standard addition of two numbers."""
    return a + b


def add_recursive(a: int, b: int) -> int:
    """
    Recursive addition (Peano-style arithmetic) mirroring Prolog logic:
    add(0, Y, Y).
    add(s(X), Y, s(Z)) :- add(X, Y, Z).
    """
    if a < 0:
        return -add_recursive(-a, -b)
    if a == 0:
        return b
    return 1 + add_recursive(a - 1, b)


def main():
    print("=" * 50)
    print("Task 1: Add Two Numbers (Prolog Equivalent in Python)")
    print("=" * 50)

    num1 = 15.5
    num2 = 26.5
    total = add_numbers(num1, num2)
    print(f"Standard Addition: {num1} + {num2} = {total}")

    int1 = 18
    int2 = 24
    rec_total = add_recursive(int1, int2)
    print(f"Recursive (Peano-style) Addition: {int1} + {int2} = {rec_total}")

    print("\nDemonstration with custom values:")
    test_cases = [(10, 20), (-5, 15), (0, 42), (100, -35)]
    for x, y in test_cases:
        print(f"  add({x}, {y}) -> {add_numbers(x, y)}")


if __name__ == "__main__":
    main()

