import random


# Середня складність: O(n)
# Повертає k-й найменший елемент у масиві
def quick_select(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k має бути в межах від 1 до довжини масиву")
    if len(arr) == 1:
        return arr[0]

    # Обираємо випадковий опорний елемент
    pivot = random.choice(arr)

    # Ділимо масив на частини: менші, рівні, більші за pivot
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k <= len(lows):
        return quick_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return quick_select(highs, k - len(lows) - len(pivots))


# Приклади
arr1 = [7, 10, 4, 3, 20, 15]
k1 = 3
print(f"{k1}-й найменший елемент: {quick_select(arr1, k1)}")

# 2
arr2 = [12, 3, 5, 7, 19]
k2 = 2
print(f"{k2}-й найменший елемент: {quick_select(arr2, k2)}")

# Один елемент
arr3 = [1]
k3 = 1
print(f"{k3}-й найменший елемент: {quick_select(arr3, k3)}")
