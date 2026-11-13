"""
Task 12: How an Integer Variable is Used
AI Lab Coursework - Variable Mechanics & Arithmetic Logic

Description:
    Demonstrates the creation, memory model (immutability), arithmetic operations,
    bitwise logic, type casting, and relational comparison of integer variables
    in Python.
"""


def demonstrate_declaration_and_memory():
    print("--- 1. Declaration, Assignment, & Immutability ---")
    x = 42
    print(f"Variable x = {x}, Type = {type(x).__name__}, Memory Address = {id(x)}")

    # Immutability: Reassigning creates a new object in memory
    old_id = id(x)
    x = x + 1
    new_id = id(x)
    print(f"After x = x + 1: x = {x}")
    print(f"Memory Address Changed: {old_id != new_id} (old={old_id}, new={new_id})")


def demonstrate_arithmetic():
    print("\n--- 2. Arithmetic Operations ---")
    a = 23
    b = 7
    print(f"a = {a}, b = {b}")
    print(f"  Addition (a + b)            : {a + b}")
    print(f"  Subtraction (a - b)         : {a - b}")
    print(f"  Multiplication (a * b)      : {a * b}")
    print(f"  True Division (a / b)       : {a / b:.4f}")
    print(f"  Floor Division (a // b)     : {a // b}")
    print(f"  Modulus / Remainder (a % b) : {a % b}")
    print(f"  Exponentiation (b ** 2)     : {b ** 2}")


def demonstrate_bitwise():
    print("\n--- 3. Bitwise Operations ---")
    p = 12  # 0b1100
    q = 10  # 0b1010
    print(f"p = {p} (bin: {bin(p)}), q = {q} (bin: {bin(q)})")
    print(f"  Bitwise AND (p & q)         : {p & q} (bin: {bin(p & q)})")
    print(f"  Bitwise OR  (p | q)         : {p | q} (bin: {bin(p | q)})")
    print(f"  Bitwise XOR (p ^ q)         : {p ^ q} (bin: {bin(p ^ q)})")
    print(f"  Bitwise NOT (~p)            : {~p}")
    print(f"  Left Shift (p << 1)         : {p << 1} (bin: {bin(p << 1)})")
    print(f"  Right Shift (p >> 1)        : {p >> 1} (bin: {bin(p >> 1)})")


def demonstrate_casting_and_comparisons():
    print("\n--- 4. Comparisons & Type Conversions ---")
    val_from_str = int("128")
    val_from_float = int(99.85)  # Truncates
    print(f"int('128')  -> {val_from_str}")
    print(f"int(99.85)  -> {val_from_float}")

    n = 15
    print(f"\nEvaluating n = {n}:")
    print(f"  Is n > 10?                  : {n > 10}")
    print(f"  Is n even? (n % 2 == 0)     : {n % 2 == 0}")
    print(f"  Is 10 <= n <= 20?           : {10 <= n <= 20}")


def main():
    print("=" * 60)
    print("Task 12: Usage of Integer Variables in Python")
    print("=" * 60)
    demonstrate_declaration_and_memory()
    demonstrate_arithmetic()
    demonstrate_bitwise()
    demonstrate_casting_and_comparisons()


if __name__ == "__main__":
    main()

