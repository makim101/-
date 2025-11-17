def dfs(graph, start, visited=None):

    # Инициализация множества посещенных вершин при первом вызове
    if visited is None:
        visited = set()
    
    # Добавляем текущую вершину в посещенные
    visited.add(start)
    result = [start]  # Список для хранения порядка обхода
    
    print(f"Посещаем вершину: {start}")
    
    # Рекурсивно посещаем всех непосещенных соседей
    for neighbor in graph[start]:
        if neighbor not in visited:
            print(f"Переход из {start} в {neighbor}")
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# Пример использования
if __name__ == "__main__":
    # Граф в виде списка смежности
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("Обход графа в глубину (DFS):")
    traversal_order = dfs(graph, 'A')
    print(f"Порядок обхода: {traversal_order}")
