import re
import queue

class Graph(object):
    def __init__(self, size):
        self.vertices = []
        self.matrix = []
        for _ in range(size):
            self.matrix.append([0 for i in range(size)])
        self.size = size

    
    def add_vertice(self, v1, v2, weight):
        idx1 = self.get_index(v1)
        idx2 = self.get_index(v2)
        self.matrix[idx1][idx2] = weight
    
    def get_index(self, vertice_name):
        if vertice_name not in self.vertices:
            self.vertices.append(vertice_name)
        return self.vertices.index(vertice_name)
    
    def get_index_name(self, vertice_index):
        return self.vertices[vertice_index]

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))

    def get_parent_colors(self, vertice_name):
        j = self.vertices.index(vertice_name)
        parents = []
        for i in range(len(self.matrix)):
            if self.matrix[i][j] != 0:
                parents.append(i)
        return list(map(self.get_index_name, parents))

    def count_bags_inside(self, start_color):
        i = self.vertices.index(start_color)
        return self._count_bags_inside(i)

    def _count_bags_inside(self, vertice_start):
        i = vertice_start
        total = 0
        for j in range(len(self.matrix)):
            weight = self.matrix[i][j]
            if weight != 0:
                total += weight * (1 + self._count_bags_inside(j))
        return total

def get_parent_colors(graph, start_color):
    found_parents = set()
    to_check = [start_color]
    while len(to_check) > 0:
        parent = to_check.pop()
        new_parents = [p for p in g.get_parent_colors(parent) if p not in found_parents]
        to_check = to_check + list(new_parents)
        found_parents.add(parent)
    return len(found_parents)-1



pattern = r'(bags? ?|contain |, |\.)|(no other bags\.)'
with open('inputs/07.txt', 'r') as f:
    lines = f.readlines()

g = Graph(len(lines))

for line in lines:
    chunks = re.sub(pattern, '', line).split(" ")[:-1]
    v1 = "".join(chunks[:2])
    
    for i in range(2, len(chunks), 3):
        weight, adj, color = chunks[i:i+3]
        g.add_vertice(v1, adj+color, int(weight))


print(get_parent_colors(g, "shinygold"))
print(g.count_bags_inside("shinygold"))
