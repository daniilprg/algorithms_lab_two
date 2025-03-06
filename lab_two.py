graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
]

def DFS(el, current_graph):
    """Обход в глубину. Проверка наличия циклов в графе."""
    visit_array[el] = 1  # Помечаем вершину как посещаемую (в процессе)
    for neigh in range(len(current_graph)):
        if current_graph[el][neigh] == 0:
            continue  # Пропускаем вершины, с которыми нет связи
        if visit_array[neigh] == 0:  # Если вершина не посещена, запускаем DFS
            if DFS(neigh, current_graph):
                return True  # Найден цикл
        if visit_array[neigh] == 1:  # Если вершина уже посещается, значит, цикл найден
            return True
    visit_array[el] = 2  # Отмечаем вершину как полностью обработанную
    return False

def BFS(el, current_graph):
    """Обход в ширину. Подсчёт диаметра графа."""
    deque.append(el)  # Добавляем стартовую вершину в очередь
    count = 10
    while deque and count > 0:
        curr = deque.pop()  # Извлекаем вершину из очереди
        visited.add(curr)  # Добавляем её в множество посещённых
        for neigh in range(len(current_graph)):
            if current_graph[curr][neigh] == 0:
                continue  # Пропускаем вершины без связи
            if neigh not in visited:  # Если вершина ещё не посещена
                deque.append(neigh)  # Добавляем её в очередь
                distances_array[neigh] = distances_array[curr] + 1  # Увеличиваем расстояние
        count -= 1
    return max(distances_array)  # Возвращаем диаметр

def print_graph(current_graph):
    """Вывод графа в консоль."""
    print('Текущий граф:')
    for el in current_graph:
        print(' '.join(map(str, el)))
    print()

def run(current_graph):
    """Основная функция анализа графа."""
    global visited, deque, visit_array, distances_array
    visited = set()  # Множество для хранения посещённых вершин

    from collections import deque
    deque = deque()  # Очередь для обхода в ширину

    visit_array = [0 for _ in range(len(current_graph))]  # 0 - не посещена, 1 - посещается, 2 - обработана
    distances_array = [0 for _ in range(len(current_graph))]  # Хранение расстояний от стартовой вершины

    print_graph(current_graph)  # Выводим граф в консоль
    count_trees = 0  # Количество деревьев

    for i in range(len(current_graph)):
        if visit_array[i] == 0:  # Если вершина не посещена
            if DFS(i, current_graph):  # Запускаем обход в глубину, если находим цикл, увеличиваем счётчик
                count_trees += 1
            for j in range(len(current_graph)):
                if visit_array[j] == 1:
                    visit_array[j] = 2  # Отмечаем вершины как обработанные

    print(f'Диаметр графа: {BFS(0, current_graph)}')  # Вычисляем диаметр графа через обход в ширину, выводим
    print(f'Количество деревьев в графе: {count_trees}')  # Выводим число деревьев

if __name__ == '__main__':
    run(graph)
