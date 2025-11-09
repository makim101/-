#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Функция поиска скачками (Jump Search)
int jumpSearch(const vector<int>& arr, int target) {
    int n = arr.size();
    
    // Если массив пустой
    if (n == 0) return -1;
    
    // Определяем размер прыжка (обычно √n)
    int jump = sqrt(n);
    int prev = 0;
    
    // Прыгаем вперед, пока не найдем блок, где может быть элемент
    // или пока не выйдем за границы массива
    while (arr[min(jump, n) - 1] < target) {
        prev = jump;
        jump += sqrt(n);
        
        // Если дошли до конца массива и не нашли подходящий блок
        if (prev >= n) return -1;
    }
    
    // Линейный поиск в найденном блоке
    while (prev < min(jump, n)) {
        if (arr[prev] == target) {
            return prev; // Элемент найден
        }
        prev++;
    }
    
    return -1; // Элемент не найден
}

// Функция для вывода массива
void printArray(const vector<int>& arr) {
    cout << "Массив: [";
    for (size_t i = 0; i < arr.size(); i++) {
        cout << arr[i];
        if (i < arr.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
}

int main() {
    // Пример 1: Отсортированный массив
    vector<int> arr1 = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610};
    int target1 = 55;
    
    cout << "=== Пример 1 ===" << endl;
    printArray(arr1);
    cout << "Поиск элемента: " << target1 << endl;
    
    int result1 = jumpSearch(arr1, target1);
    if (result1 != -1) {
        cout << "Элемент найден на позиции: " << result1 << endl;
    } else {
        cout << "Элемент не найден" << endl;
    }
    cout << endl;
    
    // Пример 2: Поиск несуществующего элемента
    vector<int> arr2 = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int target2 = 25;
    
    cout << "=== Пример 2 ===" << endl;
    printArray(arr2);
    cout << "Поиск элемента: " << target2 << endl;
    
    int result2 = jumpSearch(arr2, target2);
    if (result2 != -1) {
        cout << "Элемент найден на позиции: " << result2 << endl;
    } else {
        cout << "Элемент не найден" << endl;
    }
    cout << endl;
    
}
