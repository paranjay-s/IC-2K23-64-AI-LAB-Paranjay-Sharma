r"""
Task 8: Replace an Integer in a List
AI Lab Coursework - List Transformation & Replacement

Prolog Equivalent:
    % Replace all occurrences:
    replace([], _, _, []).
    replace([Old | Tail], Old, New, [New | ResultTail]) :-
        replace(Tail, Old, New, ResultTail).
    replace([Head | Tail], Old, New, [Head | ResultTail]) :-
        Head \= Old,
        replace(Tail, Old, New, ResultTail).

    % Replace first occurrence (using cut):
    replace_first([], _, _, []).
    replace_first([Old | Tail], Old, New, [New | Tail]) :- !.
    replace_first([Head | Tail], Old, New, [Head | ResultTail]) :-
        replace_first(Tail, Old, New, ResultTail).

Description:
    Demonstrates replacing an integer in a list: replacing all occurrences,
    replacing the first occurrence (with cut semantics), and replacing by index.
"""

from typing import List


def replace_all_recursive(lst: List[int], old_val: int, new_val: int) -> List[int]:
    """
    Recursively replaces all occurrences of old_val with new_val,
    mirroring the standard Prolog replace predicate.
    """
    if not lst:
        return []
    head, *tail = lst
    replacement_head = new_val if head == old_val else head
    return [replacement_head] + replace_all_recursive(tail, old_val, new_val)


def replace_first_recursive(lst: List[int], old_val: int, new_val: int) -> List[int]:
    """
    Replaces only the first occurrence of old_val with new_val (simulating Prolog cut !).
    """
    if not lst:
        return []
    head, *tail = lst
    if head == old_val:
        return [new_val] + tail  # Cut: do not recurse on tail
    return [head] + replace_first_recursive(tail, old_val, new_val)


def replace_at_index(lst: List[int], index: int, new_val: int) -> List[int]:
    """Replaces the element at a specific index."""
    if not (0 <= index < len(lst)):
        raise IndexError(f"Index {index} out of bounds for list of length {len(lst)}")
    copy_list = list(lst)
    copy_list[index] = new_val
    return copy_list


def main():
    print("=" * 60)
    print("Task 8: Replace an Integer in a List")
    print("=" * 60)

    sample = [10, 20, 30, 20, 50, 20, 70]
    old_target = 20
    replacement = 99

    print(f"Original List       : {sample}")
    print(f"Target Integer      : {old_target}")
    print(f"New Replacement     : {replacement}")

    # 1. Replace all occurrences
    all_replaced = replace_all_recursive(sample, old_target, replacement)
    print(f"\n1. Replace All      : {all_replaced}")

    # 2. Replace first occurrence (cut simulation)
    first_replaced = replace_first_recursive(sample, old_target, replacement)
    print(f"2. Replace First    : {first_replaced}")

    # 3. Replace by specific index
    idx_replaced = replace_at_index(sample, index=2, new_val=888)
    print(f"3. Replace at idx 2 : {idx_replaced}")


if __name__ == "__main__":
    main()
