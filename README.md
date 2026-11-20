# AI Lab Projects: Classic Search and Puzzle Algorithms

This repository contains Python solutions for classic artificial intelligence problems, university coursework, and machine learning models. The code is written to be clean, easy to read, and easy to explain for lab assessments. 

## 1. Water Jug Problem (water_jug.py)

* **The Problem:** You have two empty jugs of different sizes. You need to measure out a specific amount of water using an endless water supply.
* **The Solution:** The code uses an algorithm called Breadth-First Search (BFS). BFS looks at every possible move one level at a time, which guarantees it will find the absolute shortest number of steps to reach the goal.
* **Loop Prevention:** It keeps a record of previous water levels so it does not repeat the same pouring steps over and over.
* **How to test your own numbers:** Open the file and change the `jug1_cap`, `jug2_cap`, and `target_amount` variables at the very bottom.

## 2. Missionaries and Cannibals (missionaries_cannibals.py)

* **The Problem:** Move a group of missionaries and cannibals across a river using a small boat. The strict rule is that cannibals can never outnumber missionaries on either bank of the river.
* **The Solution:** This also uses BFS to find the shortest set of boat trips, but it adds a strict safety checker. Before making any move, it runs a validation function to ensure the move does not break the survival rules.
* **How to test your own numbers:** Change the `TOTAL_M` (missionaries), `TOTAL_C` (cannibals), and `BOAT_CAPACITY` variables at the top of the script.

## 3. Sudoku Solver (sudoku_solver.py)

* **The Problem:** Solve a standard 9x9 Sudoku grid where no number from 1 to 9 can repeat in any row, column, or 3x3 box.
* **The Solution:** The code uses an algorithm called Backtracking. It places a number in an empty spot and moves forward. If it hits a dead end where no number fits, it backs up, erases the previous number, and tries a different one.
* **How to test your own puzzle:** Update the 2D list named `board` at the top of the file. Use the number `0` to represent empty squares.

## 4. University Coursework (`Coursework/` folder)

* **The Scope:** This folder contains 15 individual Python scripts that map directly to the AI Lab syllabus (originally intended for Prolog).
* **Topics Covered:** The scripts cover basic operations, list manipulation, family relationships representation, and classic AI problems like the 8-Queens problem, Depth First Search (DFS), and the Traveling Salesman Problem (TSP).
* **Detailed Mapping:** Please see the dedicated `README.md` inside the `Coursework` folder to see exactly how each script maps to the university's Course Outcomes (CO1-CO4) and the 15 assigned questions.

## 5. Decision Tree Mini Project (`mini project/` folder)

* **The Problem:** An AI model trained to decide whether you should go for a walk outside based on weather conditions.
* **The Solution:** Uses a `DecisionTreeClassifier` from the `scikit-learn` library. It trains on a simulated dataset of past days utilizing two main features ("Temperature" and "Chance of Rain") to predict a final decision (1 = Go Outside, 0 = Stay Inside).
* **How to test:** Run `weather_walk_predictor.py` inside the `mini project` folder to see the tree predict an outcome based on sample weather conditions.

## 6. AI Lab Test 2: Emergency Evacuation Planner (`lab test 2/` folder)

* **Assigned Problem:** Set 3 (Emergency Evacuation Planner - Roll No 60-65, Roll No 64).
* **The Scope:** Formulates building rooms, corridors, staircases, and fire exits as an interconnected graph with dynamic constraints (blocked connections, smoke/fire hazards) and risk minimization.
* **Implementations Provided:**
  * `evacuation_planner.pl`: GNU-Prolog / SWI-Prolog ISO standard source code with automated self-tests.
  * `evacuation_planner_turbo.pro`: Authentic Borland Turbo Prolog 2.0 source code (`DOMAINS`, `PREDICATES`, `CLAUSES`) for university lab DOSBox.
  * `evacuation_planner.py`: Complete Python equivalent simulating Prolog reasoning, risk optimization, and test scenarios.
  * `README.md`: Complete evaluation criteria report, 3 verified test scenarios, and viva modification guide.
* **How to test:** Run `python3 "lab test 2/evacuation_planner.py"` or `echo "run_all_tests, halt." | gprolog --consult-file "lab test 2/evacuation_planner.pl"`.

## How to Run the Code

* You will need Python 3 installed on your computer.
* Open your terminal or command prompt.
* Clone this repository to your machine using:
  `git clone https://github.com/paranjay-s/IC-2K23-64-AI-LAB-Paranjay-Sharma.git`
* Move into the new folder:
  `cd IC-2K23-64-AI-LAB-Paranjay-Sharma`

**To run the classic AI scripts:**
No extra libraries are required. Simply run:
* `python water_jug.py`
* `python missionaries_cannibals.py`
* `python sudoku_solver.py`

**To run the Mini Project:**
You will need to install the required data science libraries first:
* `pip install scikit-learn pandas numpy`
* `cd "mini project"`
* `python weather_walk_predictor.py`

**To run the Coursework scripts:**
* `cd Coursework`
* `python [filename].py` (replace `[filename].py` with the specific script you want to test)
