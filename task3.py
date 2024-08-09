import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней та пріоритетної черги
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # черга, де зберігаються пари (відстань, вершина)

    while priority_queue:
        # Вибираємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань в черзі більша, ніж вже знайдена, пропускаємо цю вершину
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо нова відстань коротша, оновлюємо найкоротший шлях і додаємо в чергу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад графа у вигляді словника
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

# Виклик функції для вершини A
print(dijkstra(graph, 'A'))
