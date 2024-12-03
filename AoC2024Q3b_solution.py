import re
import logging
from typing import List, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def parse_corrupted_memory(memory: str) -> int:
    """
    Parse the corrupted memory and calculate the sum of enabled mul instructions.
    
    Args:
        memory (str): The entire memory content to parse.
    
    Returns:
        int: Sum of valid enabled multiplication results.
    """
    # Regex patterns
    mul_pattern = r'mul\((\d+),(\d+)\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Initialize state
    enabled = True
    total_sum = 0
    
    # Find all tokens in the memory
    # Use a more comprehensive regex to split tokens
    tokens = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', memory)
    
    for token in tokens:
        # Check for do() or don't() instructions
        if re.match(do_pattern, token):
            enabled = True
            logger.debug(f"Enabled: {token}")
        elif re.match(dont_pattern, token):
            enabled = False
            logger.debug(f"Disabled: {token}")
        
        # Check for mul instruction
        mul_match = re.match(mul_pattern, token)
        if mul_match and enabled:
            x = int(mul_match.group(1))
            y = int(mul_match.group(2))
            result = x * y
            total_sum += result
            logger.debug(f"Processed: {token} = {result} (Enabled)")
    
    return total_sum

def parse_from_file(file_path: str) -> Optional[int]:
    """
    Read the memory from a file and parse it.
    
    Args:
        file_path (str): Path to the file containing memory instructions.
    
    Returns:
        Optional[int]: Sum of valid multiplication results, or None if file cannot be processed.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            memory = file.read().strip()
        
        if not memory:
            logger.warning(f"File at {file_path} is empty.")
            return None
        
        total = parse_corrupted_memory(memory)
        logger.info(f"Total sum of multiplications: {total}")
        return total
    
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None
    except Exception as e:
        logger.error(f"Error processing file: {e}")
        return None

def main():
    """
    Main function to demonstrate usage of the parsing function.
    """
    file_path = 'AoC2024Q3a_input.txt'  
    
    result = parse_from_file(file_path)
    
    if result is not None:
        print(f"Sum of valid multiplications: {result}")
    else:
        print("Failed to process the file.")

if __name__ == "__main__":
    main()
