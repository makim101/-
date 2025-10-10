#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Структура для представления вершины графа
struct Vertex {
    int id;
    string name;
};

// Структура для представления графа
struct SimpleGraph {
    vector<Vertex> vertices;
    vector<vector<int>> edges;
    
    // Добавление вершины
    void addVertex(int id, string name) {
        vertices.push_back({id, name});
        edges.push_back(vector<int>());
    }
    
    // Добавление ребра
    void addEdge(int from, int to) {
        edges[from].push_back(to);
        edges[to].push_back(from); // Для неориентированного графа
    }
    
    // Вывод графа
    void printGraph() {
        cout << "Наш граф:" << endl;
        for (const auto& vertex : vertices) {
            cout << "Вершина " << vertex.id << " (" << vertex.name << ") соединена с: ";
            for (int neighbor : edges[vertex.id]) {
                cout << neighbor << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    SimpleGraph graph;
    
    // Добавляем вершины
    graph.addVertex(0, "Москва");
    graph.addVertex(1, "Санкт-Петербург");
    graph.addVertex(2, "Казань");
    graph.addVertex(3, "Новосибирск");
    graph.addVertex(4, "Владивосток");
    
    // Добавляем ребра (дороги между городами)
    graph.addEdge(0, 1); // Москва - СПб
    graph.addEdge(0, 2); // Москва - Казань
    graph.addEdge(1, 2); // СПб - Казань
    graph.addEdge(2, 3); // Казань - Новосибирск
    graph.addEdge(3, 4); // Новосибирск - Владивосток
    
    // Выводим граф
    graph.printGraph();
    
    // Проверяем соединения для Москвы (вершина 0)
    cout << "\nИз Москвы можно добраться в: ";
    for (int neighbor : graph.edges[0]) {
        cout << neighbor << " ";
    }
    cout << endl;
    
    return 0;
}
