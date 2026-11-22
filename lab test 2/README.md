# AI Lab Test 2: Emergency Evacuation Planner (Set 3)

***Youtube Explanation Video Link :*** https://youtu.be/pcPHGxJMemI

**Student Name:** Paranjay Sharma  
**Roll Number:** IC-2K23-64 *(Assigned Set: Set 3 for Roll No. 60–65)*  
**Degree / Semester:** MCA 7th Semester  
**Course:** Artificial Intelligence Laboratory (Lab Test 2)  
**Topic:** Emergency Evacuation Planner using Knowledge Representation, Graph Path Search, and Constraint Satisfaction  

---

## 1. Problem Statement & Overview

During an emergency such as a fire, people inside a multi-story or complex building need to reach a safe exit as swiftly as possible. Some corridors or staircases may become blocked by debris, fire, or toxic smoke. 

This project implements an **Intelligent Emergency Evacuation Planner** in both **Prolog** (Turbo Prolog and GNU-Prolog) and **Python**. The system represents building locations and their interconnecting passages as a graph network, evaluates safety constraints dynamically, and finds the safest path from a designated starting location to an accessible emergency exit.

### Core Requirements
1. **Locations:** Represents at least 6 locations (this implementation models 10 distinct nodes: rooms, corridors, staircases, and exits).
2. **Graph Connections:** Stored as Prolog relational facts with bidirectional adjacency.
3. **Hazard Constraints:** Allows connections to be marked as `blocked` and rooms/corridors as `unsafe`.
4. **Search Algorithm:** Finds a valid evacuation path from an arbitrary start point to an exit, guaranteeing no traversal through hazardous corridors or cycles.
5. **Output Display:** Clearly prints the evacuation route, exit destination, transitions, and cumulative risk. If no route exists, it outputs an emergency shelter-in-place alert.
6. **Additional Challenges Addressed:**
   - Quantitative risk weighting (smoke/hazard intensity) on each corridor.
   - Lowest-risk path optimization among multiple available exits.
   - Dynamic backtracking to alternative routes when primary paths are blocked.

---

## 2. Evaluation Scheme Mapping (20 Marks)

| Evaluation Criteria | Max Marks | Implementation Highlights |
|:---|:---:|:---|
| **Understanding & Knowledge Representation** | 3 | 10 building nodes, bidirectional edge facts, exit facts, and dynamic hazard predicates (`blocked/2`, `unsafe/1`). |
| **Logical Approach & Decision-Making** | 5 | Recursive Depth-First Search with cycle prevention (`Visited` list), constraint pruning, and multi-exit risk minimization. |
| **Prolog Implementation** | 5 | Complete Borland Turbo Prolog (`.pro`) and ISO GNU-Prolog (`.pl`) implementations with clean predicate definitions. |
| **Execution & Test Cases** | 3 | 3 distinct scenarios tested: default syllabus hazard, alternative multi-exit routing, and total isolation lockdown. |
| **Viva & Live Modification** | 4 | Complete viva preparation section with live modification instructions provided below. |
| **Total** | **20** | |

---

## 3. Building Network Topology

```
+-----------------------------------------------------------------+
|                    BUILDING NETWORK TOPOLOGY                    |
+-----------------------------------------------------------------+
|                                                                 |
|   [Room C] <=======> [Corridor 2] <=======> [Room A] (Start)    |
|      |                                         |                |
|      v (Stairs 2)                              v (Risk 1)       |
|  [Exit 3] (North Gate)                    [Corridor 1]          |
|                                            /        \           |
|                        (Risk 2, Blockable)/          \ (Risk 1)  |
|                                          v            v         |
|                                   [Staircase 1]   [Room B]      |
|                                          |            |         |
|                                          v            v         |
|                                       [Exit 1]     [Exit 2]     |
|                                    (Ground East) (Main Ground)  |
+-----------------------------------------------------------------+
```

### Locations Represented (10 Nodes)
- **`room_a`**: Starting Room (Office 101)
- **`room_b`**: Conference Hall
- **`room_c`**: Computer Laboratory
- **`corridor_1`**: Main Central Corridor
- **`corridor_2`**: North Wing Bypass Corridor
- **`corridor_3`**: South Wing Service Corridor
- **`staircase_1`**: East Fire Escape Staircase
- **`staircase_2`**: West Central Staircase
- **`exit_1`**: Ground East Fire Exit
- **`exit_2`**: Main Ground Floor Entrance Exit
- **`exit_3`**: North Emergency Perimeter Gate

---

## 4. File Structure in this Folder

| File Name | Language / Target | Purpose |
|:---|:---|:---|
| [`evacuation_planner.pl`](./evacuation_planner.pl) | GNU-Prolog / SWI-Prolog (ISO) | Modern Prolog code runnable natively on macOS/Linux via `gprolog`. Includes automated self-test runner. |
| [`evacuation_planner_turbo.pro`](./evacuation_planner_turbo.pro) | Borland Turbo Prolog 2.0 | Traditional Turbo Prolog file with `DOMAINS`, `PREDICATES`, and `CLAUSES` for university lab DOSBox environments. |
| [`evacuation_planner.py`](./evacuation_planner.py) | Python 3 | Pure Python equivalent demonstrating identical declarative logic, search algorithm, ASCII topology, and test cases. |
| [`README.md`](./README.md) | Markdown | Comprehensive assessment report, algorithm description, test outputs, and viva guide. |

---

## 5. How to Run

