r"""
Task 11: Demonstrate Family Relationships (Knowledge Base & Inference)
AI Lab Coursework - Knowledge Representation & First-Order Logic

Prolog Equivalent:
    % Facts
    parent(pam, bob).  parent(tom, bob).  parent(tom, liz).
    parent(bob, ann).  parent(bob, pat).  parent(pat, jim).
    male(tom).  male(bob).  male(jim).
    female(pam). female(liz). female(ann). female(pat).

    % Rules
    father(X, Y)       :- parent(X, Y), male(X).
    mother(X, Y)       :- parent(X, Y), female(X).
    grandparent(X, Z)  :- parent(X, Y), parent(Y, Z).
    sibling(X, Y)      :- parent(P, X), parent(P, Y), X \= Y.
    brother(X, Y)      :- sibling(X, Y), male(X).
    sister(X, Y)       :- sibling(X, Y), female(X).
    ancestor(X, Y)     :- parent(X, Y).
    ancestor(X, Y)     :- parent(X, Z), ancestor(Z, Y).

Description:
    Demonstrates knowledge representation of a family tree using a dedicated
    Knowledge Base in Python, inferring relationships using rule-based reasoning.
"""

from typing import Dict, List, Set


class FamilyKnowledgeBase:
    """Stores genealogical facts and evaluates logical relationship queries."""

    def __init__(self):
        # child -> set of parents
        self.parents: Dict[str, Set[str]] = {}
        # parent -> set of children
        self.children: Dict[str, Set[str]] = {}
        # person -> 'male' / 'female'
        self.gender: Dict[str, str] = {}

    def add_parent(self, parent: str, child: str):
        """Asserts fact: parent(parent, child)."""
        self.parents.setdefault(child, set()).add(parent)
        self.children.setdefault(parent, set()).add(child)

    def set_gender(self, person: str, gender: str):
        """Asserts fact: male(person) or female(person)."""
        self.gender[person] = gender.lower()

    # Rule Inferences
    def get_parents(self, person: str) -> Set[str]:
        return self.parents.get(person, set())

    def get_children(self, person: str) -> Set[str]:
        return self.children.get(person, set())

    def get_father(self, person: str) -> Set[str]:
        """father(X, Y) :- parent(X, Y), male(X)."""
        return {p for p in self.get_parents(person) if self.gender.get(p) == "male"}

    def get_mother(self, person: str) -> Set[str]:
        """mother(X, Y) :- parent(X, Y), female(X)."""
        return {p for p in self.get_parents(person) if self.gender.get(p) == "female"}

    def get_grandparents(self, person: str) -> Set[str]:
        """grandparent(X, Z) :- parent(X, Y), parent(Y, Z)."""
        grandparents = set()
        for p in self.get_parents(person):
            grandparents.update(self.get_parents(p))
        return grandparents

    def get_siblings(self, person: str) -> Set[str]:
        r"""sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y."""
        siblings = set()
        for p in self.get_parents(person):
            for child in self.get_children(p):
                if child != person:
                    siblings.add(child)
        return siblings

    def get_brothers(self, person: str) -> Set[str]:
        """brother(X, Y) :- sibling(X, Y), male(X)."""
        return {s for s in self.get_siblings(person) if self.gender.get(s) == "male"}

    def get_sisters(self, person: str) -> Set[str]:
        """sister(X, Y) :- sibling(X, Y), female(X)."""
        return {s for s in self.get_siblings(person) if self.gender.get(s) == "female"}

    def get_ancestors(self, person: str) -> Set[str]:
        """
        Recursive ancestor rule:
        ancestor(X, Y) :- parent(X, Y).
        ancestor(X, Y) :- parent(Z, Y), ancestor(X, Z).
        """
        ancestors = set()
        for p in self.get_parents(person):
            ancestors.add(p)
            ancestors.update(self.get_ancestors(p))
        return ancestors


def build_sample_family_tree() -> FamilyKnowledgeBase:
    kb = FamilyKnowledgeBase()

    # Define Gender
    kb.set_gender("tom", "male")
    kb.set_gender("pam", "female")
    kb.set_gender("bob", "male")
    kb.set_gender("liz", "female")
    kb.set_gender("pat", "female")
    kb.set_gender("ann", "female")
    kb.set_gender("jim", "male")

    # Define Parent relationships
    kb.add_parent("pam", "bob")
    kb.add_parent("tom", "bob")
    kb.add_parent("tom", "liz")
    kb.add_parent("bob", "ann")
    kb.add_parent("bob", "pat")
    kb.add_parent("pat", "jim")

    return kb


def main():
    print("=" * 60)
    print("Task 11: Family Relationships Knowledge Base")
    print("=" * 60)

    kb = build_sample_family_tree()

    queries = ["bob", "pat", "ann", "jim", "liz"]
    for person in queries:
        print(f"\n--- Inferences for '{person.capitalize()}' ---")
        print(f"  Parents      : {sorted(kb.get_parents(person))}")
        print(f"  Father       : {sorted(kb.get_father(person))}")
        print(f"  Mother       : {sorted(kb.get_mother(person))}")
        print(f"  Children     : {sorted(kb.get_children(person))}")
        print(f"  Siblings     : {sorted(kb.get_siblings(person))}")
        print(f"  Brothers     : {sorted(kb.get_brothers(person))}")
        print(f"  Sisters      : {sorted(kb.get_sisters(person))}")
        print(f"  Grandparents : {sorted(kb.get_grandparents(person))}")
        print(f"  Ancestors    : {sorted(kb.get_ancestors(person))}")


if __name__ == "__main__":
    main()
