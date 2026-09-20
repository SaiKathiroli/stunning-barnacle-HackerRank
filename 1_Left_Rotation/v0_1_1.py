def rotate_left(d, arr) -> list:
    arr_length = len(arr)
    if d <= arr_length:
        new_index_location = [index - d for index, value in enumerate(arr)]
    else:
        new_index_location = [arr_length - d + index for index, value in enumerate(arr)]
    rotated_arr = [None] * arr_length
    for i in range(arr_length):
        new_index = new_index_location[i]
        value = arr[i]
        rotated_arr[new_index] = value
    return rotated_arr


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

    passed = 0
    for i, test in enumerate(test_cases):
        # Create a copy of arr in case the function mutates the original list in place
        input_arr = test["arr"].copy()
        result = rotate_left(test["d"], input_arr)

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
