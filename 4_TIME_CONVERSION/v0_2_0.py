#!/bin/python3

def timeConversion(s: str) -> str:
    """
    Converts a time string in 12-hour AM/PM format to 24-hour military time.

    Args:
        s (str): A time in 12-hour format (e.g., '07:05:45PM').

    Returns:
        str: The time in 24-hour format (e.g., '19:05:45').
    """
    # Isolate the components based on the fixed 10-character string length
    hour = s[:2]
    minutes_seconds = s[2:8]
    meridian = s[-2:]

    if meridian == 'AM':
        # Edge Case: 12 AM becomes 00. All other AM hours remain the same.
        if hour == '12':
            hour = '00'
    else:  # PM
        # Edge Case: 12 PM remains 12. All other PM hours add 12.
        if hour != '12':
            hour = str(int(hour) + 12)

    return hour + minutes_seconds


def run_tests():
    """
    Runs a suite of test cases against the timeConversion function,
    covering standard inputs, edge cases, and boundaries.
    """
    test_cases = [
        # (Input, Expected Output, Description)

        # AM Edge Cases (Midnight transition)
        ("12:00:00AM", "00:00:00", "Edge AM: Exact Midnight"),
        ("12:45:54AM", "00:45:54", "Edge AM: Midnight with minutes and seconds"),

        # AM Standard Cases (01 to 11)
        ("01:00:00AM", "01:00:00", "Standard AM: Lower bound"),
        ("07:05:45AM", "07:05:45", "Standard AM: Mid-morning"),
        ("11:59:59AM", "11:59:59", "Standard AM: Upper bound (just before noon)"),

        # PM Edge Cases (Noon transition)
        ("12:00:00PM", "12:00:00", "Edge PM: Exact Noon"),
        ("12:45:54PM", "12:45:54", "Edge PM: Noon with minutes and seconds"),

        # PM Standard Cases (01 to 11)
        ("01:00:00PM", "13:00:00", "Standard PM: Lower bound"),
        ("07:05:45PM", "19:05:45", "Standard PM: Evening"),
        ("11:59:59PM", "23:59:59", "Standard PM: Upper bound (just before midnight)")
    ]

    passed = 0
    total = len(test_cases)

    print("--- Running Time Conversion Tests ---\n")

    for i, (input_time, expected, desc) in enumerate(test_cases, 1):
        result = timeConversion(input_time)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
            passed += 1
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input:    {input_time}")
            print(f"   Expected: {expected}")
            print(f"   Got:      {result}")

    print(f"\n--- Results: {passed}/{total} Tests Passed ---")


if __name__ == '__main__':
    # When run locally, this will execute the test suite
    run_tests()