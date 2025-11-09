#include <iostream>
#include <vector>
#include <algorithm>

// Бинарный поиск в заданном диапазоне
int binarySearch(const std::vector<int>& arr, int left, int right, int target) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1; // Элемент не найден
}

// Экспоненциальный поиск
int exponentialSearch(const std::vector<int>& arr, int target) {
    int n = arr.size();
    
    // Если массив пустой
    if (n == 0) {
        return -1;
    }
    
    // Если искомый элемент - первый элемент
    if (arr[0] == target) {
        return 0;
    }
    
    // Находим диапазон для бинарного поиска
    int i = 1;
    while (i < n && arr[i] <= target) {
        i *= 2;
    }
    
    // Определяем границы для бинарного поиска
    int left = i / 2;
    int right = std::min(i, n - 1);
    
    // Выполняем бинарный поиск в найденном диапазоне
    return binarySearch(arr, left, right, target);
}

// Функция для вывода массива
void printArray(const std::vector<int>& arr) {
    std::cout << "[";
    for (size_t i = 0; i < arr.size(); ++i) {
        std::cout << arr[i];
        if (i != arr.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;
}

int main() {
    // Пример использования
    std::vector<int> arr = {2, 3, 4, 10, 15, 18, 23, 35, 42, 51, 67, 89};
    int target = 23;
    
    std::cout << "Отсортированный массив: ";
    printArray(arr);
    std::cout << "Ищем элемент: " << target << std::endl;
    
    int result = exponentialSearch(arr, target);
    
    if (result != -1) {
        std::cout << "Элемент найден на позиции: " << result << std::endl;
    } else {
        std::cout << "Элемент не найден в массиве" << std::endl;
    }
    
    // Дополнительные примеры
    std::cout << "\n--- Дополнительные примеры ---" << std::endl;
    
    // Пример 1: Поиск несуществующего элемента
    target = 100;
    result = exponentialSearch(arr, target);
    std::cout << "Поиск " << target << ": " 
              << (result != -1 ? "найден на позиции " + std::to_string(result) : "не найден") 
              << std::endl;
    
    // Пример 2: Поиск первого элемента
    target = 2;
    result = exponentialSearch(arr, target);
    std::cout << "Поиск " << target << ": " 
              << (result != -1 ? "найден на позиции " + std::to_string(result) : "не найден") 
              << std::endl;
    
    // Пример 3: Поиск последнего элемента
    target = 89;
    result = exponentialSearch(arr, target);
    std::cout << "Поиск " << target << ": " 
              << (result != -1 ? "найден на позиции " + std::to_string(result) : "не найден") 
              << std::endl;
    
    return 0;
}
