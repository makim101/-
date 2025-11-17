def merge_sort(arr):

    # Базовый случай: массивы длиной 0 или 1 уже отсортированы
    if len(arr) <= 1:
        return arr
    
    print(f"Разделение массива: {arr}")
    
    # Разделение массива на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    print(f"Левая половина: {left_half}, Правая половина: {right_half}")
    
    # Рекурсивная сортировка обеих половин
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Слияние отсортированных половин
    return merge(left_sorted, right_sorted)

def merge(left, right):

    result = []
    i = j = 0
    
    print(f"Слияние массивов: {left} и {right}")
    
    # Слияние элементов в порядке возрастания
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Добавление оставшихся элементов
    result.extend(left[i:])
    result.extend(right[j:])
    
    print(f"Результат слияния: {result}")
    return result

# Пример использования
if __name__ == "__main__":
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print(f"Исходный массив: {numbers}")
    
    sorted_numbers = merge_sort(numbers)
    print(f"Отсортированный массив: {sorted_numbers}")
