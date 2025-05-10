def find_min_max(arr):
    # Складність: O(n), бо проходимо всі елементи лише один раз рекурсивно
    #  один елемент
    if len(arr) == 1:
        return arr[0], arr[0]

    # два елементи
    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    # Розділяємо масив навпіл
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Об'єднуємо результати зліва та справа
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)

    return overall_min, overall_max


# Приклади
arr = [7, 2, 9, 4, 1, 6]
min_val, max_val = find_min_max(arr)
print(f"Приклад 1 - Мін: {min_val}, Макс: {max_val}")

# З від'ємними числами
arr2 = [-10, -3, -25, -1]
min_val2, max_val2 = find_min_max(arr2)
print(f"Приклад 2 - Мін: {min_val2}, Макс: {max_val2}")

# Один елемент
arr3 = [42]
min_val3, max_val3 = find_min_max(arr3)
print(f"Приклад 3 - Мін: {min_val3}, Макс: {max_val3}")
