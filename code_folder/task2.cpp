//пример создания графа на С++
#include <iostream>  
#include <vector>  
using namespace std;  
class Graph {  
// Матрица инцидентности для хранения рёбер графа  
vector<vector<int> > adj_matrix;  
public:  
//Создание графа с n вершинами  
Graph(int n) { adj_matrix = vector<vector<int> >(n, vector<int>(n, 0)); }  
//Добавление ребра между вершинами u и v  
void add_edge(int u, int v) {  
// Установить ребро от u к v  
adj_matrix[u][v] = 1;  
// Установить ребро от v к u (для неориентированного графа)  
adj_matrix[v][u] = 1;  
}  
// Функция для печати представления графа с использованием матрицы инцидентности  
void print() {  
// Итерироваться по каждой вершине  
for (auto i : adj_matrix) {  
// Вывести вершину  
cout << i.first << " -> ";  
// Итерироваться по связанным вершинам  
for (auto j : i.second) {  
// Вывести связанную вершину  
cout << j << " ";  
}  
cout << endl;  
}  
}  
};  
int main() {  
// Создать объект графа  
Graph g;  
// Добавление ребер в граф  
g.add_edge(1, 0);  
g.add_edge(2, 0);  
g.add_edge(1, 2);  
//вывод графа
g.print();  
return 0;  
}
