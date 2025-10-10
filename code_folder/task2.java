//создание графа на джава
static Graph createGraph() {
    Graph graph = new Graph();
    //Добавление элементов
    graph.addVertex("Bob");
    graph.addVertex("Alice");
    graph.addVertex("Mark");
    graph.addVertex("Rob");
    graph.addVertex("Maria");
    //Добавление рёбер
    graph.addEdge("Bob", "Maria");
    graph.addEdge("Bob", "Mark");
    graph.addEdge("Maria", "Alice");
    graph.addEdge("Mark", "Alice");
    graph.addEdge("Maria", "Rob");
    graph.addEdge("Mark", "Rob");

    return graph;
}
