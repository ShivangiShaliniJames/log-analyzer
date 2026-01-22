def count_log_levels(log_lines):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    for line in log_lines:
        for level in counts:
            if level in line:
                counts[level] += 1

    return counts
