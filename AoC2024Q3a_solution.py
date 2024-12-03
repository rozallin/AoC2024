import re
import logging
from typing import List, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Constants
VALID_MUL_PATTERN = r"mul\((\d{1,3}),(\d{1,3})\)"

def parse_mul_instructions(memory: str) -> List[Tuple[int, int]]:
    """
    Extract valid mul(X,Y) instructions from the memory string.
    
    Args:
        memory (str): The entire memory content to parse.
    
    Returns:
        List[Tuple[int, int]]: A list of tuples containing valid (X, Y) pairs.
    """
    # Extract valid multiplication instructions
    matches = re.findall(VALID_MUL_PATTERN, memory)
    logger.debug(f"Found {len(matches)} raw matches: {matches}")

    # Convert matches to integers and return
    valid_matches = [(int(x), int(y)) for x, y in matches]
    return valid_matches

def parse_and_calculate_sum_from_file(file_path: str) -> Optional[int]:
    """
    Parse the corrupted memory from a file and calculate the sum of valid mul(X,Y) instructions.
    
    Args:
        file_path (str): Path to the file containing memory instructions.
    
    Returns:
        Optional[int]: Sum of valid multiplication results, or None if the file cannot be processed.
    """
    try:
        # Read file content
        with open(file_path, 'r', encoding='utf-8') as file:
            memory = file.read()
        
        if not memory.strip():
            logger.warning(f"File at {file_path} is empty.")
            return None

        # Extract and process instructions
        mul_instructions = parse_mul_instructions(memory)

        if not mul_instructions:
            logger.warning("No valid multiplication instructions found.")
            return None

        # Calculate the total sum
        total = sum(x * y for x, y in mul_instructions)
        
        # Log results
        logger.info(f"Processed {len(mul_instructions)} valid multiplication instructions.")
        logger.info(f"Total sum of multiplications: {total}")

        return total

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None
    except PermissionError:
        logger.error(f"Permission denied when accessing: {file_path}")
        return None
    except IOError as e:
        logger.error(f"IO error occurred while reading {file_path}: {e}")
        return None

def main():
    """
    Main function to demonstrate usage of the parsing function.
    """
    # File path to process
    file_path = 'AoC2024Q3a_input.txt'
    
    result = parse_and_calculate_sum_from_file(file_path)
    
    if result is not None:
        print(f"Sum of valid mul instructions: {result}")
    else:
        print("No valid instructions were processed or the file could not be read.")

if __name__ == "__main__":
    main()
