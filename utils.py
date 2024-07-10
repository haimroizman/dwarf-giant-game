# utils.py

import random
from typing import List, Dict, Tuple
from employee import Employee

def validate_and_clean_input(employees: List[Dict[str, str]]) -> List[Employee]:
    unique_employees = set()
    for emp in employees:
        employee = Employee(emp['department'], emp['name'], emp['age'])
        unique_employees.add(employee)
    return list(unique_employees)

# I've changed the function name to generate_circular_pairs -> this function handles both odd and even number of employees
# This ensures that every employy is both a dwarf and a giant exactly once
def generate_circular_pairs(employees: List[Employee]) -> List[Tuple[str, str]]:
    random.shuffle(employees)
    pairs = []
    n = len(employees)
    for i in range(n):
        dwarf = employees[i]
        giant = employees[(i + 1) % n]  # Circular pairing
        pairs.append((dwarf.name, giant.name))
    return pairs
