def analyze_log(file_path):
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    try:
        with open(file_path, "r") as file:
            for line in file:
                for level in counts:
                    if line.startswith(level):
                        counts[level] += 1
    except FileNotFoundError:
        print("Log file not found.")
        return

    print("Log Analysis Report")
    print("-------------------")
    for level, count in counts.items():
        print(f"{level}: {count}")


if __name__ == "__main__":
    analyze_log("logs/sample.log")
