def ternary_search_min(f, left, right, eps=1e-9, max_iter=100): #тернарный поиск минимума унимодальной функции f на отрезке [left, right]
    for _ in range(max_iter):
        if abs(right - left) < eps:
            break
            
        # Вычисляем две внутренние точки
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        
        # Сравниваем значения функции в этих точках
        if f(m1) < f(m2):
            right = m2  # Минимум в левой части
        else:
            left = m1   # Минимум в правой части
    
    return (left + right) / 2

def ternary_search_max(f, left, right, eps=1e-9, max_iter=100): #Тернарный поиск максимума унимодальной функции f на отрезке [left, right]
    for _ in range(max_iter):
        if abs(right - left) < eps:
            break
            
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        
        if f(m1) > f(m2):
            right = m2  # Максимум в левой части
        else:
            left = m1   # Максимум в правой части
    
    return (left + right) / 2

import math

# Пример 1: Поиск минимума параболы
def parabola(x):
    return (x - 3)**2 + 2

# Пример 2: Поиск максимума перевернутой параболы
def inverted_parabola(x):
    return -(x - 2)**2 + 5

# Пример 3: Поиск минимума функции cos(x)
def cos_function(x):
    return math.cos(x)

if __name__ == "__main__":
    print("=== Тернарный поиск минимума ===")
    min_x = ternary_search_min(parabola, 0, 6)
    print(f"Минимум параболы (x-3)²+2: x = {min_x:.6f}, f(x) = {parabola(min_x):.6f}")
    print(f"Ожидаемый минимум: x = 3.0")
    
    print("\n=== Тернарный поиск максимума ===")
    max_x = ternary_search_max(inverted_parabola, -2, 6)
    print(f"Максимум функции -(x-2)²+5: x = {max_x:.6f}, f(x) = {inverted_parabola(max_x):.6f}")
    print(f"Ожидаемый максимум: x = 2.0")
    
    print("\n=== Поиск минимума cos(x) на [0, 2π] ===")
    min_cos = ternary_search_min(cos_function, 0, 2 * math.pi)
    print(f"Минимум cos(x): x = {min_cos:.6f} радиан = {math.degrees(min_cos):.2f}°")
    print(f"f(x) = {cos_function(min_cos):.6f}")
    print(f"Ожидаемый минимум: x = π ≈ {math.pi:.6f}")
