def power(x, n):

    # Базовый случай: любое число в степени 0 равно 1
    if n == 0:
        print(f"Базовый случай: {x}^0 = 1")
        return 1
    
    # Базовый случай: любое число в степени 1 равно самому числу
    if n == 1:
        print(f"Базовый случай: {x}^1 = {x}")
        return x
    
    # Рекурсивный случай: x^n = x * x^(n-1)
    print(f"Рекурсивный вызов: {x}^{n} = {x} * {x}^{n-1}")
    result = x * power(x, n - 1)
    print(f"Возврат: {x}^{n} = {result}")
    
    return result

# Оптимизированная версия для четных степеней
def power_optimized(x, n):
 
    if n == 0:
        return 1
    if n == 1:
        return x
    
    # Если степень четная: x^n = (x^(n/2))^2
    if n % 2 == 0:
        half_power = power_optimized(x, n // 2)
        return half_power * half_power
    # Если степень нечетная: x^n = x * (x^((n-1)/2))^2
    else:
        half_power = power_optimized(x, (n - 1) // 2)
        return x * half_power * half_power

# Пример использования
if __name__ == "__main__":
    print("=== Базовая версия ===")
    base = 2
    exponent = 5
    result = power(base, exponent)
    print(f"Результат: {base}^{exponent} = {result}")
    
    print("\n=== Оптимизированная версия ===")
    result_opt = power_optimized(base, exponent)
    print(f"Результат: {base}^{exponent} = {result_opt}")
