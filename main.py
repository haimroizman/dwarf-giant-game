import json
from utils import validate_and_clean_input, generate_circular_pairs
from typing import List, Dict, Tuple
from multiprocess_manager import multiprocess_dwarf_giant_game


# def dwarf_giant_game(input_data: List[Dict[str, str]]) -> List[Tuple[str, str]]:
#     employees = validate_and_clean_input(input_data)
#     pairs = generate_unique_pairs(employees)
#     return pairs


if __name__ == "__main__":
    with open('data.json') as f:
        input_data = json.load(f)
    process_number = 4
    pairs = multiprocess_dwarf_giant_game(input_data, process_number)
    print(pairs)
    # print('______________________________' * 10)
    # for dwarf, giant in pairs:
    #     print(f"Dwarf: {dwarf}, Giant: {giant}")
