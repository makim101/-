#include <iostream>

using namespace std;

// Функция сортировки выбором для обычного массива
void selection_sort(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        int min_index = i;
        
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_index]) {
                min_index = j;
            }
        }
        
        // Обмен значений
        int temp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = temp;
    }
}

int main() {
    int test_array[] = {64, 25, 12, 22, 11};
    int n = sizeof(test_array) / sizeof(test_array[0]);
    
    cout << "Исходный массив: ";
    for (int i = 0; i < n; i++) {
        cout << test_array[i] << " ";
    }
    cout << endl;

    selection_sort(test_array, n);

    cout << "Отсортированный массив: ";
    for (int i = 0; i < n; i++) {
        cout << test_array[i] << " ";
    }
    cout << endl;

    return 0;
}
