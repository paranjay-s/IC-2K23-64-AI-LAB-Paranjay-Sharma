"""
Task 10: General Concept of a List (Creation, Iteration, Basic Methods)
AI Lab Coursework - Python Fundamentals vs Prolog Lists

Prolog vs Python List Concepts:
    - In Prolog, a list is an inductively defined linked cell: [Head | Tail],
      where [] is nil, and [1, 2, 3] is .(1, .(2, .(3, []))).
    - In Python, a list is a dynamic array providing O(1) random access,
      dynamic resizing, and rich built-in utility methods.

Description:
    Comprehensive demonstration of Python lists covering creation, indexing,
    slicing, iteration, modification, searching, and built-in methods.
"""


def demonstrate_list_creation():
    """Demonstrates various ways to create lists in Python."""
    empty_list = []
    literal_list = [10, 20, 30, 40, 50]
    range_list = list(range(1, 6))
    comprehension_list = [x**2 for x in range(1, 6)]
    mixed_list = ["AI", 2026, 3.14, True, [1, 2]]

    print("--- 1. List Creation ---")
    print(f"Empty List        : {empty_list}")
    print(f"Literal List      : {literal_list}")
    print(f"From range()      : {range_list}")
    print(f"Comprehension     : {comprehension_list}")
    print(f"Heterogeneous     : {mixed_list}")


def demonstrate_indexing_and_slicing():
    """Demonstrates index access and slicing techniques."""
    items = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"]

    print("\n--- 2. Indexing & Slicing ---")
    print(f"List              : {items}")
    print(f"First element [0] : {items[0]}")
    print(f"Last element [-1] : {items[-1]}")
    print(f"Slice [1:4]       : {items[1:4]}")
    print(f"Slice [:3]        : {items[:3]}")
    print(f"Slice [::2]       : {items[::2]} (every 2nd item)")
    print(f"Reversed [::-1]   : {items[::-1]}")


def demonstrate_iteration():
    """Demonstrates traversal and iteration patterns."""
    fruits = ["Apple", "Banana", "Cherry"]

    print("\n--- 3. Iteration Techniques ---")
    print("Standard for-loop:")
    for fruit in fruits:
        print(f"  Item: {fruit}")

    print("Enumeration with indices:")
    for idx, fruit in enumerate(fruits, start=1):
        print(f"  Index {idx}: {fruit}")


def demonstrate_list_methods():
    """Demonstrates fundamental mutating and query methods on lists."""
    numbers = [30, 10, 50, 20, 40]
    print("\n--- 4. Basic List Methods ---")
    print(f"Initial List      : {numbers}")

    # Append
    numbers.append(60)
    print(f"append(60)        : {numbers}")

    # Insert
    numbers.insert(2, 25)
    print(f"insert(2, 25)     : {numbers}")

    # Extend
    numbers.extend([70, 80])
    print(f"extend([70, 80])  : {numbers}")

    # Pop
    popped = numbers.pop()
    print(f"pop() -> {popped}       : {numbers}")

    # Remove
    numbers.remove(25)
    print(f"remove(25)        : {numbers}")

    # Index and Count
    print(f"index of 50       : {numbers.index(50)}")
    print(f"count of 20       : {numbers.count(20)}")

    # Sort
    numbers.sort()
    print(f"sort()            : {numbers}")

    # Reverse
    numbers.reverse()
    print(f"reverse()         : {numbers}")


def main():
    print("=" * 60)
    print("Task 10: General Concept of Lists in Python")
    print("=" * 60)
    demonstrate_list_creation()
    demonstrate_indexing_and_slicing()
    demonstrate_iteration()
    demonstrate_list_methods()


if __name__ == "__main__":
    main()
