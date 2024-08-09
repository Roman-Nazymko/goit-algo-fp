import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Лівий нащадок
        self.right = None  # Правий нащадок
        self.val = key  # Значення вузла
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Додавання ребер та вузлів до графа, який представляє дерево."""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    """Відображення дерева з обходом у ширину (BFS) та глибину (DFS)."""
    tree = nx.DiGraph()  # Орієнтований граф
    pos = {tree_root.id: (0, 0)}  # Початкова позиція для кореневого вузла
    tree = add_edges(tree, tree_root, pos)

    initial_color = 'skyblue'  # Початковий колір для вузлів
    bfs_nodes = bfs(tree_root)  # Вузли при обході в ширину
    dfs_nodes = dfs(tree_root)  # Вузли при обході в глибину

    plt.figure(figsize=(16, 8))

    # Відображення обходу в ширину
    plt.subplot(1, 2, 1)
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=initial_color)
    plt.title('BFS Traversal')

    for step, node in enumerate(bfs_nodes, 1):
        node.color = generate_color(step, len(bfs_nodes))
        tree.nodes[node.id]['color'] = node.color
        colors = [tree.nodes[n]['color'] for n in tree.nodes]
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.pause(0.5)

    # Відновлення кольору після BFS
    for node in tree.nodes:
        tree.nodes[node]['color'] = initial_color

    # Відображення обходу в глибину
    plt.subplot(1, 2, 2)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=initial_color)
    plt.title('DFS Traversal')

    for step, node in enumerate(dfs_nodes, 1):
        node.color = generate_color(step, len(dfs_nodes))
        tree.nodes[node.id]['color'] = node.color
        colors = [tree.nodes[n]['color'] for n in tree.nodes]
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.pause(0.5)

    plt.show()


def generate_color(step, total_steps):
    """Генерація n кольорів від темного до світлого."""
    hsv_color = (step / total_steps, 0.8, 0.8)
    rgb_color = colorsys.hsv_to_rgb(*hsv_color)
    return '#%02x%02x%02x' % tuple(int(c * 255) for c in rgb_color)


def bfs(root):
    """Обхід в ширину (BFS)."""
    queue = [root]
    visited_nodes = []
    while queue:
        node = queue.pop(0)
        visited_nodes.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited_nodes


def dfs(root):
    """Обхід в глибину (DFS)."""
    stack = [root]
    visited_nodes = []
    while stack:
        node = stack.pop()
        visited_nodes.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited_nodes


def insert_node(heap, value):
    """Вставка значення в бінарну купу та збереження властивості купи."""
    heap.append(value)
    i = len(heap) - 1

    # Відновлення властивості купи
    while i > 0 and heap[(i - 1) // 2] > heap[i]:
        heap[(i - 1) // 2], heap[i] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2


def heap_to_tree(heap):
    """Перетворення списку двійкової купи на двійкове дерево."""
    if not heap:
        return None

    nodes = [Node(val) for val in heap]

    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0]


# Створення бінарної купи
heap = []
insert_node(heap, 5)
insert_node(heap, 3)
insert_node(heap, 8)
insert_node(heap, 1)
insert_node(heap, 2)
insert_node(heap, 7)
insert_node(heap, 6)

# Перетворення купи в дерево
root = heap_to_tree(heap)

# Відображення дерева
draw_tree(root)
