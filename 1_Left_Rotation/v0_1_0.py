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


def rotate_left_test(d, arr) -> list:
    pass


if __name__ == "__main__":
    array = [1, 2, 3]  # [2,3,1] ; new_index_location - [-4,-3, -2] ; actual - [-1,-3,-2]
    rotate_by = 7

    result = rotate_left(rotate_by, array)
    print(result)

"""

"""
