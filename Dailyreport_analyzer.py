# log_analyzer.py

# Ask user for file name
filename = input("Enter the log file name: ")

try:
    # Open the file
    with open(filename, "r") as file:
        total = 0
        errors = 0
        warnings = 0
        info = 0

        # Read line by line
        for line in file:
            total += 1
            if "ERROR" in line:
                errors += 1
            if "WARNING" in line:
                warnings += 1
            if "INFO" in line:
                info += 1

    # Print summary
    print("\nLog Summary:")
    print(f"Total lines: {total}")
    print(f"Critical Issues (Errors): {errors}")
    print(f"Potential Issues (Warnings): {warnings}")
    print(f"Normal Operations (Info): {info}")

except FileNotFoundError:
    print(f"File '{filename}' not found. Please check the file name.")
    