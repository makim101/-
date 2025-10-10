import java.util.*;

public class SimpleGraph2 {
    public static void main(String[] args) {
        // Создаем граф используя HashMap
        // Ключ - вершина, Значение - список соединенных вершин
        Map<Integer, List<Integer>> graph = new HashMap<>();
        
        // Добавляем вершины
        graph.put(0, new ArrayList<>());
        graph.put(1, new ArrayList<>());
        graph.put(2, new ArrayList<>());
        graph.put(3, new ArrayList<>());
        graph.put(4, new ArrayList<>());
        
        // Добавляем ребра
        // Вершина 0 соединена с 1 и 2
        graph.get(0).add(1);
        graph.get(0).add(2);
        
        // Вершина 1 соединена с 0 и 3
        graph.get(1).add(0);
        graph.get(1).add(3);
        
        // Вершина 2 соединена с 0 и 4
        graph.get(2).add(0);
        graph.get(2).add(4);
        
        // Вершина 3 соединена с 1 и 4
        graph.get(3).add(1);
        graph.get(3).add(4);
        
        // Вершина 4 соединена с 2 и 3
        graph.get(4).add(2);
        graph.get(4).add(3);
        
        // Выводим граф
        System.out.println("Наш граф:");
        for (int vertex : graph.keySet()) {
            System.out.println("Вершина " + vertex + " соединена с: " + graph.get(vertex));
        }
        
        // Проверяем конкретные соединения
        System.out.println("\nС кем соединена вершина 0? " + graph.get(0));
        System.out.println("С кем соединена вершина 3? " + graph.get(3));
    }
}
