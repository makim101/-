def binary_search(arr, target):

    left = 0
    right = len(arr) - 1
    step = 0
    
    print(f"Поиск элемента {target} в массиве: {arr}")
    
    while left <= right:
        step += 1
        mid = (left + right) // 2
        print(f"Шаг {step}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"Элемент найден на позиции {mid}")
            return mid
        elif arr[mid] < target:
            print(f"Искомый элемент справа от mid")
            left = mid + 1
        else:
            print(f"Искомый элемент слева от mid")
            right = mid - 1
    
    print("Элемент не найден")
    return -1

# Пример использования
if __name__ == "__main__":
    # Отсортированный массив
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 45, 67, 89]
    target_element = 23
    
    result = binary_search(sorted_array, target_element)
    
    if result != -1:
        print(f"Элемент {target_element} найден на позиции {result}")
    else:
        print(f"Элемент {target_element} не найден")
