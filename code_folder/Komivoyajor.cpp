#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class TravelingSalesman {
private:
    vector<vector<int>> graph; // матрица расстояний между городами
    int numCities; // количество городов

public:
    TravelingSalesman(vector<vector<int>> distances) {
        graph = distances;
        numCities = distances.size();
    }

    // Метод для вычисления минимального пути коммивояжера
    int solveTSP() {
        // Создаем вектор с номерами всех городов (кроме начального)
        vector<int> cities;
        for (int i = 1; i < numCities; i++) {
            cities.push_back(i);
        }

        int minPath = INT_MAX; // начальное значение минимального пути

        // Перебираем все возможные перестановки городов
        do {
            // Вычисляем стоимость текущего пути
            int currentPath = 0;
            
            // Добавляем расстояние от начального города до первого
            currentPath += graph[0][cities[0]];
            
            // Добавляем расстояния между остальными городами
            for (int i = 0; i < cities.size() - 1; i++) {
                currentPath += graph[cities[i]][cities[i + 1]];
            }
            
            // Возвращаемся в начальный город
            currentPath += graph[cities[cities.size() - 1]][0];
            
            // Обновляем минимальный путь, если нашли лучше
            if (currentPath < minPath) {
                minPath = currentPath;
            }
            
        } while (next_permutation(cities.begin(), cities.end()));

        return minPath;
    }

    // Метод для вывода матрицы расстояний
    void printGraph() {
        cout << "Матрица расстояний:" << endl;
        for (int i = 0; i < numCities; i++) {
            for (int j = 0; j < numCities; j++) {
                cout << graph[i][j] << "\t";
            }
            cout << endl;
        }
    }
};

int main() {
    // Пример матрицы расстояний между 4 городами
    // Город 0: A, Город 1: B, Город 2: C, Город 3: D
    vector<vector<int>> distances = {
        {0, 10, 15, 20},  // Расстояния от города A
        {10, 0, 35, 25},   // Расстояния от города B
        {15, 35, 0, 30},   // Расстояния от города C
        {20, 25, 30, 0}    // Расстояния от города D
    };

    // Создаем объект коммивояжера
    TravelingSalesman tsp(distances);
    
    // Выводим матрицу расстояний
    tsp.printGraph();
    
    // Решаем задачу
    int result = tsp.solveTSP();
    
    cout << "\nМинимальная длина пути: " << result << endl;
    
    return 0;
}
