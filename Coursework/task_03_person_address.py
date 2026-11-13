"""
Task 3: Read the Address of a Person Using a Compound Variable/Dictionary Structure
AI Lab Coursework - Compound Data Structures

Prolog Equivalent:
    % Compound term structure in Prolog:
    person(name('Paranjay', 'Sharma'),
           address(street('42 Knowledge Park'), city('Indore'), state('Madhya Pradesh'), zip('452001')),
           contact(phone('9876543210'), email('paranjay@example.com'))).

    get_address(person(_, Address, _), Address).
    get_city(person(_, address(_, city(C), _, _), _), C).

Description:
    Demonstrates handling compound terms/structures using Python dictionaries,
    simulating Prolog functors and nested compound terms.
"""

from typing import Any, Dict


def create_person_record(
    first_name: str,
    last_name: str,
    street: str,
    city: str,
    state: str,
    zip_code: str,
    country: str = "India",
    phone: str = "",
    email: str = ""
) -> Dict[str, Any]:
    """
    Constructs a compound dictionary structure representing a Person,
    mirroring a Prolog nested functor person(name(...), address(...), contact(...)).
    """
    return {
        "name": {
            "first_name": first_name,
            "last_name": last_name,
            "full_name": f"{first_name} {last_name}",
        },
        "address": {
            "street": street,
            "city": city,
            "state": state,
            "postal_code": zip_code,
            "country": country,
        },
        "contact": {
            "phone": phone,
            "email": email,
        },
    }


def read_full_address(person: Dict[str, Any]) -> str:
    """Reads and formats the compound address structure of a person."""
    addr = person.get("address", {})
    return (
        f"{addr.get('street')}, {addr.get('city')}, "
        f"{addr.get('state')} - {addr.get('postal_code')}, {addr.get('country')}"
    )


def read_address_field(person: Dict[str, Any], field: str) -> str:
    """Simulates Prolog unification by extracting a specific sub-field from address."""
    addr = person.get("address", {})
    return addr.get(field, "Field Not Found")


def display_person_details(person: Dict[str, Any]) -> None:
    """Prints person profile and nested compound attributes."""
    name = person["name"]["full_name"]
    print(f"Profile: {name}")
    print(f"  Street      : {person['address']['street']}")
    print(f"  City        : {person['address']['city']}")
    print(f"  State       : {person['address']['state']}")
    print(f"  Postal Code : {person['address']['postal_code']}")
    print(f"  Country     : {person['address']['country']}")
    print(f"  Phone       : {person['contact']['phone']}")
    print(f"  Email       : {person['contact']['email']}")


def main():
    print("=" * 60)
    print("Task 3: Person Address using Compound Dictionary Structure")
    print("=" * 60)

    # Creating sample compound person records
    person1 = create_person_record(
        first_name="Paranjay",
        last_name="Sharma",
        street="101 Scholar Avenue, Sector 5",
        city="Indore",
        state="Madhya Pradesh",
        zip_code="452001",
        phone="+91-9876543210",
        email="paranjay.sharma@example.edu"
    )

    person2 = create_person_record(
        first_name="Aarav",
        last_name="Patel",
        street="24 Tech Park Road, Whitefield",
        city="Bengaluru",
        state="Karnataka",
        zip_code="560066",
        phone="+91-9123456780",
        email="aarav.patel@example.com"
    )

    print("\n[Record 1]")
    display_person_details(person1)

    print("\n[Record 2]")
    display_person_details(person2)

    print("\n[Targeted Field Extraction (Unification)]")
    print(f"Person 1 Complete Address: {read_full_address(person1)}")
    print(f"Person 1 City            : {read_address_field(person1, 'city')}")
    print(f"Person 1 Postal Code     : {read_address_field(person1, 'postal_code')}")


if __name__ == "__main__":
    main()
