def rotate_left_brute_force(d: int, arr: list) -> list:
    n = len(arr)
    if n <= 1:
        return arr
    d = d % n

    for _ in range(d):
        first_element = arr[0]

        for i in range(n - 1):
            arr[i] = arr[i + 1]

        arr[n - 1] = first_element

    return arr


def run_tests():
    test_cases = [
        {"name": "Standard (d=4)", "d": 4, "arr": [1, 2, 3, 4, 5], "expected": [5, 1, 2, 3, 4]},
        {"name": "Standard (d=2)", "d": 2, "arr": [1, 2, 3, 4, 5], "expected": [3, 4, 5, 1, 2]},
        {"name": "Zero Rotation", "d": 0, "arr": [1, 2, 3, 4, 5], "expected": [1, 2, 3, 4, 5]},
        {"name": "Full Rotation", "d": 5, "arr": [1, 2, 3, 4, 5], "expected": [1, 2, 3, 4, 5]},
        {"name": "Wrap-around (d=7)", "d": 7, "arr": [1, 2, 3, 4, 5], "expected": [3, 4, 5, 1, 2]},
        {"name": "Single Element", "d": 3, "arr": [42], "expected": [42]},
        {"name": "Empty Array", "d": 2, "arr": [], "expected": []},
        {"name": "Negative Values", "d": 2, "arr": [-1, -2, -3, -4], "expected": [-3, -4, -1, -2]},
    ]

    print("--- Testing Naive Brute Force (One-By-One Shift) ---")
    run_suite(rotate_left_brute_force, test_cases)


def run_suite(func, test_cases):
    passed = 0
    for i, test in enumerate(test_cases):
        # Deep copy so in-place mutations don't ruin the baseline test case
        input_arr = test["arr"].copy()
        result = func(test["d"], input_arr)

        if result == test["expected"]:
            passed += 1
        else:
            print(f"❌ Test {i + 1} Failed: {test['name']}")
            print(f"   Input:    d = {test['d']}, arr = {test['arr']}")
            print(f"   Expected: {test['expected']}")
            print(f"   Got:      {result}\n")

    print(f"Passed {passed}/{len(test_cases)} tests.")


if __name__ == "__main__":
    run_tests()
