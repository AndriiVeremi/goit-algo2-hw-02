def find_min_max(arr):

    # Перевірка чи масив не порожній
    if not arr:
        return None, None

    # Якщо в масиві один елемент.
    if len(arr) == 1:
        return arr[0], arr[0]

    # Ділимо масив навпіл.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Знаходимо min/max для кожної половини.
    min1, max1 = find_min_max(left_half)
    min2, max2 = find_min_max(right_half)

    # Порівнюємо результати з обох половин.
    final_min = min(min1, min2)
    final_max = max(max1, max2)

    return final_min, final_max

# Приклад використання:
if __name__ == "__main__":
    my_array = [3, 5, 1, 9, -2, 7, 8, 4, 6, 0]
    min_val, max_val = find_min_max(my_array)
    
    print(f"Масив: {my_array}")
    print(f"Мінімальний елемент: {min_val}")
    print(f"Максимальний елемент: {max_val}")
    print("-" * 20)

    
    # Приклад з одним елементом
    my_array_3 = [42]
    min_val_3, max_val_3 = find_min_max(my_array_3)
    
    print(f"Масив: {my_array_3}")
    print(f"Мінімальний елемент: {min_val_3}")
    print(f"Максимальний елемент: {max_val_3}")
