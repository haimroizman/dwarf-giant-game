import random
from multiprocessing import Pool, Manager
from typing import List, Dict, Tuple
from employee import Employee


def process_chunk(input_chunk: List[Dict[str, str]]) -> List[Employee]:
    # Clean the input chunk and remove duplicates
    unique_employees = set()
    for emp in input_chunk:
        employee = Employee(emp['department'], emp['name'], emp['age'])
        unique_employees.add(employee)
    return list(unique_employees)


def generate_circular_pairs(employees: List[Employee]) -> List[Tuple[str, str]]:
    random.shuffle(employees)
    pairs = []
    n = len(employees)
    for i in range(n):
        dwarf = employees[i]
        giant = employees[(i + 1) % n]  # Circular pairing
        pairs.append((dwarf.name, giant.name))
    return pairs


def multiprocess_dwarf_giant_game(input_data: List[Dict[str, str]], num_processes: int) -> List[Tuple[str, str]]:
    # Split input data into chunks
    chunk_size = max(1, len(input_data) // num_processes)
    chunks = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]

    with Manager() as manager:
        managed_employees = manager.list()

        with Pool(processes=num_processes) as pool:
            result_chunks = pool.map(process_chunk, chunks)

        # Combine the results from all chunks into a managed list
        for chunk in result_chunks:
            managed_employees.extend(chunk)

        # Remove duplicates
        unique_employees = list(set(managed_employees))

        # Generate circular pairs
        pairs = generate_circular_pairs(unique_employees)
        return pairs
