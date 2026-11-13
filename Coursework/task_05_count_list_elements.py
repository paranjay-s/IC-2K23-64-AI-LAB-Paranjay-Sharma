"""
Task 5: Count the Number of Elements in a List
AI Lab Coursework - List Processing & Recursion

Prolog Equivalent:
    count([], 0).
    count([_ | Tail], Count) :-
        count(Tail, SubCount),
        Count is SubCount + 1.

Description:
    Demonstrates counting elements in a list using recursive pattern-matching
    (Prolog Head-Tail decomposition) alongside iterative and built-in Python techniques.
"""

from typing import Any, List


def count_recursive(lst: List[Any]) -> int:
    """
    Counts elements using pure recursion, mirroring Prolog:
    Base case: [] has length 0.
    Recursive step: [_ | Tail] -> 1 + count(Tail).
    """
    if not lst:
        return 0
    _head, *tail = lst
    return 1 + count_recursive(tail)


def count_tail_recursive(lst: List[Any], accumulator: int = 0) -> int:
    """
    Tail-recursive counter using an accumulator, mirroring Prolog accumulator pattern:
    count_acc([], Acc, Acc).
    count_acc([_|T], Acc, R) :- Acc1 is Acc + 1, count_acc(T, Acc1, R).
    """
    if not lst:
        return accumulator
    _head, *tail = lst
    return count_tail_recursive(tail, accumulator + 1)


def count_iterative(lst: List[Any]) -> int:
    """Iterative loop counting elements."""
    count = 0
    for _ in lst:
        count += 1
    return count


def main():
    print("=" * 60)
    print("Task 5: Count Elements in a List (Prolog Logic in Python)")
    print("=" * 60)

    test_lists = [
        [],
        [42],
        [10, 20, 30, 40, 50],
        ["alpha", "beta", "gamma", "delta"],
        [True, False, 1, 0, "AI", 3.14],
    ]

    for idx, sample in enumerate(test_lists, 1):
        rec_cnt = count_recursive(sample)
        tail_cnt = count_tail_recursive(sample)
        iter_cnt = count_iterative(sample)
        builtin_cnt = len(sample)

        print(f"\nTest {idx}: List = {sample}")
        print(f"  Recursive Count      : {rec_cnt}")
        print(f"  Tail-Recursive Count : {tail_cnt}")
        print(f"  Iterative Count      : {iter_cnt}")
        print(f"  Built-in len()       : {builtin_cnt}")
        assert rec_cnt == tail_cnt == iter_cnt == builtin_cnt


if __name__ == "__main__":
    main()
