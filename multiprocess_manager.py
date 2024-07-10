import random
from multiprocessing import Pool, Manager
from typing import List, Dict, Tuple
from employee import Employee
from utils import validate_and_clean_input, generate_circular_pairs


def process_chunk(input_chunk: List[Dict[str, str]]) -> List[Employee]:
    return validate_and_clean_input(input_chunk)


def multiprocess_dwarf_giant_game(input_data: List[Dict[str, str]], num_processes: int) -> List[Tuple[str, str]]:
    # Split input data into chunks
    chunk_size = max(1, len(input_data) // num_processes)
    chunks = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]

    # Use Manager to handle shared memory
    with Manager() as manager:
        with Pool(processes=num_processes) as pool:
            result_chunks = pool.map(process_chunk, chunks)

        # Flatten list of lists
        all_employees = [employee for chunk in result_chunks for employee in chunk]
        unique_employees = list(set(all_employees))  # Remove duplicates

        # Generate circular pairs
        pairs = generate_circular_pairs(unique_employees)
        return pairs
