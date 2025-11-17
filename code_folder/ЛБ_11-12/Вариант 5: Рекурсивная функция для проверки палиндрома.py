def is_palindrome(s):
 
    # Приводим строку к нижнему регистру и убираем пробелы
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    print(f"Проверка строки: '{s}'")
    
    # Вспомогательная рекурсивная функция
    def check_palindrome(left, right):
        print(f"  Сравнение индексов [{left}:{s[left]}] и [{right}:{s[right]}]")
        
        # Базовый случай: прошли всю строку
        if left >= right:
            print("  Базовый случай: строка пройдена полностью")
            return True
        
        # Если символы не совпадают - не палиндром
        if s[left] != s[right]:
            print(f"  Символы не совпадают: '{s[left]}' != '{s[right]}'")
            return False
        
        # Рекурсивный случай: проверяем внутреннюю подстроку
        print(f"  Символы совпадают, проверяем подстроку от {left+1} до {right-1}")
        return check_palindrome(left + 1, right - 1)
    
    # Запускаем рекурсию для всей строки
    return check_palindrome(0, len(s) - 1)

# Альтернативная более простая версия
def is_palindrome_simple(s):
 
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Базовые случаи
    if len(s) <= 1:
        return True
    
    # Рекурсивный случай
    if s[0] == s[-1]:
        return is_palindrome_simple(s[1:-1])
    else:
        return False

# Пример использования
if __name__ == "__main__":
    test_strings = ["radar", "Hello", "A man a plan a canal Panama", "12321"]
    
    for test_str in test_strings:
        print(f"\nПроверка: '{test_str}'")
        result = is_palindrome(test_str)
        print(f"Результат: {'Палиндром' if result else 'Не палиндром'}")
        
        # Проверка упрощенной версией
        result_simple = is_palindrome_simple(test_str)
        print(f"Упрощенная проверка: {'Палиндром' if result_simple else 'Не палиндром'}")
