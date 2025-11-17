def generate_binary_strings(n):
  
    result = []
    
    def backtrack(current):
        print(f"Текущая строка: '{current}'")
        
        # Базовый случай: достигнута нужная длина
        if len(current) == n:
            print(f"Достигнута длина {n}, добавляем в результат: '{current}'")
            result.append(current)
            return
        
        # Рекурсивный случай: добавляем '0' и '1'
        print(f"Добавляем '0' к '{current}'")
        backtrack(current + '0')
        
        print(f"Добавляем '1' к '{current}'")
        backtrack(current + '1')
    
    print(f"Генерация всех бинарных строк длины {n}")
    backtrack('')
    return result

# Итеративная версия
def generate_binary_strings_iterative(n):
 
    if n == 0:
        return ['']
    
    result = ['']
    for _ in range(n):
        new_result = []
        for s in result:
            new_result.append(s + '0')
            new_result.append(s + '1')
        result = new_result
    
    return result

# Пример использования
if __name__ == "__main__":
    n = 3
    print(f"=== Генерация всех бинарных строк длины {n} ===")
    
    binary_strings = generate_binary_strings(n)
    print(f"\nВсе бинарные строки длины {n}:")
    for i, bs in enumerate(binary_strings):
        print(f"{i+1}: {bs}")
    
    print(f"\nВсего строк: {len(binary_strings)}")
    
    # Проверка итеративной версией
    iterative_result = generate_binary_strings_iterative(n)
    print(f"Проверка итеративной версией: {len(iterative_result)} строк")
