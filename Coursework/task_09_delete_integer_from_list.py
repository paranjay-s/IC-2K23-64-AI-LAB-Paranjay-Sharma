r"""
Task 9: Delete an Integer from a List
AI Lab Coursework - List Element Removal

Prolog Equivalent:
    % Delete all occurrences:
    delete_all([], _, []).
    delete_all([Target | Tail], Target, Result) :-
        delete_all(Tail, Target, Result).
    delete_all([Head | Tail], Target, [Head | Result]) :-
        Head \= Target,
        delete_all(Tail, Target, Result).

    % Delete first occurrence (using cut !):
    delete_first([], _, []).
    delete_first([Target | Tail], Target, Tail) :- !.
    delete_first([Head | Tail], Target, [Head | Result]) :-
        delete_first(Tail, Target, Result).

Description:
    Demonstrates deleting an integer from a list: deleting all instances,
    deleting the first instance, and deleting by index.
"""

from typing import List


def delete_all_recursive(lst: List[int], target: int) -> List[int]:
    """
    Recursively removes all occurrences of target from the list,
    mirroring Prolog's delete_all predicate.
    """
    if not lst:
        return []
    head, *tail = lst
    if head == target:
        return delete_all_recursive(tail, target)
    return [head] + delete_all_recursive(tail, target)


def delete_first_recursive(lst: List[int], target: int) -> List[int]:
    """
    Recursively removes only the first occurrence of target (simulating cut !).
    """
    if not lst:
        return []
    head, *tail = lst
    if head == target:
        return tail  # Cut: Stop further search and return remaining tail
    return [head] + delete_first_recursive(tail, target)


def delete_by_index(lst: List[int], index: int) -> List[int]:
    """Deletes an element at a given index."""
    if not (0 <= index < len(lst)):
        raise IndexError(f"Index {index} out of range for list of length {len(lst)}")
    copy_list = list(lst)
    del copy_list[index]
    return copy_list


def main():
    print("=" * 60)
    print("Task 9: Delete an Integer from a List")
    print("=" * 60)

    sample = [5, 12, 18, 12, 25, 12, 30]
    target_to_remove = 12

    print(f"Original List       : {sample}")
    print(f"Target to Delete    : {target_to_remove}")

    # 1. Delete all occurrences
    all_removed = delete_all_recursive(sample, target_to_remove)
    print(f"\n1. Delete All       : {all_removed}")

    # 2. Delete first occurrence
    first_removed = delete_first_recursive(sample, target_to_remove)
    print(f"2. Delete First     : {first_removed}")

    # 3. Delete by index
    idx_removed = delete_by_index(sample, 2)
    print(f"3. Delete Index 2   : {idx_removed}")


if __name__ == "__main__":
    main()
