def find_min_max(arr):
    """
    Finds the minimum and maximum elements in an array using the "divide and conquer" method.

    :param arr: A list (array) of numbers.
    :return: A tuple (min_element, max_element).
    """
    # Check if the array is not empty
    if not arr:
        return None, None

    # Base case: if the array has one element, it is both the minimum and the maximum.
    if len(arr) == 1:
        return arr[0], arr[0]

    # Divide: split the array in half.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer: recursively find min/max for each half.
    min1, max1 = find_min_max(left_half)
    min2, max2 = find_min_max(right_half)

    # Combine: compare the results from both halves.
    final_min = min(min1, min2)
    final_max = max(max1, max2)

    return final_min, final_max

# Example usage:
if __name__ == "__main__":
    my_array = [3, 5, 1, 9, -2, 7, 8, 4, 6, 0]
    min_val, max_val = find_min_max(my_array)
    
    print(f"Array: {my_array}")
    print(f"Minimum element: {min_val}")
    print(f"Maximum element: {max_val}")
    print("-" * 20)

    my_array_2 = [100, 20, 300, 4, 500, -10, 0, 1000]
    min_val_2, max_val_2 = find_min_max(my_array_2)
    
    print(f"Array: {my_array_2}")
    print(f"Minimum element: {min_val_2}")
    print(f"Maximum element: {max_val_2}")
    print("-" * 20)
    
    # Example with a single element
    my_array_3 = [42]
    min_val_3, max_val_3 = find_min_max(my_array_3)
    
    print(f"Array: {my_array_3}")
    print(f"Minimum element: {min_val_3}")
    print(f"Maximum element: {max_val_3}")
