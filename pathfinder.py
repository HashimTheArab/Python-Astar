from cmu_graphics import Rect
from math import sqrt

global starting_node
global target_node


class Node:
    parentNode = None
    size = None
    cost = {
        'g': 0.0,
        'h': 0.0
    }

    def __init__(self, rect: Rect):
        self.rect = rect
        self.position = (rect.centerX, rect.centerY)
        PathFinder.nodes[self.position] = self

    def neighbors(self, include_corners: bool) -> list:
        x, y = self.position
        size = self.size
        neighbors = [(x - size, y), (x + size, y), (x, y - size), (x, y + size)]
        if include_corners:
            neighbors.extend([(x - size, y + size), (x - size, y - size), (x + size, y - size), (x + size, y + size)])
        return neighbors

    def set_g_cost(self, path: dict):  # Todo
        """cost = 0
        self_x, self_y = self.position
        for node in list(reversed(path.keys())):
            x, y = node
            if x == self_x or y == self_y:
                cost += 10
            else:
                cost += 14"""
        self.cost['g'] = 0

    def set_h_cost(self):
        x = target_node.position[0] - self.position[0]
        y = target_node.position[1] - self.position[1]
        self.cost['h'] = sqrt((x / Node.size) ** 2 + (y / Node.size) ** 2)


class PathFinder:
    nodes = {}
    open = {}
    closed = {}
    path = {}

    def __init__(self, size: int, t_node: Node, include_corners: bool):
        self.size = size
        global target_node
        target_node = t_node
        self.include_corners = include_corners

    def start(self):
        selected_node: Node = list(self.open.values())[0]
        f_costs = self.handle_nodes(selected_node)
        self.close_node(selected_node)
        selected_node.rect.fill = 'green'

        while True:
            if len(f_costs) == 0:
                print("no path could be found")
                break
            selected_node: Node = min(f_costs.keys(), key=f_costs.__getitem__)
            self.path[selected_node.position] = selected_node
            if selected_node.position == target_node.position:
                print("path found!")
                break
            f_costs = self.handle_nodes(selected_node)
            self.close_node(selected_node)

    def handle_nodes(self, selected_node: Node) -> dict:
        f_costs = {}
        neighbors = selected_node.neighbors(self.include_corners)
        for pos in neighbors:
            if pos not in self.nodes or pos in self.closed:
                continue
            node = self.nodes[pos]
            if node.rect.fill != 'white':
                continue
            node.rect.fill = 'lightSalmon'
            node.parentNode = selected_node
            node.set_g_cost(self.path)
            node.set_h_cost()
            self.open[pos] = node
            """if pos in self.open:
                if node.get_g_cost(selected_node) < node.cost['g']:
                    node.parentNode = selected_node
                    node.set_g_cost(self.path)"""
            f_costs[node] = node.cost['g'] + node.cost['h']
        return f_costs

    def close_node(self, node: Node):
        del self.open[node.position]
        self.closed[node.position] = node
        node.rect.fill = 'mediumSlateBlue'