### Method A: Running the GNU-Prolog Program (`evacuation_planner.pl`)
On macOS/Linux where GNU-Prolog is installed:

```bash
cd "lab test 2"
# Run all 3 test scenarios automatically:
echo "run_all_tests, halt." | gprolog --consult-file evacuation_planner.pl
```

Or run interactively inside the Prolog shell:
```prolog
gprolog
| ?- consult('evacuation_planner.pl').
| ?- evacuate(room_a).
| ?- test_case_1.
| ?- test_case_2.
| ?- test_case_3.
| ?- halt.
```

### Method B: Running the Python Demonstration (`evacuation_planner.py`)
```bash
python3 "lab test 2/evacuation_planner.py"
```

### Method C: Running in Turbo Prolog (DOSBox in University Lab)
1. Open DOSBox and launch Turbo Prolog: `PROLOG.EXE`.
2. Press `Alt + F` -> `Load` -> Open `EVAC.PRO` (or copy the contents of `evacuation_planner_turbo.pro`).
3. Press `Alt + R` to compile and run.
4. Type `run_all_tests` or `evacuate(room_a)` at the Goal prompt.

---

## 6. Detailed Test Cases & Verified Outputs

### Test Case 1: Standard Syllabus Scenario
- **Conditions:** Person starts at `room_a`.
- **Active Hazard:** The connection between `corridor_1` and `staircase_1` is blocked by fire.
- **Expected Route:** `room_a -> corridor_1 -> room_b -> exit_2`
- **Output:**
```text
=====================================================
            EMERGENCY EVACUATION PLANNER             
=====================================================
Starting Location : room_a
Destination Exit  : exit_2
Evacuation Route  : room_a -> corridor_1 -> room_b -> exit_2
Total Transitions : 3
Cumulative Risk   : 3
Status            : Route Found (Safe to proceed)
=====================================================
```
- **Explanation:** The path through `staircase_1 -> exit_1` is pruned because the connection `(corridor_1, staircase_1)` fails `\+ is_blocked(X, Y)`. Prolog backtracks, explores the branch to `room_b`, and safely terminates at `exit_2`.

---

### Test Case 2: Multi-Hazard & Alternative Route via North Wing
- **Conditions:** Person starts at `room_a`.
- **Active Hazards:**
  1. Connection `(corridor_1, staircase_1)` is blocked.
  2. Connection `(corridor_1, room_b)` is blocked.
- **Expected Route:** `room_a -> corridor_2 -> room_c -> staircase_2 -> exit_3`
- **Output:**
```text
=====================================================
            EMERGENCY EVACUATION PLANNER             
=====================================================
Starting Location : room_a
Destination Exit  : exit_3
Evacuation Route  : room_a -> corridor_2 -> room_c -> staircase_2 -> exit_3
Total Transitions : 4
Cumulative Risk   : 5
Status            : Route Found (Safe to proceed)
=====================================================
```
- **Explanation:** All passages through `corridor_1` are impassable. The inference engine backtracks to `room_a`, identifies the alternative branch via `corridor_2`, traverses through `room_c` and `staircase_2`, and guides the occupant to `exit_3`.

---

### Test Case 3: Complete Isolation / Total Hazard (Failsafe Warning)
- **Conditions:** Person starts at `room_a`.
- **Active Hazards:** Both main corridors exiting Room A (`corridor_1` and `corridor_2`) are engulfed in flames (`unsafe(corridor_1).`, `unsafe(corridor_2).`).
- **Expected Result:** Safe termination with an emergency warning.
- **Output:**
```text
=====================================================
            EMERGENCY EVACUATION PLANNER             
=====================================================
Starting Location : room_a
Status            : NO SAFE ROUTE AVAILABLE!
Alert             : All exit corridors are blocked or unsafe.
Action            : Shelter in place, seal doors, await rescue.
=====================================================
```
- **Explanation:** Because all transitions from `room_a` fail the `safe_transition/3` safety check, the search exhausts all choice points. The fallback clause triggers to provide actionable life-safety instructions.

---

## 7. Viva Voce & Live Modification Guide (For the 4 Exam Marks)

During the practical exam, examiners frequently ask students to modify a rule or add an input condition live. Here is how to handle the most common requests:

### Live Modification 1: "Add a new corridor between Room C and Exit 1"
In Prolog, simply append a new fact:
```prolog
connection(room_c, exit_1, 1).
```
The search engine will automatically discover and use this new connection without altering any search logic!

### Live Modification 2: "Make Exit 2 unavailable because the ground floor door is locked"
Temporarily retract `exit_node(exit_2)` or mark it unsafe:
```prolog
retract(exit_node(exit_2)).
% Or:
assertz(unsafe(exit_2)).
```

### Live Modification 3: "How does the system prevent infinite loops?"
Prolog maintains a `Visited` list accumulator:
```prolog
find_path(Current, Exit, Visited, [Current | PathTail], TotalRisk) :-
    safe_transition(Current, Next, StepRisk),
    \+ list_member(Next, Visited),           % Prevents visiting the same node twice
    find_path(Next, Exit, [Next | Visited], PathTail, SubRisk),
    ...
```

### Live Modification 4: "What is the difference between Turbo Prolog and GNU Prolog?"
- **Turbo Prolog** is strongly typed: all symbols, lists, and numbers must be declared under `DOMAINS`, and predicates under `PREDICATES`.
- **GNU-Prolog / SWI-Prolog** follows the ISO standard: untyped Horn clauses, dynamic term unification, and built-in primitives like `findall/3` and `sort/2`.
