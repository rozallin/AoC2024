def read_locations_from_file(file_path):
    """
    Read two lists of location IDs from a text file.

    :param file_path: Path to the text file.
    :return: Two lists of location IDs.
    """
    locations_a = []
    locations_b = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split("   ")  # Split on three spaces
                if len(parts) != 2:
                    raise ValueError(f"Invalid line format: {line}")
                loc_a, loc_b = map(int, parts)  # Convert the values to integers
                locations_a.append(loc_a)
                locations_b.append(loc_b)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError as e:
        print(f"Error: {e}")
    return locations_a, locations_b


def calculate_similarity_score(locations_a, locations_b):
    """
    Calculate the similarity score between two lists of locations.

    :param locations_a: List of location IDs from the left list.
    :param locations_b: List of location IDs from the right list.
    :return: Total similarity score.
    """
    # Count occurrences of each number in the right list
    right_list_counts = {}
    for loc in locations_b:
        right_list_counts[loc] = right_list_counts.get(loc, 0) + 1

    # Calculate similarity score
    total_similarity_score = 0
    for loc in locations_a:
        # Count how many times this number appears in the right list
        count = right_list_counts.get(loc, 0)
        # Multiply the number by its count and add to total score
        total_similarity_score += loc * count

    return total_similarity_score


# Main execution block
file_path = "AoC2024Q1a_input.txt"

# Read locations
locations_a, locations_b = read_locations_from_file(file_path)

# Calculate and print the similarity score
similarity_score = calculate_similarity_score(locations_a, locations_b)
print(f"Similarity Score: {similarity_score}")