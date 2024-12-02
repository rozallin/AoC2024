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

def is_safe_with_dampener(report):
    """Check if a report can be made safe by removing a single level."""
    levels = list(map(int, report.split()))
    
    for i in range(len(levels)):
        # Create a new report excluding the ith level
        modified_levels = levels[:i] + levels[i+1:]
        modified_report = " ".join(map(str, modified_levels))
        
        # Check if the modified report is safe
        if is_safe_report(modified_report):
            return True
    
    return False

def count_safe_reports(file_path):
    """Count the number of safe reports in a file, considering the Problem Dampener."""
    safe_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            report = line.strip()
            if is_safe_report(report) or is_safe_with_dampener(report):
                safe_count += 1

    return safe_count

# Example usage:
file_path = 'AoC2024Q2a_input.txt'
safe_reports = count_safe_reports(file_path)
print(f"Number of safe reports: {safe_reports}")
