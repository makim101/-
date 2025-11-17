def is_sorted(arr, index=0):

    print(f"Проверка массива: {arr}, текущий индекс: {index}")
    
    # Базовый случай: дошли до конца массива
    if index >= len(arr) - 1:
        print("Базовый случай: массив пройден полностью - отсортирован")
        return True
    
    # Проверяем, что текущий элемент не больше следующего
    if arr[index] > arr[index + 1]:
        print(f"Нарушение сортировки: {arr[index]} > {arr[index + 1]}")
        return False
    
    print(f"Элементы {arr[index]} <= {arr[index + 1]} - OK, переходим к следующей паре")
    
    # Рекурсивный случай: проверяем остальную часть массива
    return is_sorted(arr, index + 1)

# Версия с проверкой направления сортировки
def is_sorted_general(arr, ascending=True, index=0):

    if index >= len(arr) - 1:
        return True
    
    if ascending:
        if arr[index] > arr[index + 1]:
            return False
    else:
        if arr[index] < arr[index + 1]:
            return False
    
    return is_sorted_general(arr, ascending, index + 1)

# Пример использования
if __name__ == "__main__":
    test_arrays = [
        [1, 2, 3, 4, 5],           # Отсортирован
        [5, 4, 3, 2, 1],           # Не отсортирован по возрастанию
        [1, 3, 2, 4, 5],           # Не отсортирован
        [1],                        # Один элемент
        []                          # Пустой массив
    ]
    
    for i, arr in enumerate(test_arrays):
        print(f"\n=== Тест {i+1} ===")
        print(f"Массив: {arr}")
        result = is_sorted(arr)
        print(f"Результат: {'Отсортирован' if result else 'Не отсортирован'}")
