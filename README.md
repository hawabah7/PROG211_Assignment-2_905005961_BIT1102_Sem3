# Livestock Health & Tracking System (PROG211 – OOP 1)

A simple Python program that tracks the treatments (vaccines, deworming) given to farm animals and shows which animals are due for their next treatment.

## Domain
Agriculture – Livestock Health & Tracking System

## Features / OOP Concepts
| Requirement | Where it is in the code |
|---|---|
| Two classes with attributes & methods | `Treatment`, `Animal` |
| Object creation & interaction | `Animal.give_treatment(treatment, date)` uses a `Treatment` object |
| One data structure | List `herd` that stores `Animal` objects |
| Add / display functions | `add_animal()`, `display_animals()` |
| Instance methods | `give_treatment()`, `update_weight()`, `is_due()`, `display_info()` |
| Class methods | `get_total_animals()`, `from_string()` |
| Static method | `is_valid_tag()` |
| Tuples (bonus) | `Animal.SPECIES` and the `(treatment, date)` history entries |

## How it aligns with Digital Public Goods (DPG) standards
- **Open-source:** the full code is public on GitHub.
- **Inclusive & accessible:** plain-text output and simple wording; works offline on any computer with Python.
- **Privacy-respecting:** no farmer names, phone numbers or locations are stored – only an animal tag (e.g. `A001`), species and weight.
- **Modular & reusable:** each class and function does one job and can be reused for other tracking systems.

## How to run
```
python livestock_tracker.py
```
Requires Python 3.8+. No extra libraries.

## Example output
See `sample_output.txt`.

## Author
<HAWABAH> – Student ID <905005961> – Limkokwing University, Sierra Leone
