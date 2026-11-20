/* =========================================================================
   EMERGENCY EVACUATION PLANNER
   Lab Test 2 - Set 3 (Roll No: 64, Student: Paranjay Sharma)
   Course: MCA 7th Sem - Artificial Intelligence Laboratory
   Implementation: ISO & GNU-Prolog Compatible
   ========================================================================= */

/* -------------------------------------------------------------------------
   1. DYNAMIC PREDICATES FOR RUNTIME HAZARD CONFIGURATION
   Allows blocking/unblocking corridors and marking locations unsafe dynamically.
   GNU Prolog syntax requires parentheses: :- dynamic(pred/arity).
   ------------------------------------------------------------------------- */
:- dynamic(blocked/2).
:- dynamic(unsafe/1).

/* -------------------------------------------------------------------------
   2. KNOWLEDGE BASE: LOCATIONS, GRAPH CONNECTIONS, AND RISKS
   Network of Rooms, Corridors, Staircases, and Exits (10 Locations).
   connection(From, To, RiskWeight)
   Risk: 1 = Low/Clear, 2 = Medium/Smoke, 4 = High Hazard
   ------------------------------------------------------------------------- */

% Exit Points
exit_node(exit_1).
exit_node(exit_2).
exit_node(exit_3).

% Location Descriptions
location_type(room_a, 'Room (Office 101)').
location_type(room_b, 'Room (Conference Hall)').
location_type(room_c, 'Room (Computer Lab)').
location_type(corridor_1, 'Main Central Corridor').
location_type(corridor_2, 'North Wing Corridor').
location_type(corridor_3, 'South Wing Corridor').
location_type(staircase_1, 'Staircase East (Fire Escape)').
location_type(staircase_2, 'Staircase West (Central Stairs)').
location_type(exit_1, 'Ground Floor East Fire Exit').
location_type(exit_2, 'Ground Floor Main Entrance Exit').
location_type(exit_3, 'North Emergency Perimeter Gate').

% Bidirectional Building Graph with Risk Levels
connection(room_a, corridor_1, 1).
connection(corridor_1, staircase_1, 2).
connection(corridor_1, room_b, 1).
connection(room_b, exit_2, 1).
connection(staircase_1, exit_1, 1).

% Additional interconnected building layout for alternative routes
connection(room_a, corridor_2, 2).
connection(corridor_2, room_c, 1).
connection(room_c, staircase_2, 1).
connection(staircase_2, exit_3, 1).
connection(room_b, corridor_3, 1).
connection(corridor_3, staircase_1, 2).
connection(corridor_3, exit_2, 2).

/* -------------------------------------------------------------------------
   3. GRAPH TRAVERSAL & CONSTRAINT LOGIC
   Ensure undirected traversal, check safety against blocked paths and unsafe nodes.
   ------------------------------------------------------------------------- */

% Symmetric adjacency with risk cost
adjacent(X, Y, Cost) :- connection(X, Y, Cost).
adjacent(X, Y, Cost) :- connection(Y, X, Cost).

% Check if a specific connection is blocked (bidirectional check)
is_blocked(X, Y) :- blocked(X, Y).
is_blocked(X, Y) :- blocked(Y, X).

% A transition is safe iff neither connection is blocked nor destination node is unsafe
safe_transition(From, To, Cost) :-
    adjacent(From, To, Cost),
    \+ is_blocked(From, To),
    \+ unsafe(To).

/* -------------------------------------------------------------------------
   4. HELPER PREDICATES (PORTABLE LIST UTILITIES)
   ------------------------------------------------------------------------- */

list_member(X, [X | _]).
list_member(X, [_ | Tail]) :- list_member(X, Tail).

get_last([X], X).
get_last([_ | Tail], Last) :- get_last(Tail, Last).

get_length([], 0).
get_length([_ | Tail], N) :-
    get_length(Tail, N1),
    N is N1 + 1.

/* -------------------------------------------------------------------------
   5. PATH SEARCH (DEPTH-FIRST SEARCH WITH CYCLE PREVENTION)
   find_path(Current, Exit, Visited, Path, TotalRisk)
   ------------------------------------------------------------------------- */

% Base case: Destination reached is an exit node
find_path(Current, Current, _, [Current], 0) :-
    exit_node(Current).

% Recursive step: Move to a safe neighbor not previously visited
find_path(Current, Exit, Visited, [Current | PathTail], TotalRisk) :-
    safe_transition(Current, Next, StepRisk),
    \+ list_member(Next, Visited),
    find_path(Next, Exit, [Next | Visited], PathTail, SubRisk),
    TotalRisk is StepRisk + SubRisk.

