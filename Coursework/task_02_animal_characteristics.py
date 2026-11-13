"""
Task 2: Categorize Animal Characteristics
AI Lab Coursework - Knowledge Representation & Rule-Based Categorization

Prolog Equivalent:
    mammal(X) :- warm_blooded(X), has_fur(X), gives_milk(X).
    bird(X)   :- warm_blooded(X), has_feathers(X), lays_eggs(X).
    fish(X)   :- cold_blooded(X), has_scales(X), breathes_gills(X).
    reptile(X):- cold_blooded(X), has_scales(X), lays_eggs(X).

Description:
    Demonstrates knowledge representation using a rule-based expert system in Python.
    Facts about animals and inference rules are used to deduce an animal's category
    and traits, simulating Prolog's resolution engine.
"""

from typing import Dict, List, Set


# Knowledge Base: Facts about animals and their biological traits
ANIMAL_FACTS: Dict[str, Set[str]] = {
    "dog": {"warm_blooded", "has_fur", "gives_milk", "canine", "carnivore"},
    "cat": {"warm_blooded", "has_fur", "gives_milk", "feline", "carnivore"},
    "sparrow": {"warm_blooded", "has_feathers", "lays_eggs", "can_fly", "beak"},
    "penguin": {"warm_blooded", "has_feathers", "lays_eggs", "can_swim", "flightless"},
    "salmon": {"cold_blooded", "has_scales", "breathes_gills", "lives_in_water"},
    "crocodile": {"cold_blooded", "has_scales", "lays_eggs", "carnivore", "semi_aquatic"},
    "frog": {"cold_blooded", "amphibious", "lays_eggs", "smooth_skin"},
    "elephant": {"warm_blooded", "has_skin", "gives_milk", "herbivore", "large_ears"},
}

# Classification Rules (Prolog clauses modeled as predicate logic)
RULES = {
    "Mammal": lambda traits: {"warm_blooded", "gives_milk"}.issubset(traits),
    "Bird": lambda traits: {"warm_blooded", "has_feathers", "lays_eggs"}.issubset(traits),
    "Fish": lambda traits: {"cold_blooded", "has_scales", "breathes_gills"}.issubset(traits),
    "Reptile": lambda traits: {"cold_blooded", "has_scales", "lays_eggs"}.issubset(traits),
    "Amphibian": lambda traits: {"cold_blooded", "amphibious", "lays_eggs"}.issubset(traits),
}


def categorize_animal(animal_name: str) -> List[str]:
    """Infers categories for a known animal based on its traits."""
    traits = ANIMAL_FACTS.get(animal_name.lower())
    if traits is None:
        return ["Unknown Animal"]

    categories = [cat for cat, rule in RULES.items() if rule(traits)]
    return categories if categories else ["Unclassified"]


def infer_category_from_traits(traits: Set[str]) -> List[str]:
    """Classifies an unknown creature given a set of observed traits."""
    categories = [cat for cat, rule in RULES.items() if rule(traits)]
    return categories if categories else ["Unknown"]


def main():
    print("=" * 60)
    print("Task 2: Categorize Animal Characteristics (Knowledge Base)")
    print("=" * 60)

    print("\n[1] Classifying known animals in the knowledge base:")
    for animal, traits in ANIMAL_FACTS.items():
        categories = categorize_animal(animal)
        print(f"  * {animal.capitalize():12} -> Category: {', '.join(categories):10} | Traits: {sorted(traits)}")

    print("\n[2] Inference from arbitrary observed traits (Prolog Query Simulation):")
    sample_observations = [
        ("Specimen A", {"warm_blooded", "gives_milk", "has_fur"}),
        ("Specimen B", {"warm_blooded", "has_feathers", "lays_eggs", "can_fly"}),
        ("Specimen C", {"cold_blooded", "has_scales", "breathes_gills"}),
    ]

    for label, obs in sample_observations:
        result = infer_category_from_traits(obs)
        print(f"  * {label}: Traits {obs} -> Inferred as: {', '.join(result)}")


if __name__ == "__main__":
    main()

