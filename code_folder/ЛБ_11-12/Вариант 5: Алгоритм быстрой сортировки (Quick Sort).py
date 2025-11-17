def quick_sort(arr):

    # Базовый случай: массивы длиной 0 или 1 уже отсортированы
    if len(arr) <= 1:
        return arr
    
    # Выбор опорного элемента (pivot)
    pivot = arr[len(arr) // 2]
    print(f"Опорный элемент: {pivot}")
    
    # Разделение массива на три части
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    print(f"Левая часть: {left}, Средняя: {middle}, Правая: {right}")
    
    # Рекурсивная сортировка левой и правой частей
    return quick_sort(left) + middle + quick_sort(right)

# Пример использования
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Исходный массив: {numbers}")
    
    sorted_numbers = quick_sort(numbers)
    print(f"Отсортированный массив: {sorted_numbers}")
