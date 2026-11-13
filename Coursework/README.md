# AI Lab Coursework - Python Implementations

**Student Name:** Paranjay Sharma  
**Roll / Scholar ID:** IC-2K23-64  
**Course:** MCA 7th Semester - Artificial Intelligence Laboratory  
**Repository:** [IC-2K23-64-AI-LAB-Paranjay-Sharma](https://github.com/paranjay-s/IC-2K23-64-AI-LAB-Paranjay-Sharma)

---

## Course Outcomes (COs)

- **CO1:** Get the basic idea of how to program in prolog and its working environment.
- **CO2:** Apply various AI search algorithms (uninformed, informed, heuristic, constraint satisfaction).
- **CO3:** Understand the fundamentals of knowledge representation.
- **CO4:** Ability to apply knowledge representation, reasoning, and machine learning techniques to realworld problem.

---

## Coursework Tasks Mapping Table

The university syllabus originally requested Prolog implementations; this repository provides fully functional, documented Python (`.py`) equivalents designed to illustrate declarative logic, knowledge bases, state-space search, and constraint satisfaction.

| Task # | Syllabus Question | Python File | Mapped CO | Description |
|:------:|:------------------|:------------|:---------:|:------------|
| **1** | Add two numbers | [`task_01_add_two_numbers.py`](./task_01_add_two_numbers.py) | **CO1** | Standard arithmetic and Peano-style recursive logic equivalent to Prolog relation `add(X, Y, Sum)`. |
| **2** | Categorize animal characteristics | [`task_02_animal_characteristics.py`](./task_02_animal_characteristics.py) | **CO3, CO4** | Knowledge base of animal facts and biological traits with rule-based categorization. |
| **3** | Read the address of a person using a compound variable/dictionary structure | [`task_03_person_address.py`](./task_03_person_address.py) | **CO1, CO3** | Compound data structures simulating Prolog nested functors `person(name(...), address(...))` using Python dictionaries. |
| **4** | Show the concept of the cut operator (simulate Prolog's cut/early exit in Python) | [`task_04_cut_operator_simulation.py`](./task_04_cut_operator_simulation.py) | **CO1** | Simulation of Prolog's cut (`!`) operator: search-space pruning, branch commitment, and early exit. |
| **5** | Count the number of elements in a list | [`task_05_count_list_elements.py`](./task_05_count_list_elements.py) | **CO1** | Head-tail recursive list counting, accumulator pattern, and iterative techniques. |
| **6** | Reverse a list | [`task_06_reverse_list.py`](./task_06_reverse_list.py) | **CO1** | List reversal via naive recursion, linear-time accumulator pattern, and two-pointer swap. |
| **7** | Append an integer into a list | [`task_07_append_integer_to_list.py`](./task_07_append_integer_to_list.py) | **CO1** | Pure recursive list append preserving immutability alongside in-place list methods. |
| **8** | Replace an integer in a list | [`task_08_replace_integer_in_list.py`](./task_08_replace_integer_in_list.py) | **CO1** | Recursive replacement of all occurrences, first occurrence (cut logic), and index-based replacement. |
| **9** | Delete an integer from a list | [`task_09_delete_integer_from_list.py`](./task_09_delete_integer_from_list.py) | **CO1** | Recursive element deletion (all instances vs first occurrence) and index deletion. |
| **10** | Show the general concept of a list (creation, iteration, basic methods) | [`task_10_list_concepts.py`](./task_10_list_concepts.py) | **CO1** | Creation, slicing, iteration, searching, sorting, and manipulation methods on dynamic lists. |
| **11** | Demonstrate family relationships (using classes, dictionaries, or a basic knowledge base) | [`task_11_family_relationships.py`](./task_11_family_relationships.py) | **CO3, CO4** | Knowledge Base representing family trees with rule inference (father, mother, sibling, grandparent, ancestor). |
| **12** | Show how an integer variable is used | [`task_12_integer_variable_usage.py`](./task_12_integer_variable_usage.py) | **CO1** | Integer declaration, memory model (immutability), arithmetic, bitwise logic, and type casting. |
| **13** | Solve the 8-queens problem | [`task_13_eight_queens.py`](./task_13_eight_queens.py) | **CO2** | Constraint Satisfaction Problem (CSP) solved via backtracking search; outputs all 92 configurations. |
| **14** | Implement Depth First Search (DFS) | [`task_14_depth_first_search.py`](./task_14_depth_first_search.py) | **CO2** | Uninformed state-space search: recursive DFS, explicit stack iterative DFS, and goal path-finding. |
| **15** | Solve the Traveling Salesman Problem (TSP) | [`task_15_traveling_salesman.py`](./task_15_traveling_salesman.py) | **CO2, CO4** | NP-hard combinatorial optimization: exact exhaustive search vs nearest-neighbor greedy heuristic. |

---

## How to Execute the Code

Run any task file directly using `python3` from the repository root:

```bash
# Example: Run Task 1 (Add two numbers)
python3 Coursework/task_01_add_two_numbers.py

# Example: Run Task 11 (Family Relationships Knowledge Base)
python3 Coursework/task_11_family_relationships.py

# Example: Run Task 13 (8-Queens Problem)
python3 Coursework/task_13_eight_queens.py

# Example: Run Task 14 (Depth First Search)
python3 Coursework/task_14_depth_first_search.py

# Example: Run Task 15 (Traveling Salesman Problem)
python3 Coursework/task_15_traveling_salesman.py
```

To run all 15 tasks sequentially:
```bash
for task in Coursework/task_*.py; do
    echo "Running $task..."
    python3 "$task"
    echo ""
done
```
