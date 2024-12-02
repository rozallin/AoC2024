def is_safe_report(report):
    """Check if a single report is safe."""
    levels = list(map(int, report.split()))
    
    # Check if the report is monotonically increasing or decreasing
    increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

    # If neither increasing nor decreasing, it's unsafe
    if not (increasing or decreasing):
        return False

    # Check the difference between adjacent levels is between 1 and 3
    valid_differences = all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))

    return valid_differences

def count_safe_reports(file_path):
    """Count the number of safe reports in a file."""
    safe_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            if is_safe_report(line.strip()):
                safe_count += 1

    return safe_count

# Example usage:
file_path = 'AoC2024Q2a_input.txt'  # Replace with your file's path
safe_reports = count_safe_reports(file_path)
print(f"Number of safe reports: {safe_reports}")
