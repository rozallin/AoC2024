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


def calculate_total_distance(locations_a, locations_b):
    """
    Calculate the total distance between paired locations.

    Pair the locations by sorting both lists and then calculating 
    the absolute distance between corresponding pairs.

    :param locations_a: List of location IDs from the left list.
    :param locations_b: List of location IDs from the right list.
    :return: Total distance between paired locations.
    """
    # Sort both lists
    sorted_a = sorted(locations_a)
    sorted_b = sorted(locations_b)

    # Verify lists have same length
    if len(sorted_a) != len(sorted_b):
        raise ValueError("Both location lists must have the same length.")

    # Calculate distances between paired locations
    total_distance = 0
    for loc_a, loc_b in zip(sorted_a, sorted_b):
        # Calculate absolute distance between paired locations
        distance = abs(loc_a - loc_b)
        total_distance += distance

    return total_distance


# Main execution block
file_path = "AoC2024Q1a_input.txt"

# Read locations
locations_a, locations_b = read_locations_from_file(file_path)

try:
    total = calculate_total_distance(locations_a, locations_b)
    print(f"Total distance: {total}")
except ValueError as e:
    print(f"Error: {e}")