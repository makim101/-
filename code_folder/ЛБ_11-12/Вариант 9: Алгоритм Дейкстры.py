import heapq
import math

def dijkstra(graph, start):

    # Инициализация расстояний (бесконечность для всех вершин кроме стартовой)
    distances = {vertex: math.inf for vertex in graph}
    distances[start] = 0
    
    # Очередь с приоритетом для обработки вершин
    priority_queue = [(0, start)]
    
    print(f"Начальная вершина: {start}, расстояние: 0")
    
    while priority_queue:
        # Извлекаем вершину с минимальным расстоянием
        current_distance, current_vertex = heapq.heappop(priority_queue)
        print(f"\nОбрабатываем вершину {current_vertex}, расстояние: {current_distance}")
        
        # Если найденное расстояние больше известного, пропускаем
        if current_distance > distances[current_vertex]:
            continue
        
        # Обновляем расстояния до соседей
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            print(f"  Проверяем соседа {neighbor}, вес ребра: {weight}")
            
            # Если найден более короткий путь
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                print(f"  Обновлено расстояние до {neighbor}: {distance}")
    
    return distances

# Пример использования
if __name__ == "__main__":
    # Взвешенный граф
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    start_vertex = 'A'
    shortest_paths = dijkstra(graph, start_vertex)
    
    print(f"\nКратчайшие расстояния от вершины {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"  До {vertex}: {distance}")
