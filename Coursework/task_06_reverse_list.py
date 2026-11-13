"""
Task 6: Reverse a List
AI Lab Coursework - List Inversion & Prolog Accumulator Pattern

Prolog Equivalent:
    % Naive Reverse:
    rev([], []).
    rev([H|T], R) :- rev(T, RevT), append(RevT, [H], R).

    % Accumulator-based Reverse (Linear O(N) efficiency):
    rev_acc([], Acc, Acc).
    rev_acc([H|T], Acc, R) :- rev_acc(T, [H|Acc], R).

Description:
    Implements list reversal in Python using functional recursion,
    Prolog accumulator technique, two-pointer in-place swap, and Python slicing.
"""

from typing import Any, List


def reverse_naive_recursive(lst: List[Any]) -> List[Any]:
    """
    Naive recursive reversal mirroring Prolog's naive reverse:
    rev([H|T]) -> rev(T) + [H]
    """
    if not lst:
        return []
    head, *tail = lst
    return reverse_naive_recursive(tail) + [head]


def reverse_accumulator(lst: List[Any], acc: List[Any] = None) -> List[Any]:
    """
    Efficient tail-recursive reversal using an accumulator,
    mirroring Prolog's rev_acc([H|T], Acc, R) :- rev_acc(T, [H|Acc], R).
    """
    if acc is None:
        acc = []
    if not lst:
        return acc
    head, *tail = lst
    return reverse_accumulator(tail, [head] + acc)


def reverse_two_pointers(lst: List[Any]) -> List[Any]:
    """In-place reversal using two-pointer swap technique."""
    arr = list(lst)
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def main():
    print("=" * 60)
    print("Task 6: Reverse a List (Prolog Logic in Python)")
    print("=" * 60)

    test_lists = [
        [],
        [1],
        [1, 2, 3, 4, 5],
        ["Prolog", "Lisp", "Python", "Haskell"],
        [100, 200, 300, 400],
    ]

    for idx, original in enumerate(test_lists, 1):
        naive_rev = reverse_naive_recursive(original)
        acc_rev = reverse_accumulator(original)
        two_pt_rev = reverse_two_pointers(original)
        slice_rev = original[::-1]

        print(f"\nTest {idx}: Original = {original}")
        print(f"  Naive Recursive Reverse  : {naive_rev}")
        print(f"  Accumulator Reverse      : {acc_rev}")
        print(f"  Two-Pointer Reverse      : {two_pt_rev}")
        print(f"  Python Slicing [::-1]    : {slice_rev}")
        assert naive_rev == acc_rev == two_pt_rev == slice_rev


if __name__ == "__main__":
    main()

