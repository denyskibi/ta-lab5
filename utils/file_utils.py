# Standard Libraries
from typing import List


def load_numbers_from_txt_file(file_path: str) -> List[int]:
    numbers: List[int] = []

    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]  # cut excluding first line

        for line in lines:
            number_str = line.strip()
            number_int = int(number_str)
            numbers.append(number_int)

    return numbers
