def bucket_sort(arr): #реализация блочной сортировки чисел в диапазоне от 0 до 1
    if len(arr) == 0:
        return arr
    
    # Создаем пустые корзины
    n = len(arr)
    buckets = [[] for _ in range(n)]
    
    # Распределяем элементы по корзинам
    for num in arr:
        # Вычисляем индекс корзины
        bucket_index = int(num * n)
        buckets[bucket_index].append(num)
    
    # Сортируем каждую корзину
    for bucket in buckets:
        bucket.sort()
    
    # Объединяем отсортированные корзины
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# Пример 
numbers1 = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51, 0.12, 0.89, 0.75]
print("Исходный массив:", numbers1)
sorted1 = bucket_sort(numbers1)
print("Отсортированный:", sorted1)