/* -------------------------------------------------------------------------
   6. OPTIMAL ROUTE FINDING (LOWEST RISK & SHORTEST ROUTE)
   Evaluates all available paths and selects the lowest-risk trajectory.
   ------------------------------------------------------------------------- */

all_evacuation_routes(Start, Routes) :-
    findall([Risk, Path], find_path(Start, _Exit, [Start], Path, Risk), Routes).

find_best_route(Start, BestPath, MinRisk) :-
    all_evacuation_routes(Start, Routes),
    Routes \= [],
    sort(Routes, [[MinRisk, BestPath] | _]).

/* -------------------------------------------------------------------------
   7. OUTPUT FORMATTING AND DISPLAY UTILITIES
   ------------------------------------------------------------------------- */

print_path([Node]) :-
    write(Node), nl.
print_path([Node, Next | Rest]) :-
    write(Node), write(' -> '),
    print_path([Next | Rest]).

display_route_details(Start, Path, Risk) :-
    get_last(Path, ExitNode),
    nl,
    write('====================================================='), nl,
    write('            EMERGENCY EVACUATION PLANNER             '), nl,
    write('====================================================='), nl,
    write('Starting Location : '), write(Start), nl,
    write('Destination Exit  : '), write(ExitNode), nl,
    write('Evacuation Route  : '), print_path(Path),
    get_length(Path, HopsCount),
    Steps is HopsCount - 1,
    write('Total Transitions : '), write(Steps), nl,
    write('Cumulative Risk   : '), write(Risk), nl,
    write('Status            : Route Found (Safe to proceed)'), nl,
    write('====================================================='), nl.

/* Main user query predicate */
evacuate(Start) :-
    find_best_route(Start, BestPath, MinRisk),
    !,
    display_route_details(Start, BestPath, MinRisk).

evacuate(Start) :-
    nl,
    write('====================================================='), nl,
    write('            EMERGENCY EVACUATION PLANNER             '), nl,
    write('====================================================='), nl,
    write('Starting Location : '), write(Start), nl,
    write('Status            : NO SAFE ROUTE AVAILABLE!'), nl,
    write('Alert             : All exit corridors are blocked or unsafe.'), nl,
    write('Action            : Shelter in place, seal doors, await rescue.'), nl,
    write('====================================================='), nl.

/* -------------------------------------------------------------------------
   8. THREE SPECIFIED TEST SCENARIOS
   ------------------------------------------------------------------------- */

% Reset dynamic hazards
reset_hazards :-
    retractall(blocked(_, _)),
    retractall(unsafe(_)).

% Test Case 1: Standard Syllabus Scenario
% Corridor 1 -> Staircase 1 is blocked. Start from Room A.
test_case_1 :-
    reset_hazards,
    write('>>> RUNNING TEST CASE 1 (Syllabus Default Scenario)'), nl,
    write('Hazard: Corridor 1 - Staircase 1 is BLOCKED by fire.'), nl,
    assertz(blocked(corridor_1, staircase_1)),
    evacuate(room_a).

% Test Case 2: Multi-Exit & Alternative Routing Challenge
% Corridor 1 - Room B is also blocked. Start from Room A.
% System must intelligently backtrack and take North Wing via Room C -> Exit 3.
test_case_2 :-
    reset_hazards,
    write('>>> RUNNING TEST CASE 2 (Alternative Route via North Wing)'), nl,
    write('Hazards: Corridor 1 - Staircase 1 is BLOCKED.'), nl,
    write('         Corridor 1 - Room B is BLOCKED.'), nl,
    assertz(blocked(corridor_1, staircase_1)),
    assertz(blocked(corridor_1, room_b)),
    evacuate(room_a).

% Test Case 3: Complete Lockdown / No Path Available
% All exits from Room A are blocked.
test_case_3 :-
    reset_hazards,
    write('>>> RUNNING TEST CASE 3 (All Outlets Blocked - Fail Safe)'), nl,
    write('Hazards: Corridor 1 and Corridor 2 are completely engulfed in fire.'), nl,
    assertz(unsafe(corridor_1)),
    assertz(unsafe(corridor_2)),
    evacuate(room_a).

% Automated Test Suite Runner
run_all_tests :-
    nl,
    write('###############################################################'), nl,
    write('#   AI LAB TEST 2 - SET 3: EMERGENCY EVACUATION PLANNER       #'), nl,
    write('#   Student: Paranjay Sharma | Roll No: 64 | Batch: MCA 7th   #'), nl,
    write('###############################################################'), nl, nl,
    test_case_1, nl,
    test_case_2, nl,
    test_case_3, nl,
    write('All 3 test scenarios completed successfully.'), nl.

/* Main entry point for Online Compilers (OnlineGDB, TutorialsPoint, etc.) */
main :-
    run_all_tests,
    halt.

:- initialization(main).

