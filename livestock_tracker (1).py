"""
Livestock Health & Tracking System - PROG211 Object-Oriented Programming 1
Domain: Agriculture

DPG alignment (see README.md):
- Open source: hosted on GitHub
- Inclusive/accessible: plain-text output, simple wording
- Privacy-respecting: NO farmer or owner details; only an animal tag ID
- Modular and reusable: classes and functions are independent
"""

from datetime import date, timedelta


class Treatment:
    """Task 1: a type of treatment, e.g. a vaccine or deworming (class #1)."""

    def __init__(self, name, interval_days):
        self.name = name                    # attribute
        self.interval_days = interval_days  # days before it is due again

    def display_info(self):
        print(f"Treatment: {self.name} | Repeat every {self.interval_days} days")


class Animal:
    """Task 1: an animal on the farm, identified only by a tag (class #2)."""

    SPECIES = ("Cattle", "Goat", "Sheep", "Pig", "Chicken")  # tuple (bonus)
    total_animals = 0  # class attribute shared by all objects

    def __init__(self, tag_id, species, weight_kg):
        self.tag_id = tag_id          # anonymous tag, no owner data
        self.species = species
        self.weight_kg = weight_kg
        self.history = []             # list of (treatment name, date) tuples

    # ---------- Task 3: instance methods ----------
    def give_treatment(self, treatment, on_date):
        """Record a Treatment object given on a date (object interaction)."""
        self.history.append((treatment.name, on_date))
        print(f"  {self.tag_id}: {treatment.name} given on {on_date}.")

    def update_weight(self, new_weight):
        print(f"  {self.tag_id}: weight {self.weight_kg}kg -> {new_weight}kg.")
        self.weight_kg = new_weight

    def is_due(self, treatment, today):
        """True if the treatment was never given or its interval has passed."""
        dates = [d for name, d in self.history if name == treatment.name]
        if not dates:
            return True
        return today >= max(dates) + timedelta(days=treatment.interval_days)

    def display_info(self):
        last = "none yet"
        if self.history:
            name, when = self.history[-1]   # unpack the tuple
            last = f"{name} on {when}"
        print(f"Tag: {self.tag_id} | {self.species} | {self.weight_kg}kg | "
              f"Treatments: {len(self.history)} | Last: {last}")

    # ---------- Task 3: class methods ----------
    @classmethod
    def get_total_animals(cls):
        return cls.total_animals

    @classmethod
    def from_string(cls, text):
        """Create an Animal from 'tag,species,weight' e.g. 'A002,Goat,25'."""
        tag, species, weight = text.split(",")
        return cls(tag.strip(), species.strip(), float(weight))

    # ---------- static method ----------
    @staticmethod
    def is_valid_tag(tag_id):
        """Tag must look like A001 (letter A + 3 digits)."""
        return (len(tag_id) == 4 and tag_id[0] == "A"
                and tag_id[1:].isdigit())


# ---------- Task 2: ONE data structure (a list of Animal objects) ----------
def add_animal(herd, animal):
    if not Animal.is_valid_tag(animal.tag_id):
        print(f"Invalid tag: {animal.tag_id}")
        return
    if animal.species not in Animal.SPECIES:
        print(f"Unknown species: {animal.species}")
        return
    for existing in herd:                       # loop through the list
        if existing.tag_id == animal.tag_id:
            print(f"Tag {animal.tag_id} already exists.")
            return
    herd.append(animal)
    Animal.total_animals += 1                   # count only accepted animals
    print(f"Added animal {animal.tag_id}.")


def display_animals(herd):
    print("\n--- Herd Records ---")
    if not herd:
        print("No animals.")
    for animal in herd:
        animal.display_info()


def show_due(herd, treatment, today):
    print(f"\n--- Animals due for {treatment.name} on {today} ---")
    for animal in herd:
        if animal.is_due(treatment, today):
            print(f"  {animal.tag_id} ({animal.species})")


def main():
    herd = []  # list that stores all Animal objects

    deworm = Treatment("Deworming", 90)
    vaccine = Treatment("Anthrax Vaccine", 365)

    print("=== Treatments ===")
    for t in (deworm, vaccine):
        t.display_info()

    print("\n=== Adding Animals ===")
    add_animal(herd, Animal("A001", "Cattle", 320.5))
    add_animal(herd, Animal.from_string("A002, Goat, 25"))  # class method
    add_animal(herd, Animal("A001", "Sheep", 30))            # duplicate
    add_animal(herd, Animal("B7", "Goat", 20))               # invalid tag
    add_animal(herd, Animal("A003", "Dragon", 50))           # bad species

    print("\n=== Recording Treatments ===")
    herd[0].give_treatment(deworm, date(2026, 6, 1))
    herd[0].give_treatment(vaccine, date(2026, 6, 1))
    herd[1].give_treatment(deworm, date(2026, 9, 1))
    herd[1].update_weight(27.5)

    display_animals(herd)
    show_due(herd, deworm, date(2026, 10, 24))

    print(f"\nTotal animals registered: {Animal.get_total_animals()}")
    print("Allowed species (tuple):", Animal.SPECIES)


if __name__ == "__main__":
    main()
