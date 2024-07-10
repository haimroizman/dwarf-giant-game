import random
from typing import List, Dict, Tuple


# I tried to make it simple as much as I can, so this is why I've added the functon eq and hash to make it hashable,
# So I can use it in a set to remove the duplicates, and I've added the __eq__ to compare the objects in the set
class Employee:
    def __init__(self, department: str, name: str, age: int):
        self.department = department
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.department == other.department and self.name == other.name and self.age == other.age
        return False

    def __hash__(self):
        return hash((self.department, self.name, self.age))
