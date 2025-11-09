def pancake_sort(arr):
    n = len(arr)
  
    # Поочередно размещаем наибольший элемент в конец
    for curr_size in range(n, 1, -1):
        # Находим индекс максимального элемента в несортированной части
        max_index = arr.index(max(arr[:curr_size]))
        
        # Если максимальный элемент не на своем месте
        if max_index != curr_size - 1:
            # Переворачиваем так, чтобы максимальный элемент оказался в начале
            if max_index != 0:
                flip(arr, max_index)
            # Переворачиваем несортированную часть, чтобы максимальный элемент оказался в конце
            flip(arr, curr_size - 1)
    
    return arr

def flip(arr, k): #переворачивает массив от начала до индекса k
  
    left = 0
    while left < k:
        arr[left], arr[k] = arr[k], arr[left]
        left += 1
        k -= 1
def examples():
    arr1 = [23, 10, 20, 11, 12, 6, 7]
    print(f"Исходный массив: {arr1}")
    result1 = pancake_sort(arr1.copy())
    print(f"Отсортированный: {result1}")
examples()
