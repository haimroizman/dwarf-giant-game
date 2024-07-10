import random
from multiprocessing import Pool, Manager
from typing import List, Dict, Tuple
from employee import Employee
from utils import validate_and_clean_input


def process_chunk(input_chunk: List[Dict[str, str]]) -> List[Tuple[str, str]]:
    employees = validate_and_clean_input(input_chunk)
    pairs = generate_circular_pairs(employees)
    return pairs


def generate_circular_pairs(employees: List[Employee]) -> List[Tuple[str, str]]:
    random.shuffle(employees)
    pairs = []
    n = len(employees)
    for i in range(n):
        dwarf = employees[i]
        giant = employees[(i + 1) % n]
        pairs.append((dwarf.name, giant.name))
    return pairs


def multiprocess_dwarf_giant_game(input_data: List[Dict[str, str]], num_processes: int) -> List[Tuple[str, str]]:
    # Split input data into chunks
    chunk_size = max(1, len(input_data) // num_processes)
    chunks = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]


    with Manager() as manager:
        with Pool(processes=num_processes) as pool:
            result_chunks = pool.map(process_chunk, chunks)

        all_pairs = [pair for chunk in result_chunks for pair in chunk]
        unique_pairs = list(set(all_pairs))
        return unique_pairs
