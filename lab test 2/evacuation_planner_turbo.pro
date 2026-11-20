/* =========================================================================
   EMERGENCY EVACUATION PLANNER (TURBO PROLOG VERSION)
   Lab Test 2 - Set 3 (Roll No: 64, Student: Paranjay Sharma)
   Course: MCA 7th Sem - Artificial Intelligence Laboratory
   Syntax: Borland Turbo Prolog 2.0 (DOSBox Compatible)
   ========================================================================= */

DOMAINS
    loc = symbol
    loclist = loc*
    integer_val = integer

DATABASE - building_hazards
    blocked(loc, loc)
    unsafe(loc)

PREDICATES
    nondeterm connection(loc, loc, integer_val)
    nondeterm adjacent(loc, loc, integer_val)
    nondeterm is_blocked(loc, loc)
    nondeterm safe_transition(loc, loc, integer_val)
    nondeterm is_exit(loc)
    nondeterm list_member(loc, loclist)
    nondeterm find_path(loc, loc, loclist, loclist, integer_val)
    evacuate(loc)
    print_path(loclist)
    reset_hazards
    test_1
    test_2
    test_3
    run_all_tests

CLAUSES
    /* -------------------------------------------------------------
       KNOWLEDGE BASE: GRAPH CONNECTIONS AND RISK WEIGHTS
       ------------------------------------------------------------- */
    is_exit(exit_1).
    is_exit(exit_2).
    is_exit(exit_3).

    % Primary floor connections
    connection(room_a, corridor_1, 1).
    connection(corridor_1, staircase_1, 2).
    connection(corridor_1, room_b, 1).
    connection(room_b, exit_2, 1).
    connection(staircase_1, exit_1, 1).

    % North and South wing bypass connections
    connection(room_a, corridor_2, 2).
    connection(corridor_2, room_c, 1).
    connection(room_c, staircase_2, 1).
    connection(staircase_2, exit_3, 1).
    connection(room_b, corridor_3, 1).
    connection(corridor_3, staircase_1, 2).
    connection(corridor_3, exit_2, 2).

    /* -------------------------------------------------------------
       SYMMETRIC GRAPH TRANSITIONS & SAFETY RULES
       ------------------------------------------------------------- */
    adjacent(X, Y, Cost) :- connection(X, Y, Cost).
    adjacent(X, Y, Cost) :- connection(Y, X, Cost).

    is_blocked(X, Y) :- blocked(X, Y).
    is_blocked(X, Y) :- blocked(Y, X).

    safe_transition(From, To, Cost) :-
        adjacent(From, To, Cost),
        not(is_blocked(From, To)),
        not(unsafe(To)).

    /* -------------------------------------------------------------
       LIST UTILITIES
       ------------------------------------------------------------- */
    list_member(X, [X | _]) :- !.
    list_member(X, [_ | Tail]) :- list_member(X, Tail).

    print_path([Node]) :-
        write(Node), nl, !.
    print_path([Node | Rest]) :-
        write(Node), write(" -> "),
        print_path(Rest).

    /* -------------------------------------------------------------
       PATHFINDING ALGORITHM (DEPTH FIRST SEARCH WITH CYCLE CHECKS)
       ------------------------------------------------------------- */
    find_path(Current, Current, _, [Current], 0) :-
        is_exit(Current), !.

    find_path(Current, Goal, Visited, [Current | PathTail], TotalCost) :-
        safe_transition(Current, Next, StepCost),
        not(list_member(Next, Visited)),
        find_path(Next, Goal, [Next | Visited], PathTail, SubCost),
        TotalCost = StepCost + SubCost.

    /* -------------------------------------------------------------
       EVACUATION CONTROLLER & OUTPUT FORMATTER
       ------------------------------------------------------------- */
    evacuate(Start) :-
        find_path(Start, ExitNode, [Start], Path, Risk),
        is_exit(ExitNode),
        write("\n=====================================================\n"),
        write("            EMERGENCY EVACUATION PLANNER             \n"),
        write("=====================================================\n"),
        write("Starting Location : "), write(Start), nl,
        write("Destination Exit  : "), write(ExitNode), nl,
        write("Evacuation Route  : "), print_path(Path),
        write("Cumulative Risk   : "), write(Risk), nl,
        write("Status            : Route Found (Safe to proceed)\n"),
        write("=====================================================\n"),
        !.

    evacuate(Start) :-
        write("\n=====================================================\n"),
        write("            EMERGENCY EVACUATION PLANNER             \n"),
        write("=====================================================\n"),
        write("Starting Location : "), write(Start), nl,
        write("Status            : NO SAFE ROUTE AVAILABLE!\n"),
        write("Alert             : All exit corridors are blocked/unsafe.\n"),
        write("Action            : Shelter in place, await rescue.\n"),
        write("=====================================================\n").

    /* -------------------------------------------------------------
       TEST SCENARIOS
       ------------------------------------------------------------- */
    reset_hazards :-
        retractall(blocked(_, _)),
        retractall(unsafe(_)).

    test_1 :-
        reset_hazards,
        write(">>> TEST CASE 1: Standard Corridor 1 - Staircase 1 Blocked\n"),
        assertz(blocked(corridor_1, staircase_1)),
        evacuate(room_a).

    test_2 :-
        reset_hazards,
        write(">>> TEST CASE 2: Corridor 1 Blocked completely (Route via North Wing)\n"),
        assertz(blocked(corridor_1, staircase_1)),
        assertz(blocked(corridor_1, room_b)),
        evacuate(room_a).

    test_3 :-
        reset_hazards,
        write(">>> TEST CASE 3: Total Isolation (All Outlets from Room A Unsafe)\n"),
        assertz(unsafe(corridor_1)),
        assertz(unsafe(corridor_2)),
        evacuate(room_a).

    run_all_tests :-
        test_1,
        test_2,
        test_3.

GOAL
    run_all_tests.
