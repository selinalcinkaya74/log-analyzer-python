
def analyze_log(file_path):
    error_count = 0
    warning_count = 0
    info_count = 0

    error_lines = []

    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
                error_lines.append(line.strip())
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

    print("Log Analysis Results:")
    print("---------------------")
    print(f"ERROR: {error_count}")
    print(f"WARNING: {warning_count}")
    print(f"INFO: {info_count}")

    print("\nSample ERROR lines:")
    for err in error_lines[:5]:
        print(err)

analyze_log("example.log")