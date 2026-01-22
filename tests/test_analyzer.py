from src.analyzer import count_log_levels

def test_log_counting():
    sample_logs = [
        "INFO Application started\n",
        "WARNING Disk usage high\n",
        "ERROR Failed to connect\n",
        "INFO User logged in\n"
    ]

    result = count_log_levels(sample_logs)

    assert result["INFO"] == 2
    assert result["WARNING"] == 1
    assert result["ERROR"] == 1
