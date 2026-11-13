"""
Task 7: Append an Integer into a List
AI Lab Coursework - List Construction & Recursion

Prolog Equivalent:
    append_elem([], Element, [Element]).
    append_elem([Head | Tail], Element, [Head | ResultTail]) :-
        append_elem(Tail, Element, ResultTail).

Description:
    Demonstrates appending an integer into a list using functional recursion
    (mirroring Prolog's immutable list construction) and Python's standard list methods.
"""

from typing import List


def append_integer_recursive(lst: List[int], element: int) -> List[int]:
    """
    Appends an integer to the end of a list recursively without mutating the original list.
    Mirroring Prolog's append relation:
    - Base case: appending to [] yields [element].
    - Recursive step: appending to [H|T] yields [H | append(T, element)].
    """
    if not isinstance(element, int):
        raise TypeError(f"Expected an integer, got {type(element).__name__}")

    if not lst:
        return [element]
    head, *tail = lst
    return [head] + append_integer_recursive(tail, element)


def append_integer_inplace(lst: List[int], element: int) -> List[int]:
    """Appends an integer using Python's in-place list.append() method."""
    if not isinstance(element, int):
        raise TypeError(f"Expected an integer, got {type(element).__name__}")
    lst.append(element)
    return lst


def main():
    print("=" * 60)
    print("Task 7: Append an Integer into a List")
    print("=" * 60)

    original_list = [10, 20, 30, 40]
    new_value = 50

    print(f"Original List       : {original_list}")
    print(f"Integer to Append   : {new_value}")

    # Recursive pure append
    rec_result = append_integer_recursive(original_list, new_value)
    print(f"Recursive Result    : {rec_result}")
    print(f"Original Unaltered  : {original_list}")

    # In-place append
    working_copy = list(original_list)
    append_integer_inplace(working_copy, new_value)
    print(f"In-place Appended   : {working_copy}")

    # Appending multiple integers sequentially
    extended = []
    print("\nSequential Appending:")
    for num in [7, 14, 21, 28, 35]:
        extended = append_integer_recursive(extended, num)
        print(f"  Appended {num:2d} -> {extended}")


if __name__ == "__main__":
    main()
